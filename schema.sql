CREATE TABLE IF NOT EXISTS user (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    profile_pic TEXT NOT NULL,
    grocy_api_key TEXT,
    colruyt_email TEXT,
    colruyt_password TEXT
);