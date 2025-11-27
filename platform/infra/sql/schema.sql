-- Basic schema for the EverLight archive in Cloudflare D1.
-- Feel free to extend with additional fields once more metadata is available.

CREATE TABLE IF NOT EXISTS content_assets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    path TEXT NOT NULL UNIQUE,
    release TEXT,
    title TEXT,
    type TEXT,
    checksum INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS media_assets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    path TEXT NOT NULL UNIQUE,
    size INTEGER,
    checksum INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS catalog_assets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    path TEXT NOT NULL UNIQUE,
    size INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
