import pandas as pd
import os
import logging
import transformation as tr
import load
# --- ETL Extract Function ---
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def extract_ckd_data(path: str) -> pd.DataFrame:

    logging.info(f"Attempting to extract data from: {path}")
    if not os.path.exists(path):
        logging.error(f"File not found at: {path}")
        raise FileNotFoundError(f"File not found at: {path}")
    try:
        df = pd.read_csv(path)
        logging.info(f"Successfully extracted {len(df)} rows from {path}")
        print(f"Extracted {len(df)} rows from {path}")
        return df
    except Exception as e:
        logging.error(f"Error reading CSV file at {path}: {e}")
        raise



# --- Main ETL Pipeline Execution ---
if __name__ == "__main__":
    # PATH=os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    DATA_PATH = r"D:\DE ITI\python\ckd_etl_project\data\kidney_disease_dataset.csv"
    DB_PATH = "ckd_etl_project/output/ckd.db" # This will create 'output' folder if it doesn't exist
    DB_TABLE_NAME = "patients"

    try:
        logging.info("--- ETL Pipeline Started ---")

        # 1. Extract
        df_extracted = extract_ckd_data(DATA_PATH)

        # 2. Transform
        df_transformed = tr.transformationson_ckd_data(df_extracted)

        # 3. Load
        load.load_to_sqlite(df_transformed, db_path=DB_PATH, table_name=DB_TABLE_NAME)

        #display database content
        
        load.display_db_content(DB_PATH, DB_TABLE_NAME)


        logging.info("--- ✅ ETL Pipeline Completed Successfully! ---")

    except FileNotFoundError as e:
        logging.critical(f"ETL pipeline failed: Input file not found. {e}")
    except ValueError as e:
        logging.critical(f"ETL pipeline failed: Data validation error during transformation. {e}")
    except Exception as e:
        # Catch any other unexpected errors
        logging.critical(f"An unexpected critical error occurred during ETL pipeline execution: {e}", exc_info=True)

    