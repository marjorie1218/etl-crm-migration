import sqlite3
import os

OUTPUT_DB = "data/target/clients.db"

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT,
    signup_date TEXT NOT NULL
);
"""

def main():
    os.makedirs(os.path.dirname(OUTPUT_DB), exist_ok=True)

    conn = sqlite3.connect(OUTPUT_DB)
    cursor = conn.cursor()

    cursor.execute(CREATE_TABLE_SQL)

    conn.commit()
    conn.close()

    print(f"Schema created -> {OUTPUT_DB}")

if __name__ == "__main__":
    main()