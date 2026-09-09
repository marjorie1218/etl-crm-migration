import pandas as pd
from extract import extract

def clean_names(df):
    df["name"] = df["name"].str.strip()
    df["name"] = df["name"].str.title()
    return df

def clean_phones(df):
    def format_phone(phone):
        if pd.isna(phone):
            return phone
        digits = "".join(char for char in str(phone) if char.isdigit())
        if len(digits) != 10:
            return phone
        return f"({digits[:3]}) {digits[3:6]}-{digits[6:]}"

    df["phone"] = df["phone"].apply(format_phone)
    return df

def clean_dates(df):
    df["signup_date"] = pd.to_datetime(df["signup_date"], format="mixed")
    df["signup_date"] = df["signup_date"].dt.strftime("%Y-%m-%d")
    return df

def clean_duplicates(df):
    has_email = df["email"].notna()
    is_duplicate_email = df["email"].duplicated(keep="first")

    rows_to_drop = has_email & is_duplicate_email
    num_duplicates = rows_to_drop.sum()

    df = df[~rows_to_drop]

    print(f"Removed {num_duplicates} duplicate rows")
    return df

def transform():
    df = extract()
    df = clean_names(df)
    df = clean_phones(df)
    df = clean_dates(df)
    df = clean_duplicates(df)

    print(f"Names cleaned. Example:\n{df['name'].head(5)}")
    print(f"\nPhones cleaned. Example:\n{df['phone'].head(5)}")
    print(f"\nDates cleaned. Example:\n{df['signup_date'].head(5)}")
    print(f"\nFinal row count: {len(df)}")

    return df

if __name__ == "__main__":
    transform()