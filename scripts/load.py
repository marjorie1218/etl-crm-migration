import sqlite3
from transform import transform

OUTPUT_DB = "data/target/clients.db"

def load(df):
    conn = sqlite3.connect(OUTPUT_DB)
    cursor = conn.cursor()

    inserted = 0
    skipped = 0

    for _, row in df.iterrows():
        try:
            cursor.execute(
                "INSERT INTO clients (name, email, phone, signup_date) VALUES (?, ?, ?, ?)",
                (row["name"], row["email"], row["phone"], row["signup_date"])
            )
            inserted += 1
        except sqlite3.IntegrityError:
            skipped += 1

    conn.commit()
    conn.close()

    print(f"Inserted {inserted} rows, skipped {skipped} rows (already existed)")

if __name__ == "__main__":
    df = transform()
    load(df)