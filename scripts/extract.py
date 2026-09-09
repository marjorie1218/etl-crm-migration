import pandas as pd

INPUT_FILE = "data/source/clients_legacy.csv"

def extract():
    df = pd.read_csv(INPUT_FILE)

    print(f"Extracted {len(df)} rows from {INPUT_FILE}")
    print(f"Columns: {list(df.columns)}")
    print(f"Missing emails: {df['email'].isna().sum()}")
    print(f"Missing phones: {df['phone'].isna().sum()}")

    return df

if __name__ == "__main__":
    extract()