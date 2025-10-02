import pandas as pd

def compute_monthly_metrics(df: pd.DataFrame) -> None:
    """
    Compute monthly metrics and save to CSV.
    Assumes 'purchased_date' column with valid dates and numeric 'item_price', 'item_promo_discount'.
    """
    # Check for required columns
    required_columns = ['purchased_date', 'item_price', 'item_promo_discount']
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}. Available columns: {list(df.columns)}")

    # Convert purchased_date to datetime (should be clean after clean_data)
    df['purchased_date'] = pd.to_datetime(df['purchased_date'], format='mixed', errors='raise')
    df['month_year'] = df['purchased_date'].dt.strftime('%Y-%m')

    # Ensure item_price and item_promo_discount are numeric (should be guaranteed by clean_data)
    if not pd.api.types.is_numeric_dtype(df['item_price']) or not pd.api.types.is_numeric_dtype(df['item_promo_discount']):
        raise ValueError("Non-numeric values found in item_price or item_promo_discount after cleaning")

    grouped = df.groupby('month_year').agg(
        total_items_promo_discount=('item_promo_discount', 'sum'),
        item_price_sum=('item_price', 'sum')
    ).reset_index()

    grouped['total_items_price'] = grouped['item_price_sum'] - grouped['total_items_promo_discount']
    grouped[['month_year', 'total_items_promo_discount', 'total_items_price']].to_csv('monthly_metrics.csv', index=False)