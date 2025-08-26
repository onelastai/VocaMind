CREATE TABLE transcripts (
    id SERIAL PRIMARY KEY,
    call_id TEXT UNIQUE,
    text TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
