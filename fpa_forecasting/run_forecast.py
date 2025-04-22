import pandas as pd
from datetime import datetime
from tools.forecast_tools import forecast_with_seasonality

# Load the Excel file
df = pd.read_excel("data/sales_history.xlsx")

# Clean 'Sales' column: remove $ and convert (negatives)
df["Sales"] = (
    df["Sales"]
    .astype(str)
    .str.replace("[$,]", "", regex=True)
    .str.replace("(", "-", regex=False)
    .str.replace(")", "", regex=False)
    .astype(float)
)

# Parse the 'Date' column to datetime
df["Date"] = pd.to_datetime(df["Date"], format="%b-%y")

# Use all data BEFORE Nov 2024 as historicals
historical_df = df[df["Date"] >= "2024-11-01"]


# Sum by month
monthly_sales = (
    historical_df
    .groupby(df["Date"].dt.to_period("M"))["Sales"]
    .sum()
    .sort_index()
)

# Convert monthly sales to list of values
historical_data = monthly_sales.values.tolist()

# Forecast next 5 months
forecast = forecast_with_seasonality(
    historical_data,
    start_month="2025-04-01",  # first forecast month
    months_ahead=12,
    base_growth=0.02           # a modest baseline trend
)

# Generate labels for forecast months (Nov 2024 – Mar 2025)
forecast_months = pd.date_range(start="2025-04-01", periods=12, freq="MS")

# Save forecast to Excel
forecast_df = pd.DataFrame([forecast], columns=forecast_months)
forecast_df.to_excel("data/revenue_forecast_output.xlsx", index=False)

print("✅ Forecast complete! Output saved to data/revenue_forecast_output.xlsx")
