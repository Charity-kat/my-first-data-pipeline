import pandas as pd
from transform import transform_crypto_data

def test_transformation_logic():
    # 1. Create dummy raw data
    dummy_data = {
        "crypto": ["Bitcoin"],
        "price_usd": [10000.00],
        "price_zar": [180000.00]
    }
    df = pd.DataFrame(dummy_data)
    df.to_csv("data/raw_crypto_prices.csv", index=False)

    # 2. Run transformation function
    transform_crypto_data()

    # 3. Read clean result and verify expected calculation (180000 / 10000 = 18.0)
    clean_df = pd.read_csv("data/clean_crypto_prices.csv")
    
    assert "calculated_usd_zar_rate" in clean_df.columns
    assert clean_df["calculated_usd_zar_rate"].iloc[0] == 18.0
    assert "extracted_at" in clean_df.columns