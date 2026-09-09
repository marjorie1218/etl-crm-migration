import pandas as pd
from extract import extract

def clean_names(df):
    df["name"] = df["name"].str.strip()
    df["name"] = df["name"].str.title()
    return df

def transform():
    df = extract()
    df = clean_names(df)

    print(f"Names cleaned. Example:\n{df['name'].head(5)}")

    return df

if __name__ == "__main__":
    transform()