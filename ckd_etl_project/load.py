import pandas as pd
import logging
import sqlite3
import os


def load_to_sqlite(df: pd.DataFrame, db_path: str = "output/ckd.db", table_name: str = "patients"):

    logging.info(f"Attempting to load data to SQLite database: '{db_path}', table: '{table_name}'")
    try:
        # Ensure the output directory exists
        db_directory = os.path.dirname(db_path)
        if db_directory and not os.path.exists(db_directory):
            os.makedirs(db_directory, exist_ok=True)
            logging.info(f"Created output directory: {db_directory}")
        # start database connection
        
        conn = sqlite3.connect(db_path)
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        conn.close()
        logging.info(f"Successfully loaded {len(df)} rows to SQLite table '{table_name}'.")
    except Exception as e:
        logging.error(f"Error loading data to SQLite database '{db_path}': {e}")
        raise # Re-raise the exception to propagate the error

def display_db_content(db_path: str, table_name: str):
    
    logging.info(f"Attempting to display content from database: '{db_path}', table: '{table_name}'")
    try:
        conn = sqlite3.connect(db_path)
        # Read the entire table into a DataFrame
        df_from_db = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
        conn.close()

        if not df_from_db.empty:
            logging.info(f"\n--- Content of '{table_name}' table in '{db_path}' ---")
            print(df_from_db.head()) # Print first 5 rows
            print(f"\nTotal rows in DB: {len(df_from_db)}")
            logging.info(f"Successfully retrieved {len(df_from_db)} rows from the database.")
        else:
            logging.warning(f"The table '{table_name}' in '{db_path}' is empty.")

    except sqlite3.Error as e:
        logging.error(f"SQLite error when trying to display DB content: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred while displaying DB content: {e}")


