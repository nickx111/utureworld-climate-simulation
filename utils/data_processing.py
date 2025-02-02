import pandas as pd
import numpy as np

def process_uploaded_data(uploaded_file):
    """Process uploaded CSV data file"""
    try:
        df = pd.read_csv(uploaded_file)
        # Basic validation and cleaning
        required_columns = ['year', 'temperature', 'sea_level', 'co2_levels']
        if not all(col in df.columns for col in required_columns):
            raise ValueError("Missing required columns in uploaded data")
        
        # Clean and normalize data
        df = df.dropna()
        df['year'] = pd.to_numeric(df['year'], errors='coerce')
        df = df.sort_values('year')
        
        return df
    except Exception as e:
        raise ValueError(f"Error processing uploaded file: {str(e)}")

def load_sample_data():
    """Generate sample climate data for demonstration"""
    years = range(2000, 2023)
    data = {
        'year': list(years),
        'temperature': [15 + np.random.normal(0.02 * i, 0.1) for i in range(len(years))],
        'sea_level': [0 + np.random.normal(0.3 * i, 0.05) for i in range(len(years))],
        'co2_levels': [370 + 2.1 * i + np.random.normal(0, 0.5) for i in range(len(years))],
        'resource_index': [100 - 0.5 * i + np.random.normal(0, 1) for i in range(len(years))]
    }
    return pd.DataFrame(data)
