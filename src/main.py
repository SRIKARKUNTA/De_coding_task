import argparse
from datetime import datetime

from csv_processor.download import download_csv
from csv_processor.clean import clean_data
from csv_processor.stats import write_stats
from csv_processor.metrics import compute_monthly_metrics

def main() -> None:
    parser = argparse.ArgumentParser(description="Download and process order items CSV")
    parser.add_argument('--url', required=True, help="URL of the CSV file")
    args = parser.parse_args()

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    local_file = f"order_items_{timestamp}.csv"

    download_csv(args.url, local_file)
    df, stats = clean_data(local_file)
    write_stats(stats)
    compute_monthly_metrics(df)

if __name__ == '__main__':
    main()