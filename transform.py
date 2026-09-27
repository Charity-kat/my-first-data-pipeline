import pandas as pd
from datetime import datetime

def transform_crypto_data():
    print("🔄 Starting data transformation...")
    
    raw_path = "data/raw_crypto_prices.csv"
    
    try:
        # 1. Read raw CSV
        df = pd.read_csv(raw_path)
        
        # 2. Add transformation metadata (ingestion timestamp)
        df["extracted_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 3. Calculate effective USD to ZAR exchange rate from the API figures
        df["calculated_usd_zar_rate"] = (df["price_zar"] / df["price_usd"]).round(2)
        
        # 4. Save clean output file
        clean_path = "data/clean_crypto_prices.csv"
        df.to_csv(clean_path, index=False)
        
        print(f"✅ Data transformed and saved to: {clean_path}\n")
        print(df)
        
    except Exception as e:
        print(f"❌ Transformation failed: {e}")

if __name__ == "__main__":
    transform_crypto_data()