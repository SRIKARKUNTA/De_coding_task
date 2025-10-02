import pandas as pd

def clean_data(file_path: str) -> tuple[pd.DataFrame, dict]:
    """
    Load CSV, remove empty rows, duplicates, invalid date rows, and invalid numeric rows, log discarded rows, and compute stats.
    """
    df = pd.read_csv(file_path, low_memory=False)

    total_rows = len(df)

    # Remove fully empty rows
    empty_rows = df[df.isnull().all(axis=1)]
    total_empty = len(empty_rows)
    df = df.dropna(how='all')

    # Remove exact duplicates
    duplicates = df[df.duplicated(keep=False)]
    total_duplicates = len(df) - len(df.drop_duplicates())
    df = df.drop_duplicates()

    # Check for invalid dates in purchased_date
    invalid_dates = df[df['purchased_date'].notna() & pd.to_datetime(df['purchased_date'], format='mixed', errors='coerce').isna()]
    df = df[df['purchased_date'].notna() & pd.to_datetime(df['purchased_date'], format='mixed', errors='coerce').notna()]

    # Convert item_price and item_promo_discount to numeric, identify invalid values
    df['item_price'] = pd.to_numeric(df['item_price'], errors='coerce')
    df['item_promo_discount'] = pd.to_numeric(df['item_promo_discount'], errors='coerce')

    # Identify rows with invalid (NaN) prices or discounts
    invalid_prices = df[df['item_price'].isna() | df['item_promo_discount'].isna()]
    total_invalid = len(invalid_dates) + len(invalid_prices)

    # Keep only rows with valid prices and discounts
    df = df[df['item_price'].notna() & df['item_promo_discount'].notna()]

    total_usable = len(df)

    # Log discarded (empty + duplicates + invalid dates + invalid prices/discounts)
    discarded = pd.concat([empty_rows, duplicates, invalid_dates, invalid_prices]).drop_duplicates()
    discarded.to_csv('discarded_rows.csv', index=False)

    stats = {
        "total_rows": total_rows,
        "total_empty_rows_removed": total_empty,
        "total_invalid_rows_discarded": total_invalid,
        "total_duplicate_rows_removed": total_duplicates,
        "total_usable_rows": total_usable
    }

    return df, stats