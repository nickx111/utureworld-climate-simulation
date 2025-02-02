import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def run_climate_simulation(data, temp_increase, timeframe, emission_reduction):
    """
    Run climate crisis simulation based on input parameters
    """
    # Extract baseline trends
    years = data['year'].values.reshape(-1, 1)
    temps = data['temperature'].values
    
    # Fit linear model for baseline projection
    model = LinearRegression()
    model.fit(years, temps)
    
    # Generate future years
    future_years = np.arange(
        data['year'].max() + 1,
        data['year'].max() + timeframe + 1
    ).reshape(-1, 1)
    
    # Calculate projections
    temp_projection = model.predict(future_years)
    temp_projection += (temp_increase * np.arange(len(future_years)) / len(future_years))
    
    # Adjust for emission reduction
    reduction_factor = 1 - (emission_reduction / 100)
    temp_projection *= reduction_factor
    
    # Generate associated impacts
    sea_level_rise = 0.3 * temp_projection + np.random.normal(0, 0.1, len(temp_projection))
    resource_depletion = 100 - (2 * np.arange(len(future_years))) * reduction_factor
    
    # Compile results
    results = {
        'year': future_years.flatten(),
        'temperature': temp_projection,
        'sea_level': sea_level_rise,
        'resource_index': resource_depletion,
        'emission_reduction': np.full_like(temp_projection, emission_reduction)
    }
    
    return results
