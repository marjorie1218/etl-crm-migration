import sqlite3

conn = sqlite3.connect("data/target/clients.db")
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())
print(cursor.execute("SELECT COUNT(*) FROM clients;").fetchone())
conn.close()
