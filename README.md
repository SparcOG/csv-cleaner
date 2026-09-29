# CSV Cleaner

A small Python tool that removes fully empty rows and exact duplicate rows from a CSV file.

## Features

- Keeps the header row
- Removes fully empty rows
- Removes exact duplicate rows
- Creates a cleaned CSV file
- Prints a short summary

## Requirements

- Python 3

## How to run

1. Open Terminal in the project folder.
2. Run:

   ```bash
   python3 clean_csv.py
   ```

3. The script reads `sample_input.csv`.
4. The script creates `cleaned.csv`.

## Example output

```text
Input rows: 6
Removed empty rows: 2
Removed duplicate rows: 1
Saved rows: 3
Output file: cleaned.csv
```

## Current limits

- Works with CSV files only
- Does not modify dates or cell values
- Removes only exact duplicate rows
- Uses the fixed input file name `sample_input.csv`

## Project status

Version 1 complete.