import csv
import os
from datetime import datetime


def parse_date(date_str):
    """Convert a date to YYYY-MM-DD."""
    date_formats = [
        "%Y-%m-%d",
        "%d/%m/%Y",
        "%Y/%m/%d",
    ]

    date_str = date_str.strip()

    for date_format in date_formats:
        try:
            parsed_date = datetime.strptime(date_str, date_format)
            return parsed_date.strftime("%Y-%m-%d")
        except ValueError:
            continue

    return date_str


def clean_csv(input_path, output_path):
    """Clean a CSV file and save the result to a new file."""
    if not os.path.exists(input_path):
        print(f"Error: file not found: {input_path}")
        return

    unique_rows = set()
    cleaned_rows = []

    with open(
        input_path,
        mode="r",
        encoding="utf-8",
        newline=""
    ) as input_file:
        reader = csv.reader(input_file)

        try:
            header = next(reader)
        except StopIteration:
            print("Error: input file is empty.")
            return

        for row in reader:
            if not row or all(cell.strip() == "" for cell in row):
                continue

            row = [cell.strip() for cell in row]

            if len(row) > 2:
                row[2] = parse_date(row[2])

            row_tuple = tuple(row)

            if row_tuple not in unique_rows:
                unique_rows.add(row_tuple)
                cleaned_rows.append(row)

    with open(
        output_path,
        mode="w",
        encoding="utf-8",
        newline=""
    ) as output_file:
        writer = csv.writer(output_file)
        writer.writerow(header)
        writer.writerows(cleaned_rows)

    print(f"Cleaning completed. Output saved to: {output_path}")


if __name__ == "__main__":
    input_file = os.path.join("sample_data", "customers.csv")
    output_file = "cleaned.csv"

    clean_csv(input_file, output_file)