import pandas as pd

import pandas as pd

def clean_data(input_file_path, output_file_path):
    """"
    Reads a raw weather data CSV file, cleans common formatting issues,
    and saves the structured result to a new CSV file.
    """
    print(f"Reading raw data from: {input_file_path}")
    
    # 1. Load the data into a Pandas DataFrame
    df = pd.read_csv(input_file_path)
    
    # 2. Handle Duplicate Records
    # Removes any completely identical rows introduced by API scraping or log bugs
    initial_rows = len(df)
    df = df.drop_duplicates()
    print(f"Removed {initial_rows - len(df)} duplicate records.")
    
    # 3. Standardize Data Formats (Dates)
    # Ensures all date strings are converted into a standardized YYYY-MM-DD datetime format
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')
    elif 'dt' in df.columns:
        df['date'] = pd.to_datetime(df['dt'], unit='s').dt.strftime('%Y-%m-%d') # Handles Unix timestamps common in APIs
        
    # 4. Handle Missing / Null Values
    # Based on slide instructions: choose a logical replacement strategy for down-stream math.
    # For numeric columns (temp, humidity, UV index), we fill missing gaps with the column mean.
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    for col in numeric_cols:
        if df[col].isnull().any():
            column_mean = df[col].mean()
            df[col] = df[col].fillna(column_mean)
            
    # For categorical/string columns, we fill with a placeholder string
    string_cols = df.select_dtypes(include=['object']).columns
    for col in string_cols:
        if col != 'date': # Skip our clean date column
            df[col] = df[col].fillna('Unknown/Missing')

    # 5. Enforce Proper Data Types
    # Ensures flags or indices are explicitly cast to numeric/boolean types for later analysis
    if 'max_uv_index' in df.columns:
        df['max_uv_index'] = df['max_uv_index'].astype(float)
    if 'humidity_pct' in df.columns:
        df['humidity_pct'] = df['humidity_pct'].astype(int)

    # 6. Save the cleaned, flat DataFrame to the output path
    # index=False avoids writing an extra automated row-index column to your final file
    df.to_csv(output_file_path, index=False)
    print(f"Cleaned data successfully saved to: {output_file_path}\n")


def main():
    # Define your pipeline file paths
    # (Adjust these filenames to match whatever you named your fetched dataset)
    input_file = "raw_weather_data.csv"
    output_file = "clean_weather_data.csv"
    
    # Execute the cleaning routine
    clean_data(input_file, output_file)

if __name__ == "__main__":
    main()
    # TODO: implement cleaning logic
    print("Cleaning data... (not implemented yet)")
    
