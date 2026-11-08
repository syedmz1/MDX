def check_record(record):
    """Calculate the percentage and status of a record."""
    percentage = (record["value"] / record["limit"]) * 100

    if record["value"] > record["limit"]:
        status = "OVER LIMIT"
    else:
        status = "OK"

    return percentage, status

def print_report(record):
    """Print a report for one record."""
    percentage, status = check_record(record)

    print(f"Dataset: {record['label']}")
    print(f"Rows loaded: {record['value']}")
    print(f"Rows expected: {record['limit']}")
    print(f"Completion: {percentage:.2f}%")
    print(f"Status: {status}")
    print("-" * 30)

def load_records(path):
    """Load records from a file into a list of dictionaries."""
    records = []

    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")

            record = {
                "label": label,
                "value": float(value),
                "limit": float(limit)
            }

            records.append(record)

    return records

try:
    records = load_records("records.txt")

except FileNotFoundError:
    print("records.txt not found")
    records = []

over_limit = 0

with open("results.txt", "w") as f:
    for record in records:

        percentage, status = check_record(record)

        print_report(record)

        f.write(f"{record['label']},{status}\n")

        if status == "OVER LIMIT":
            over_limit += 1

print(f"Total records: {len(records)}")
print(f"Records over limit: {over_limit}")