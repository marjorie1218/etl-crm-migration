import csv
import random
from faker import Faker

fake = Faker()
Faker.seed(42)
random.seed(42)

NUM_RECORDS = 300
OUTPUT_FILE = "data/source/clients_legacy.csv"

DATE_FORMATS = ["%Y-%m-%d", "%d/%m/%Y", "%b %d, %Y"]

def generate_messy_phone():
    digits = fake.msisdn()[:10]
    style = random.choice(["dashes", "parens", "plain"])
    if style == "dashes":
        return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
    elif style == "parens":
        return f"({digits[:3]}){digits[3:6]}{digits[6:]}"
    else:
        return digits

def generate_messy_date():
    date = fake.date_between(start_date="-5y", end_date="today")
    fmt = random.choice(DATE_FORMATS)
    return date.strftime(fmt)

def generate_messy_name():
    name = fake.name()
    style = random.choice(["normal", "upper", "lower", "spaces"])
    if style == "upper":
        return name.upper()
    elif style == "lower":
        return name.lower()
    elif style == "spaces":
        return f"  {name}  "
    else:
        return name

def generate_record():
    return {
        "name": generate_messy_name(),
        "email": fake.email() if random.random() > 0.05 else "",
        "phone": generate_messy_phone() if random.random() > 0.10 else "",
        "signup_date": generate_messy_date(),
    }

def main():
    records = []
    for _ in range(NUM_RECORDS):
        records.append(generate_record())

    num_duplicates = int(NUM_RECORDS * 0.08)
    for _ in range(num_duplicates):
        records.append(random.choice(records[:NUM_RECORDS]))

    random.shuffle(records)

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "email", "phone", "signup_date"])
        writer.writeheader()
        writer.writerows(records)

    print(f"Generated {len(records)} records ({num_duplicates} duplicates) -> {OUTPUT_FILE}")

if __name__ == "__main__":
    main()