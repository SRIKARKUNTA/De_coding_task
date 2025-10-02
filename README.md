# CSV Processor

A Python-based project  downloads a CSV file from a provided URL, saves it with a timestamp, cleans the data by removing duplicates and empty rows, logs discarded rows, and produces a JSON stats file and a monthly metrics CSV.

📌 Assumptions
- Input CSV has columns:
  - `order_date` (in `YYYY-MM-DD` format)
  - `item_price` (float)
  - `item_promo_discount` (float)  
- System has enough memory to load a ~1GB CSV into Pandas (16GB+ RAM recommended).  
- No extra invalid row checks beyond:
  - Empty rows
  - Duplicates
  - Invalid date formats (discarded)
- Therefore, `"total_invalid_rows_discarded"` in stats is always `0`.  


## Setup

1. Install Poetry: `pip install poetry`
2. Install dependencies: `poetry install`

**##📂 Project Structure**
csv-processor/
├── src/
│   ├── main.py                 # CLI entrypoint
│   └── csv_processor/
│       ├── clean.py            # Data cleaning logic
│       ├── download.py         # Streaming CSV download
│       ├── metrics.py          # Monthly aggregation calculations
│       └── stats.py            # Processing statistics (JSON output)
│
├── tests/
│   ├── __init__.py
│   └── test_clean.py           # Unit tests for cleaning module
│
├── pyproject.toml              # Poetry dependencies & build config
├── README.md                   # Project documentation
└── .gitignore                  # Ignore large outputs and build artifacts

## How to Run

Run via CLI with the URL argument:

`poetry run python src/main.py --url https://storage.googleapis.com/nozzle-csv-exports/testing-data/order_items_data_2_.csv`


Outputs:
When you run the pipeline, the following files are generated in the working directory:

**order_items_<timestamp>.csv** → raw downloaded file

**discarded_rows.csv** → rows removed during cleaning

**processing_stats.json** → summary of processing (rows kept, discarded, invalid)

**monthly_metrics.csv** → monthly aggregated metrics

⚠️Note: These files are listed in .gitignore, so they won’t appear in the GitHub repo, but they will be created locally every time you run the program.

## How to Execute Tests

`poetry run pytest`

Tests cover basic cleaning functionality using a sample in-memory DataFrame.

