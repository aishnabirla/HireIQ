import sqlite3
import bcrypt
import os

DB_PATH = "/tmp/resume_screener.db"

def initialize():
    print("Setting up database...")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password_hash TEXT NOT NULL,
        role TEXT NOT NULL DEFAULT 'hr',
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS job_descriptions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        content TEXT NOT NULL,
        uploaded_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resumes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        jd_id INTEGER NOT NULL,
        candidate_name TEXT,
        candidate_email TEXT,
        file_name TEXT NOT NULL,
        raw_text TEXT NOT NULL,
        uploaded_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (jd_id) REFERENCES job_descriptions(id)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS evaluations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        resume_id INTEGER NOT NULL,
        jd_id INTEGER NOT NULL,
        match_score REAL NOT NULL,
        matched_skills TEXT,
        missing_skills TEXT,
        education TEXT,
        experience TEXT,
        evaluated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (resume_id) REFERENCES resumes(id),
        FOREIGN KEY (jd_id) REFERENCES job_descriptions(id)
    )""")

    password = "hr@123"
    hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    cursor.execute(
        "INSERT OR IGNORE INTO users (name, email, password_hash, role) VALUES (?, ?, ?, ?)",
        ("Admin", "hr@strive4x.com", hashed.decode('utf-8'), "admin")
    )

    conn.commit()
    conn.close()
    print("Database setup complete!")

# Allow running directly too
if __name__ == "__main__":
    initialize()