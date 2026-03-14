# PocketPal Memory System Research

**Researcher:** Jiles  
**Date:** 2026-03-11  
**Focus:** Optimal memory systems for mobile AI assistants

---

## Executive Summary

For a mobile AI assistant like PocketPal running on Android/Termux with offline-first requirements, the optimal architecture combines **SQLite + sqlite-vec** for semantic search, with GGUF-based embedding models for local inference. This provides a complete, privacy-focused, offline-capable memory system.

---

## 1. Best Local Storage Solutions for Mobile

### Recommendation: SQLite + sqlite-vec

| Database | Size | Mobile Fit | Notes |
|----------|------|------------|-------|
| **SQLite** | ~500KB | ⭐⭐⭐⭐⭐ | Built into Android, zero config, ACID compliant |
| **LMDB** | ~64KB | ⭐⭐⭐⭐ | Faster writes, memory-mapped, but no SQL interface |
| **LevelDB** | ~2MB | ⭐⭐⭐ | Google's key-value store, good for bulk storage |
| **RocksDB** | ~5MB | ⭐⭐⭐ | Facebook's embedded DB, heavy for mobile |
| **BerkeleyDB** | ~1MB+ | ⭐⭐ | Legacy, complex licensing |

### Why SQLite Wins for PocketPal
- **Zero dependencies** — Already in Android's stdlib
- **Single file** — Easy to backup/sync
- **Mature tooling** — Great Python/JavaScript support for Termux
- **Extensible** — sqlite-vec adds vector search capability

### Implementation for Termux
```bash
# Install Python and SQLite
pkg install python sqlite

# Install sqlite-vec for semantic search
pip install sqlite-vec

# For local embeddings (optional but recommended)
pip install sqlite-lembed  # Requires llama.cpp
```

---

## 2. Semantic Memory Search on Mobile

### Solution: sqlite-vec + Local Embeddings

**sqlite-vec** is a pure C SQLite extension that provides vector search (KNN) without external dependencies. It works on:
- Linux/MacOS/Windows
- Raspberry Pi
- Android/Termux (via Python)
- Browser (WASM)

### Schema Design

```sql
-- Main memories table
CREATE TABLE memories (
    id INTEGER PRIMARY KEY,
    content TEXT NOT NULL,           -- The actual memory text
    timestamp INTEGER,               -- Unix timestamp
    memory_type TEXT,                -- 'conversation', 'fact', 'preference', 'event'
    importance INTEGER DEFAULT 1,   -- 1-5 importance scale
    metadata TEXT                    -- JSON for extra data
);

-- Vector embeddings for semantic search
CREATE VIRTUAL TABLE memory_vectors USING vec0(
    embedding float[384]             -- Dimension depends on model
);

-- Index for fast timestamp queries
CREATE INDEX idx_timestamp ON memories(timestamp);
CREATE INDEX idx_memory_type ON memories(memory_type);
```

### Generating Embeddings Locally

Use **sqlite-lembed** with quantized GGUF models for on-device embedding generation:

```python
import sqlite_vec

# Load a lightweight embedding model (all-MiniLM-L6-v2, ~40MB quantized)
# Model: sentence-transformers/all-MiniLM-L6-v2 in Q8_0 quantization

def embed_text(text):
    # Returns a 384-dimensional embedding vector
    return lembed('all-MiniLM-L6-v2', text)

# Store a memory with its embedding
def add_memory(content, memory_type='conversation'):
    embedding = embed_text(content)
    cursor.execute(
        "INSERT INTO memories (content, timestamp, memory_type) VALUES (?, ?, ?)",
        (content, int(time.time()), memory_type)
    )
    memory_id = cursor.lastrowid
    cursor.execute(
        "INSERT INTO memory_vectors (rowid, embedding) VALUES (?, ?)",
        (memory_id, embedding)
    )
```

### Semantic Search Query

```python
def search_memories(query, limit=5):
    query_embedding = embed_text(query)
    cursor.execute("""
        SELECT m.*, v.distance
        FROM memories m
        JOIN (
            SELECT rowid, distance 
            FROM memory_vectors 
            WHERE embedding match ?
            ORDER BY distance
            LIMIT ?
        ) v ON m.id = v.rowid
        ORDER BY v.distance
    """, (query_embedding, limit))
    return cursor.fetchall()
```

### Lightweight Embedding Models (Mobile-Friendly)

| Model | Dimensions | Size (Q8_0) | Quality |
|-------|------------|-------------|---------|
| all-MiniLM-L6-v2 | 384 | ~40MB | Good |
| nomic-embed-text-v1.5 | 768 | ~270MB | Better |
| mxbai-embed-large-v1 | 1024 | ~400MB | Best |

**Recommendation:** Start with `all-MiniLM-L6-v2` for mobile — fast and small.

---

## 3. Memory Compression Techniques

### Tiered Memory Architecture

Implement three tiers based on importance and recency:

```
┌─────────────────────────────────────┐
│  Working Memory (In-Memory)         │  ← Last 10-20 exchanges
│  - Fast access, unlimited size      │    (dict/List in Python)
├─────────────────────────────────────┤
│  Episodic Memory (SQLite)           │  ← Last 7 days
│  - Full text + vectors              │
├─────────────────────────────────────┤
│  Long-term Memory (Compressed)      │  ← Older memories
│  - Summarized + vectors only        │
└─────────────────────────────────────┘
```

### Compression Techniques

1. **Importance-Based Pruning**
   ```python
   def compress_memory(memory_id):
       # Get original memory
       memory = get_memory(memory_id)
       
       # Summarize using local LLM or extract key facts
       summary = summarize(memory['content'])
       
       # Keep summary + original hash for verification
       update_memory(memory_id, {
           'content': summary,
           'compressed': True,
           'original_hash': hash(memory['content'])
       })
   ```

2. **Vector-Only Archival**
   - For very old memories, keep only the embedding vector + minimal metadata
   - Full text can be reconstructed on-demand from cloud backup

3. **Delta Storage**
   - Store only differences from previous memories
   - Example: "Same as yesterday + new info"

4. **Quantized Embeddings**
   - Store vectors as float16 or int8 instead of float32
   - Saves 50-75% storage with minimal quality loss

### Storage Budget Example

| Tier | Count | Size per Item | Total |
|------|-------|---------------|-------|
| Working | 20 | ~2KB | 40KB |
| Episodic | 1000 | ~2KB + 1.5KB (vector) | 3.5MB |
| Long-term | 5000 | ~500B (compressed) | 2.5MB |
| **Total** | ~6000 | | **~6MB** |

---

## 4. Best Practices for Personal AI Memory

### Memory Organization

1. **Memory Types**
   - `conversation` — Chat logs
   - `fact` — Explicitly stated facts about user
   - `preference` — User preferences and settings
   - `event` — Significant events or "remember when" moments
   - `reflection` — AI's own thoughts/analysis

2. **Metadata Schema**
   ```python
   {
       "source": "user_message",      # Where it came from
       "topics": ["food", "johannesburg # Auto-tagged
       "entities"], ": ["Pizza place"],    # Extracted entities
       "sentiment": "positive",
       "importance": 3,                # Auto-calculated or user-tagged
       "verified": False               # User can confirm facts
   }
   ```

3. **Importance Scoring**
   - Explicit user statements: +2
   - Repeated behaviors: +1 per occurrence
   - Emotional content: +1
   - Time-based decay: -0.1 per week

### Memory Retrieval Best Practices

1. **Hybrid Search** — Combine semantic (vector) + keyword (BM25) for best results
2. **Recency Weighting** — Boost recent memories in results
3. **Context Window** — Include relevant memories in LLM context
4. **Memory Limit** — Never exceed context window; use importance scoring to prioritize

### Privacy & Security

- **Local-only by default** — No cloud sync unless explicitly enabled
- **Encryption at rest** — Use SQLCipher for encrypted SQLite
- **User control** — Allow export/delete of all memories
- **No telemetry** — Don't send memory data anywhere

---

## 5. "Remember When" Functionality

### Implementation Pattern

```python
def handle_remember_when(query):
    # Parse "remember when..." patterns
    # Extract key entities, time references, topics
    
    # Example: "remember when we talked about pizza?"
    # → Search for memories about "pizza" from conversations
    
    # Search with time constraint if specified
    if "last month" in query:
        memories = search_memories(
            extract_topic(query),
            time_range=(now - 30 days, now)
        )
    else:
        memories = search_memaries(extract_topic(query))
    
    if memories:
        return format_memory_remember(memories)
    return "I don't have any memories matching that."
```

### Memory Time-Tracking

```sql
-- Track when memory was created vs what time period it describes
CREATE TABLE memories (
    -- ... other columns ...
    created_at INTEGER,      -- When we saved it
    describes_at INTEGER,    -- What time period it describes (optional)
    expires_at INTEGER       -- When to auto-delete (optional)
);
```

### Temporal Queries

```python
def search_memories_with_time(query, time_filter=None):
    embedding = embed_text(query)
    
    base_sql = """
        SELECT m.*, v.distance,
               (julianday('now') - m.created_at/86400.0) as age_days
        FROM memories m
        JOIN memory_vectors v ON m.id = v.rowid
        WHERE v.embedding match ?
    """
    
    params = [embedding]
    
    if time_filter:
        base_sql += " AND m.created_at BETWEEN ? AND ?"
        params.extend(time_filter)
    
    base_sql += " ORDER BY v.distance, m.importance DESC LIMIT 5"
    
    return cursor.execute(base_sql, params).fetchall()
```

---

## Recommended Architecture Summary

```
┌─────────────────────────────────────────────────────────────┐
│                    PocketPal Memory                         │
├─────────────────────────────────────────────────────────────┤
│  Python App (Termux)                                        │
│  ├── SQLite Database (sqlite + sqlite-vec)                 │
│  │   ├── memories table (text + metadata)                  │
│  │   └── memory_vectors (embeddings)                      │
│  │                                                         │
│  ├── Embedding Pipeline                                    │
│  │   ├── Local: sqlite-lembed + GGUF model (all-MiniLM)   │
│  │   └── Fallback: API-based (Ollama/OpenAI)              │
│  │                                                         │
│  └── Memory Manager                                        │
│       ├── Tiered storage (working/episodic/long-term)     │
│       ├── Importance-based retrieval                       │
│       └── "Remember when" processor                        │
└─────────────────────────────────────────────────────────────┘
```

### Key Dependencies

```txt
# Core
sqlalchemy          # Database ORM
sqlite-vec          # Vector search

# Optional (for local embeddings)
sqlite-lembed       # Local embedding generation
llama-cpp-python    # GGUF model inference

# Fallback APIs (when online)
openai              # OpenAI embeddings API
ollama              # Local Ollama server
```

### Next Steps for Implementation

1. **Phase 1:** Basic SQLite storage + keyword search
2. **Phase 2:** Add sqlite-vec for semantic search
3. **Phase 3:** Add local embedding generation (sqlite-lembed)
4. **Phase 4:** Implement memory compression + tiered storage
5. **Phase 5:** Add "remember when" temporal queries

---

*Research complete. Ready for implementation.*
