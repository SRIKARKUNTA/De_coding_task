# CSV Processor

This project downloads a CSV file from a provided URL, saves it with a timestamp, cleans the data by removing duplicates and empty rows, logs discarded rows, and produces a JSON stats file and a monthly metrics CSV.

Assumptions:
- The CSV has columns: 'order_date' (in YYYY-MM-DD format), 'item_price' (float), 'item_promo_discount' (float).
- System has sufficient memory to load the ~1GB file into Pandas (e.g., 16GB+ RAM recommended). 
- No additional invalid row checks beyond empty and duplicates, also removed invalid dates format. so "total_invalid_rows_discarded" is always 0.

## Setup

1. Install Poetry: `pip install poetry`
2. Install dependencies: `poetry install`

## How to Run

Run via CLI with the URL argument:

`poetry run python src/main.py --url https://storage.googleapis.com/nozzle-csv-exports/testing-data/order_items_data_2_.csv`

Outputs:
- Downloaded file: `order_items_<timestamp>.csv`
- `discarded_rows.csv`
- `processing_stats.json`
- `monthly_metrics.csv`

All outputs are in the current working directory.

## How to Execute Tests

`poetry run pytest`

Tests cover basic cleaning functionality using a sample in-memory DataFrame.

