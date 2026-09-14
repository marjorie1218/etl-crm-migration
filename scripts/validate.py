import sqlite3
import pandas as pd
from datetime import datetime

SOURCE_FILE = "data/source/clients_legacy.csv"
TARGET_DB = "data/target/clients.db"
REPORT_FILE = "reports/migration_report.txt"

def validate():
    source_df = pd.read_csv(SOURCE_FILE)
    source_count = len(source_df)
    source_valid_emails = set(source_df["email"].dropna())

    conn = sqlite3.connect(TARGET_DB)
    target_count = conn.execute("SELECT COUNT(*) FROM clients").fetchone()[0]
    target_non_null_emails = conn.execute("SELECT COUNT(*) FROM clients WHERE email IS NOT NULL").fetchone()[0]
    target_emails = set(row[0] for row in conn.execute("SELECT email FROM clients WHERE email IS NOT NULL"))
    conn.close()

    missing_emails = source_valid_emails - target_emails
    duplicate_check = len(target_emails) == target_count
    duplicate_check = len(target_emails) == target_non_null_emails

    report_lines = [
        f"Migration Report — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        "=" * 50,
        f"Source rows: {source_count}",
        f"Target rows: {target_count}",
        f"Rows removed (duplicates): {source_count - target_count}",
        "",
        f"Source unique emails: {len(source_valid_emails)}",
        f"Target unique emails: {len(target_emails)}",
        f"Missing emails (lost data): {len(missing_emails)}",
        "",
        f"No duplicate emails in target: {duplicate_check}",
        "",
        "STATUS: PASS" if len(missing_emails) == 0 and duplicate_check else "STATUS: FAIL",
    ]

    report_text = "\n".join(report_lines)

    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(report_text)

    print(report_text)
    print(f"\nReport saved -> {REPORT_FILE}")

if __name__ == "__main__":
    validate()