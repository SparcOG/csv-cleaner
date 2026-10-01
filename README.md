# CSV Cleaner

A small Python tool for cleaning CSV files.

## What is CSV?

CSV is a table stored as text.

- The first row contains column names.
- Each following row contains one record.
- Commas separate columns.
- An empty row contains no data.
- Duplicate rows contain the same values.
- Dates may be written in different formats.

For example, this project uses:

```text
name,email,signup_date,city
Anna,anna@example.com,2026-09-01,Minsk
Ivan,ivan@example.com,01/09/2026,Minsk
Anna,anna@example.com,2026-09-01,Minsk

Olga,olga@example.com,2026/09/03,Grodno
Sergey,sergey@example.com,2026-09-04,Brest
Ivan,ivan@example.com,01/09/2026,Minsk
```

## Project goal

The script will create a new cleaned file and keep the original file unchanged:

```text
customers.csv → cleaned.csv
```

The final result should:

1. Keep the original `customers.csv` unchanged.
2. Remove empty rows.
3. Remove complete duplicate rows.
4. Convert dates to `YYYY-MM-DD`.
5. Save the result as a separate `cleaned.csv` file.

## Project structure

```text
sample_data/
└── customers.csv
```

## Requirements

- Python 3

## Project status

The project is being developed step by step.