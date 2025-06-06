# Script to load CERT dataset CSVs

import pandas as pd
import os

# Set data directory
DATA_DIR = os.path.join(os.path.dirname(__file__), '../data')

# Load datasets
def load_cert_data():
    datasets = {}
    files = ['logon.csv', 'device.csv', 'file.csv', 'email.csv']
    
    for f in files:
        path = os.path.join(DATA_DIR, f)
        if os.path.exists(path):
            datasets[f.replace('.csv', '')] = pd.read_csv(path)
        else:
            print(f"Warning: {f} not found in {DATA_DIR}")
    
    return datasets

# Explore the datasets
def explore_data(datasets):
    for name, df in datasets.items():
        print(f"\n=== {name.upper()} DATA ===")
        print(f"Shape: {df.shape}")
        print("Columns:", df.columns.tolist())
        print(df.head())

if __name__ == "__main__":
    datasets = load_cert_data()
    explore_data(datasets)
