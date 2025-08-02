import sqlite3
import os

DB_PATH = os.path.join("models", "case_log.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    case_type TEXT,
                    case_number TEXT,
                    filing_year TEXT,
                    raw_html TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                 )''')
    conn.commit()
    conn.close()

def log_query(case_type, case_number, filing_year, raw_html):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("INSERT INTO logs (case_type, case_number, filing_year, raw_html) VALUES (?, ?, ?, ?)",
              (case_type, case_number, filing_year, raw_html))
    conn.commit()
    conn.close()