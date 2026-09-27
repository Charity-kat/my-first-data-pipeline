import sqlite3
import pandas as pd

def load_crypto_data():
    print("📥 Starting data loading into SQLite database...")
    
    clean_path = "data/clean_crypto_prices.csv"
    db_path = "data/crypto_pipeline.db"
    
    try:
        # 1. Read the clean transformed CSV
        df = pd.read_csv(clean_path)
        
        # 2. Connect to SQLite database (creates the file if it doesn't exist)
        conn = sqlite3.connect(db_path)
        
        # 3. Write data into a table named 'crypto_prices' (appends if already present)
        df.to_sql("crypto_prices", conn, if_exists="append", index=False)
        
        # 4. Verify insertion by querying the database table
        df_db = pd.read_sql("SELECT * FROM crypto_prices", conn)
        conn.close()
        
        print(f"✅ Data loaded into database table 'crypto_prices' at: {db_path}\n")
        print("--- DATABASE TABLE CONTENTS ---")
        print(df_db)
        
    except Exception as e:
        print(f"❌ Loading failed: {e}")

if __name__ == "__main__":
    load_crypto_data()