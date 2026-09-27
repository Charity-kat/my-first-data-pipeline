import time
from extract import fetch_crypto_data
from transform import transform_crypto_data
from load import load_crypto_data

def run_pipeline():
    print("=" * 50)
    print("⚙️  EXECUTION STARTED: Crypto DevSecOps Data Pipeline")
    print("=" * 50)
    
    start_time = time.time()
    
    # 1. Step 1: Extract
    fetch_crypto_data()
    print("-" * 50)
    
    # 2. Step 2: Transform
    transform_crypto_data()
    print("-" * 50)
    
    # 3. Step 3: Load
    load_crypto_data()
    print("-" * 50)
    
    elapsed_time = round(time.time() - start_time, 2)
    print(f"🎉 PIPELINE EXECUTION COMPLETED SUCCESSFULLY IN {elapsed_time} SECONDS!")
    print("=" * 50)

if __name__ == "__main__":
    run_pipeline()