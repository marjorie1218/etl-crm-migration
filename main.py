import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "scripts"))

from transform import transform
from load import load
from validate import validate

def main():
    print("=== ETL Pipeline: CRM Migration ===\n")

    df = transform()
    load(df)

    print("\n" + "=" * 50 + "\n")
    validate()

if __name__ == "__main__":
    main()