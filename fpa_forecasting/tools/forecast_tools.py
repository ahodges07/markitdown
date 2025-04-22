import pandas as pd

def forecast_with_seasonality(historical_data, start_month, months_ahead=6, base_growth=0.03):
    forecast = []
    current = historical_data[-1]
    
    seasonality_weights = {
        "Jan": 1.2, "Feb": 0.9, "Mar": 0.8, "Apr": 0.8,
        "May": 0.85, "Jun": 0.8, "Jul": 0.9, "Aug": 1.3,
        "Sep": 1.2, "Oct": 0.85, "Nov": 0.8, "Dec": 1.1
    }
    
    date = pd.to_datetime(start_month)

    for i in range(months_ahead):
        month_str = date.strftime("%b")
        seasonal_factor = seasonality_weights.get(month_str, 1)
        current *= (1 + base_growth)
        forecast_value = round(current * seasonal_factor, 2)
        forecast.append(forecast_value)
        date += pd.DateOffset(months=1)
        
    return forecast
