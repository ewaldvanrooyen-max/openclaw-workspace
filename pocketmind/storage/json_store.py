"""
PocketMind JSON Storage Module

Handles reading and writing user data to local JSON files.
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional


class JSONStore:
    """
    Simple JSON-based storage for user profile and conversation history.
    
    Files stored in ~/.pocketmind/ directory:
    - profile.json    : User profile from onboarding
    - history.json    : Conversation history
    - config.json     : App configuration
    """
    
    def __init__(self, data_dir: Optional[str] = None):
        """
        Initialize the JSON store.
        
        Args:
            data_dir: Custom data directory (default: ~/.pocketmind/)
        """
        if data_dir:
            self.data_dir = Path(data_dir)
        else:
            self.data_dir = Path.home() / ".pocketmind"
        
        # Ensure directory exists
        self.data_dir.mkdir(parents=True, exist_ok=True)
    
    def _get_path(self, name: str) -> Path:
        """Get the file path for a given store name."""
        return self.data_dir / f"{name}.json"
    
    def save(self, name: str, data: Any) -> bool:
        """
        Save data to a JSON file.
        
        Args:
            name: Store name (e.g., 'profile', 'history')
            data: Data to save (must be JSON serializable)
            
        Returns:
            True if successful
        """
        try:
            path = self._get_path(name)
            with open(path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error saving {name}: {e}")
            return False
    
    def load(self, name: str, default: Any = None) -> Any:
        """
        Load data from a JSON file.
        
        Args:
            name: Store name (e.g., 'profile', 'history')
            default: Default value if file doesn't exist
            
        Returns:
            Loaded data or default value
        """
        try:
            path = self._get_path(name)
            if not path.exists():
                return default
            
            with open(path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading {name}: {e}")
            return default
    
    def exists(self, name: str) -> bool:
        """Check if a store file exists."""
        return self._get_path(name).exists()
    
    def delete(self, name: str) -> bool:
        """Delete a store file."""
        try:
            path = self._get_path(name)
            if path.exists():
                path.unlink()
            return True
        except Exception as e:
            print(f"Error deleting {name}: {e}")
            return False
    
    def update(self, name: str, updates: Dict) -> bool:
        """
        Update specific fields in a store.
        
        Args:
            name: Store name
            updates: Dictionary of updates to merge
            
        Returns:
            True if successful
        """
        current = self.load(name, {})
        if isinstance(current, dict):
            current.update(updates)
        else:
            current = updates
        return self.save(name, current)
    
    @property
    def profile_path(self) -> Path:
        """Get path to profile file."""
        return self._get_path("profile")
    
    @property
    def history_path(self) -> Path:
        """Get path to history file."""
        return self._get_path("history")
    
    @property
    def config_path(self) -> Path:
        """Get path to config file."""
        return self._get_path("config")


class ProfileStore(JSONStore):
    """
    Specialized store for user profile data.
    """
    
    def __init__(self, data_dir: Optional[str] = None):
        super().__init__(data_dir)
    
    def save_profile(self, profile: Dict) -> bool:
        """Save user profile."""
        # Add metadata
        profile["_updated_at"] = datetime.now().isoformat()
        
        if not profile.get("_created_at"):
            profile["_created_at"] = datetime.now().isoformat()
        
        return self.save("profile", profile)
    
    def load_profile(self) -> Optional[Dict]:
        """Load user profile."""
        return self.load("profile")
    
    def has_profile(self) -> bool:
        """Check if user has completed onboarding."""
        profile = self.load_profile()
        return profile is not None and profile.get("name") is not None
    
    def update_profile(self, updates: Dict) -> bool:
        """Update specific profile fields."""
        profile = self.load_profile() or {}
        profile.update(updates)
        return self.save_profile(profile)


class HistoryStore(JSONStore):
    """
    Specialized store for conversation history.
    """
    
    def __init__(self, data_dir: Optional[str] = None, max_entries: int = 100):
        super().__init__(data_dir)
        self.max_entries = max_entries
    
    def save_history(self, messages: list) -> bool:
        """Save conversation history."""
        # Trim to max entries
        if len(messages) > self.max_entries:
            messages = messages[-self.max_entries:]
        
        return self.save("history", {
            "messages": messages,
            "_saved_at": datetime.now().isoformat()
        })
    
    def load_history(self) -> list:
        """Load conversation history."""
        data = self.load("history")
        if data and isinstance(data, dict):
            return data.get("messages", [])
        return []
    
    def add_message(self, role: str, content: str) -> bool:
        """Add a single message to history."""
        messages = self.load_history()
        messages.append({
            "role": role,
            "content": content,
            "_timestamp": datetime.now().isoformat()
        })
        return self.save_history(messages)
    
    def clear_history(self) -> bool:
        """Clear all conversation history."""
        return self.delete("history")
    
    def get_recent(self, n: int = 10) -> list:
        """Get the N most recent messages."""
        messages = self.load_history()
        return messages[-n:] if len(messages) > n else messages
