import pandas as pd
import logging

def transformationson_ckd_data(df: pd.DataFrame) -> pd.DataFrame:
    logging.info("Starting data transformations.")

    # Standardize column names
    df.columns = [col.lower() for col in df.columns]
    logging.debug("Converted column names to lowercase.")

    # Replace '?' with NaN
    df.replace('?', pd.NA, inplace=True)
    logging.debug("Replaced '?' with NaN values.")

    # Remove completely empty rows
    rows_before = len(df)
    df.dropna(how='all', inplace=True)
    logging.info(f"Dropped {rows_before - len(df)} completely empty rows.")

    # Convert specific columns to numeric
    numeric_cols = ['age', 'creatinine_level', 'bun', 'gfr', 'urine_output']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            logging.debug(f"Converted '{col}' to numeric.")
        else:
            logging.warning(f"Column '{col}' not found. Skipping conversion.")

    # Remove duplicates
    before = len(df)
    df.drop_duplicates(inplace=True)
    logging.info(f"Removed {before - len(df)} duplicate rows.")

    # Reset index
    df.reset_index(drop=True, inplace=True)

    # Rename columns for consistency
    df.rename(columns={
        'age': 'patient_age',
        'creatinine_level': 'creatinine',
        'bun': 'blood_urea_nitrogen',
        'gfr': 'glomerular_filtration_rate',
        'urine_output': 'urine_output_ml'
    }, inplace=True)
    logging.debug("Renamed columns for clarity.")
    

    # Check for negative values in numeric columns
    final_numeric_cols = ['patient_age', 'creatinine', 'blood_urea_nitrogen', 
                        'glomerular_filtration_rate', 'urine_output_ml']
    for col in final_numeric_cols:
        if col in df.columns and (df[col] < 0).any():
            error_msg = f"Negative values found in column: '{col}'"
            logging.error(error_msg)
            raise ValueError(error_msg)
    logging.debug("Validated for no negative values.")

    # Validate CKD_Status is binary (0 or 1)
    if 'ckd_status' in df.columns:
        unique_vals = set(df['ckd_status'].dropna().unique())
        if not unique_vals.issubset({0, 1}):
            error_msg = "CKD_Status column contains non-binary values."
            logging.error(error_msg)
            raise ValueError(error_msg)
        logging.debug("CKD_Status validated for binary values.")

    logging.info("Data transformations completed successfully.")
    return df
