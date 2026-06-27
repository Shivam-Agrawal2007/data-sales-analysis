import pandas as pd
from logger import logger

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        logger.info("Dataset loaded successfully.")
        # print(f"Rows: {df.shape[0]}")
        # print(f"Columns: {df.shape[1]}")
        return df
    
    except FileNotFoundError:
        logger.error("Dataset not found.")
        return None