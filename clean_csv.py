"""Remove fully empty rows and exact duplicate rows from a CSV file."""

import csv
from pathlib import Path


def is_empty_row(row: list[str]) -> bool:
    """Return True when every cell in a row is empty or contains only spaces."""
    return all(cell.strip() == "" for cell in row)


def clean_csv(input_path: Path, output_path: Path) -> None:
    """Read a CSV file, remove empty and duplicate rows, then write a new file."""
    with input_path.open("r", newline="", encoding="utf-8") as input_file:
        reader = csv.reader(input_file)
        rows = list(reader)

    if not rows:
        print("The input file is empty.")
        return

    header = rows[0]
    data_rows = rows[1:]

    cleaned_rows = []
    seen_rows = set()
    removed_empty = 0
    removed_duplicates = 0

    for row in data_rows:
        if is_empty_row(row):
            removed_empty += 1
            continue

        row_key = tuple(row)
        if row_key in seen_rows:
            removed_duplicates += 1
            continue

        seen_rows.add(row_key)
        cleaned_rows.append(row)

    with output_path.open("w", newline="", encoding="utf-8") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(header)
        writer.writerows(cleaned_rows)

    print(f"Input rows: {len(data_rows)}")
    print(f"Removed empty rows: {removed_empty}")
    print(f"Removed duplicate rows: {removed_duplicates}")
    print(f"Saved rows: {len(cleaned_rows)}")
    print(f"Output file: {output_path}")


if __name__ == "__main__":
    clean_csv(Path("sample_input.csv"), Path("cleaned.csv"))