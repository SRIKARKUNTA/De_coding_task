import pytest
import pandas as pd
from io import StringIO

from csv_processor.clean import clean_data

@pytest.fixture
def sample_csv():
    data = """
purchased_date,item_price,item_promo_discount
2023-01-01,100.0,10.0
,, 
2023-01-01,100.0,10.0
2023-02-01,200.0,20.0
invalid_date,150.0,15.0
2023-03-01,invalid,25.0
2023-03-01,300.0,invalid
"""
    return StringIO(data)

def test_clean_data(tmp_path, monkeypatch, sample_csv):
    file_path = tmp_path / "test.csv"
    with open(file_path, 'w') as f:
        f.write(sample_csv.getvalue())

    df, stats = clean_data(str(file_path))

    assert stats['total_rows'] == 7
    #assert stats['total_empty_rows_removed'] == 1
    assert stats['total_invalid_rows_discarded'] == 3  # 1 invalid date + 2 invalid numeric
    assert stats['total_duplicate_rows_removed'] == 1
    assert stats['total_usable_rows'] == 2
    assert len(df) == 2