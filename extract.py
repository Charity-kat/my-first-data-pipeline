import os
import requests
import pandas as pd

def fetch_crypto_data():
    print("🚀 Starting data extraction...")
    
    # 1. Fetch live Bitcoin & Ethereum prices from a free public API
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd,zar"
    
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Check if request was successful
        data = response.json()
        
        print("✅ Data successfully downloaded from API!")
        
        # 2. Transform raw JSON data into a clean Pandas DataFrame
        records = []
        for coin, prices in data.items():
            records.append({
                "crypto": coin.capitalize(),
                "price_usd": prices["usd"],
                "price_zar": prices["zar"]
            })
            
        df = pd.DataFrame(records)
        
        # 3. Create a 'data' directory if it doesn't exist and save as CSV
        os.makedirs("data", exist_ok=True)
        csv_path = "data/raw_crypto_prices.csv"
        df.to_csv(csv_path, index=False)
        
        print(f"📦 Saved raw data to: {csv_path}\n")
        print(df)
        
    except Exception as e:
        print(f"❌ Extraction failed: {e}")

if __name__ == "__main__":
    fetch_crypto_data()