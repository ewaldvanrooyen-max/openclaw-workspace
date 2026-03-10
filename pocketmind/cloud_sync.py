"""
PocketMind Cloud Sync Module

Provides cloud backup and sync functionality for paid subscription tiers.
Free users: Local storage only
Paid users: Cloud backup and sync via Google Drive or generic storage

Usage:
    python main.py --backup           # Create backup
    python main.py --restore           # Restore from backup
    python main.py --sync-status       # Check sync status
"""

import os
import json
import hashlib
import shutil
import tarfile
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional, List, Any
from dataclasses import dataclass, asdict
from enum import Enum


class SubscriptionTier(Enum):
    """Subscription tiers for PocketMind."""
    FREE = "free"
    PREMIUM = "premium"
    ENTERPRISE = "enterprise"


@dataclass
class SyncConfig:
    """Configuration for cloud sync."""
    enabled: bool = False
    tier: str = "free"
    provider: str = "local"  # local, google_drive, generic
    last_sync: Optional[str] = None
    backup_count: int = 0
    
    # Google Drive config (for premium tiers)
    credentials_path: Optional[str] = None
    folder_id: Optional[str] = None
    
    # Generic storage config
    storage_url: Optional[str] = None
    storage_key: Optional[str] = None


@dataclass
class BackupManifest:
    """Manifest for a backup."""
    version: str = "1.0"
    created_at: str = ""
    device_id: str = ""
    profile: Optional[Dict] = None
    history: Optional[List] = None
    config: Optional[Dict] = None
    checksums: Dict[str, str] = None
    
    def __post_init__(self):
        if self.checksums is None:
            self.checksums = {}
        if not self.created_at:
            self.created_at = datetime.now().isoformat()


class CloudSync:
    """
    Cloud sync and backup handler for PocketMind.
    
    Supports:
    - Local backup files (all tiers)
    - Google Drive sync (premium)
    - Generic S3-compatible storage (premium)
    """
    
    def __init__(self, data_dir: Optional[str] = None):
        """
        Initialize cloud sync.
        
        Args:
            data_dir: Path to PocketMind data directory (default: ~/.pocketmind/)
        """
        if data_dir:
            self.data_dir = Path(data_dir)
        else:
            self.data_dir = Path.home() / ".pocketmind"
        
        self.backup_dir = self.data_dir / "backups"
        self.config_file = self.data_dir / "sync_config.json"
        self.state_file = self.data_dir / "sync_state.json"
        
        # Ensure backup directory exists
        self.backup_dir.mkdir(parents=True, exist_ok=True)
        
        # Load config
        self.config = self._load_config()
        self.state = self._load_state()
    
    def _load_config(self) -> SyncConfig:
        """Load sync configuration."""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r') as f:
                    data = json.load(f)
                    return SyncConfig(**data)
            except Exception:
                pass
        return SyncConfig()
    
    def _save_config(self) -> bool:
        """Save sync configuration."""
        try:
            with open(self.config_file, 'w') as f:
                json.dump(asdict(self.config), f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving config: {e}")
            return False
    
    def _load_state(self) -> Dict[str, Any]:
        """Load sync state."""
        if self.state_file.exists():
            try:
                with open(self.state_file, 'r') as f:
                    return json.load(f)
            except Exception:
                pass
        return {"backups": []}
    
    def _save_state(self) -> bool:
        """Save sync state."""
        try:
            with open(self.state_file, 'w') as f:
                json.dump(self.state, f, indent=2)
            return True
        except Exception:
            return False
    
    def _calculate_checksum(self, file_path: Path) -> str:
        """Calculate MD5 checksum of a file."""
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    def _get_data_files(self) -> Dict[str, Path]:
        """Get all data files to backup."""
        files = {}
        
        # Core data files
        for name in ["profile", "history", "config", "user_profile"]:
            path = self.data_dir / f"{name}.json"
            if path.exists():
                files[name] = path
        
        return files
    
    def get_tier(self) -> SubscriptionTier:
        """Get current subscription tier."""
        tier_str = self.config.tier.lower()
        try:
            return SubscriptionTier(tier_str)
        except ValueError:
            return SubscriptionTier.FREE
    
    def set_tier(self, tier: str) -> bool:
        """Set subscription tier."""
        try:
            SubscriptionTier(tier.lower())
            self.config.tier = tier.lower()
            return self._save_config()
        except ValueError:
            return False
    
    def can_use_cloud(self) -> bool:
        """Check if user can use cloud features."""
        tier = self.get_tier()
        return tier in [SubscriptionTier.PREMIUM, SubscriptionTier.ENTERPRISE]
    
    def create_backup(self, name: Optional[str] = None) -> Optional[str]:
        """
        Create a local backup of all data.
        
        Args:
            name: Optional name for the backup
            
        Returns:
            Path to backup file or None on failure
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_name = name or f"pocketmind_backup_{timestamp}"
        
        # Create backup archive
        backup_path = self.backup_dir / f"{backup_name}.tar.gz"
        
        try:
            with tarfile.open(backup_path, "w:gz") as tar:
                # Add each data file
                for name, path in self._get_data_files().items():
                    tar.add(path, arcname=f"{name}.json")
                
                # Add manifest
                manifest = BackupManifest(
                    created_at=datetime.now().isoformat(),
                    device_id=self._get_device_id(),
                    profile=self._load_json("profile"),
                    history=self._load_json("history"),
                    config=self._load_json("config"),
                )
                
                # Calculate checksums
                for name, path in self._get_data_files().items():
                    manifest.checksums[name] = self._calculate_checksum(path)
                
                # Write manifest
                manifest_path = self.backup_dir / f"{backup_name}_manifest.json"
                with open(manifest_path, 'w') as f:
                    json.dump(asdict(manifest), f, indent=2)
                tar.add(manifest_path, arcname="manifest.json")
                manifest_path.unlink()
            
            # Update state
            self.state["backups"].append({
                "name": backup_name,
                "path": str(backup_path),
                "created": datetime.now().isoformat(),
                "size": os.path.getsize(backup_path)
            })
            self.config.last_sync = datetime.now().isoformat()
            self.config.backup_count += 1
            self._save_state()
            self._save_config()
            
            print(f"✅ Backup created: {backup_path}")
            return str(backup_path)
            
        except Exception as e:
            print(f"❌ Backup failed: {e}")
            return None
    
    def _load_json(self, name: str) -> Optional[Dict]:
        """Load a JSON file from data directory."""
        path = self.data_dir / f"{name}.json"
        if path.exists():
            try:
                with open(path, 'r') as f:
                    return json.load(f)
            except Exception:
                pass
        return None
    
    def _get_device_id(self) -> str:
        """Get a unique device identifier."""
        # Use a simple hash of the data directory path
        return hashlib.md5(str(self.data_dir).encode()).hexdigest()[:8]
    
    def list_backups(self) -> List[Dict[str, Any]]:
        """List all available backups."""
        seen_names = set()
        backups = []
        
        # From state
        for backup in self.state.get("backups", []):
            name = backup.get("name", "")
            if name and name not in seen_names:
                backups.append(backup)
                seen_names.add(name)
        
        # Also scan backup directory (only .tar.gz files)
        for path in self.backup_dir.glob("*.tar.gz"):
            # Get the base name without .tar.gz extension
            name = path.name[:-7]  # Remove .tar.gz
            # Check if already in state
            if name not in seen_names:
                backups.append({
                    "name": name,
                    "path": str(path),
                    "created": datetime.fromtimestamp(path.stat().st_mtime).isoformat(),
                    "size": path.stat().st_size
                })
                seen_names.add(name)
        
        return sorted(backups, key=lambda x: x.get("created", ""), reverse=True)
    
    def restore_backup(self, name: Optional[str] = None, latest: bool = True) -> bool:
        """
        Restore from a backup.
        
        Args:
            name: Specific backup name to restore
            latest: If True and no name given, restore most recent
            
        Returns:
            True if successful
        """
        # Find backup to restore
        backup_path = None
        
        if name:
            backup_path = self.backup_dir / f"{name}.tar.gz"
            if not backup_path.exists():
                # Try with full path
                backup_path = Path(name)
        elif latest:
            backups = self.list_backups()
            if backups:
                backup_path = Path(backups[0]["path"])
        
        if not backup_path or not backup_path.exists():
            print(f"❌ Backup not found: {name or 'latest'}")
            return False
        
        try:
            # Create restore point first
            print("📦 Creating restore point...")
            self.create_backup(name="restore_point_pre_restore")
            
            # Extract backup
            print(f"🔄 Restoring from: {backup_path.name}")
            
            with tarfile.open(backup_path, "r:gz") as tar:
                # Extract to temp directory first
                with tempfile.TemporaryDirectory() as tmpdir:
                    tar.extractall(tmpdir)
                    
                    # Copy files to data directory
                    for filename in os.listdir(tmpdir):
                        if filename.endswith(".json"):
                            src = Path(tmpdir) / filename
                            dst = self.data_dir / filename
                            shutil.copy2(src, dst)
                            print(f"   ✓ Restored: {filename}")
            
            print("✅ Restore complete!")
            return True
            
        except Exception as e:
            print(f"❌ Restore failed: {e}")
            return False
    
    def verify_backup(self, name: str) -> Dict[str, Any]:
        """
        Verify integrity of a backup.
        
        Args:
            name: Backup name
            
        Returns:
            Dict with verification results
        """
        backup_path = self.backup_dir / f"{name}.tar.gz"
        
        if not backup_path.exists():
            return {"valid": False, "error": "Backup not found"}
        
        try:
            # Extract and verify checksums
            with tempfile.TemporaryDirectory() as tmpdir:
                with tarfile.open(backup_path, "r:gz") as tar:
                    tar.extractall(tmpdir)
                
                manifest_path = Path(tmpdir) / "manifest.json"
                if not manifest_path.exists():
                    return {"valid": False, "error": "No manifest found"}
                
                with open(manifest_path, 'r') as f:
                    manifest_data = json.load(f)
                
                checksums = manifest_data.get("checksums", {})
                
                # Verify each file
                results = {}
                all_valid = True
                
                for filename, expected_checksum in checksums.items():
                    file_path = Path(tmpdir) / f"{filename}.json"  # Add .json extension
                    if file_path.exists():
                        actual = self._calculate_checksum(file_path)
                        valid = actual == expected_checksum
                        results[filename] = {
                            "valid": valid,
                            "expected": expected_checksum,
                            "actual": actual
                        }
                        if not valid:
                            all_valid = False
                    else:
                        results[filename] = {"valid": False, "error": "File missing"}
                        all_valid = False
                
                return {
                    "valid": all_valid,
                    "created": manifest_data.get("created_at"),
                    "files": results
                }
                
        except Exception as e:
            return {"valid": False, "error": str(e)}
    
    def delete_backup(self, name: str) -> bool:
        """Delete a backup."""
        backup_path = self.backup_dir / f"{name}.tar.gz"
        
        if not backup_path.exists():
            print(f"❌ Backup not found: {name}")
            return False
        
        try:
            backup_path.unlink()
            
            # Remove from state
            self.state["backups"] = [
                b for b in self.state.get("backups", []) 
                if b.get("name") != name
            ]
            self._save_state()
            
            print(f"✅ Deleted: {name}")
            return True
        except Exception as e:
            print(f"❌ Delete failed: {e}")
            return False
    
    def get_status(self) -> Dict[str, Any]:
        """Get sync status."""
        backups = self.list_backups()
        
        return {
            "enabled": self.config.enabled,
            "tier": self.config.tier,
            "provider": self.config.provider,
            "can_cloud_sync": self.can_use_cloud(),
            "last_sync": self.config.last_sync,
            "backup_count": len(backups),
            "data_dir": str(self.data_dir),
            "storage_used": sum(b.get("size", 0) for b in backups)
        }
    
    def configure_google_drive(self, credentials_path: str, folder_id: Optional[str] = None) -> bool:
        """Configure Google Drive sync (premium feature)."""
        if not self.can_use_cloud():
            print("❌ Cloud sync requires a premium subscription")
            return False
        
        if not Path(credentials_path).exists():
            print(f"❌ Credentials file not found: {credentials_path}")
            return False
        
        self.config.provider = "google_drive"
        self.config.credentials_path = credentials_path
        self.config.folder_id = folder_id
        self.config.enabled = True
        
        return self._save_config()
    
    def sync_to_cloud(self) -> bool:
        """
        Sync backup to cloud (premium feature).
        
        For Google Drive, uses pydrive or google-api-python-client.
        For generic storage, supports S3-compatible APIs.
        """
        if not self.can_use_cloud():
            print("❌ Cloud sync requires a premium subscription")
            return False
        
        if self.config.provider == "google_drive":
            return self._sync_google_drive()
        elif self.config.provider == "generic":
            return self._sync_generic()
        else:
            print("❌ No cloud provider configured")
            print("   Run: python main.py --configure-cloud")
            return False
    
    def _sync_google_drive(self) -> bool:
        """Sync to Google Drive."""
        try:
            # Try to import Google Drive API
            from pydrive.auth import GoogleAuth
            from pydrive.drive import GoogleDrive
            
            # Load credentials
            gauth = GoogleAuth(self.config.credentials_path)
            gauth.LoadCredentialsFile(self.config.credentials_path)
            
            if gauth.credentials is None:
                gauth.LocalWebserverAuth()
            else:
                gauth.Refresh()
            
            drive = GoogleDrive(gauth)
            
            # Create backup first
            backup_path = self.create_backup()
            if not backup_path:
                return False
            
            # Upload to Drive
            backup_file = drive.CreateFile({
                "title": Path(backup_path).name,
                "parents": [{"id": self.config.folder_id}] if self.config.folder_id else []
            })
            backup_file.SetContentFile(backup_path)
            backup_file.Upload()
            
            print(f"✅ Synced to Google Drive: {backup_file['title']}")
            return True
            
        except ImportError:
            print("❌ Google Drive sync requires: pip install pydrive2")
            return False
        except Exception as e:
            print(f"❌ Google Drive sync failed: {e}")
            return False
    
    def _sync_generic(self) -> bool:
        """Sync to generic S3-compatible storage."""
        try:
            import boto3
            
            if not self.config.storage_url or not self.config.storage_key:
                print("❌ Storage not configured. Run: python main.py --configure-cloud")
                return False
            
            # Parse S3 endpoint
            s3_client = boto3.client(
                's3',
                endpoint_url=self.config.storage_url,
                aws_access_key_id=self.config.storage_key,
                # You'd add secret key and region here
            )
            
            # Create and upload backup
            backup_path = self.create_backup()
            if not backup_path:
                return False
            
            # Upload
            bucket = "pocketmind-backups"  # Configure this
            s3_client.upload_file(backup_path, bucket, Path(backup_path).name)
            
            print(f"✅ Synced to cloud storage: {Path(backup_path).name}")
            return True
            
        except ImportError:
            print("❌ Generic sync requires: pip install boto3")
            return False
        except Exception as e:
            print(f"❌ Cloud sync failed: {e}")
            return False


def create_sync_instance() -> CloudSync:
    """Create a CloudSync instance."""
    return CloudSync()
