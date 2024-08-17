import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from statsmodels.tsa.holtwinters import ExponentialSmoothing

customer_df = pd.read_csv('Cleaned_Customer.csv')
product_df = pd.read_csv('Cleaned_Product.csv')
store_df = pd.read_csv('Cleaned_Store.csv')
state_df = pd.read_csv('Cleaned_State.csv')
sell_df = pd.read_csv('Cleaned_Sell.csv')
revenue_df = pd.read_csv('Cleaned_Revenue.csv')

# Print columns to verify
print("Historical Data Columns:", sell_df.columns)

# Rename column 'Sale Date' to 'Date' if needed
if 'Date' in sell_df.columns:
    sell_df.rename(columns={'Date': 'Date'}, inplace=True)

# Print updated columns to verify
print("Updated Historical Sales Data Columns:", sell_df.columns)

# Convert 'Date' column to datetime
if 'Date' in sell_df.columns:
    sell_df['Date'] = pd.to_datetime(sell_df['Date'], errors='coerce')
    # Drop rows with invalid dates if any
    sell_df.dropna(subset=['Date'], inplace=True)   
    # Set 'Date' as index
    sell_df.set_index('Date', inplace=True)   
    # Verify the data after setting index
    print("Data After Setting Index:", sell_df.head())
else:
    print("Column 'Date' not found in historical sales data")
    
# Sample predicted sales data for demonstration
predicted_sales_data = {
    'Date': ['2024-07-08', '2024-07-09', '2024-07-10', '2024-07-11', '2024-07-12'],
    'Predicted_Sales': [1900, 2000, 2100, 2200, 2300]
}
predicted_sales = pd.DataFrame(predicted_sales_data)
predicted_sales['Date'] = pd.to_datetime(predicted_sales['Date'], errors='coerce')
predicted_sales.set_index('Date', inplace=True)

# Print columns to verify
print("Predicted Sales Data Columns:", predicted_sales.columns)
print("Predicted Sales Data Preview:", predicted_sales.head())

# Plot historical and predicted sales
if 'Date' in sell_df.index.names and 'Date' in predicted_sales.index.names:
    plt.figure(figsize=(12, 6))
    plt.plot(sell_df.index, sell_df['Revenue'], label='Historical Sales', color='blue')
    plt.plot(predicted_sales.index, predicted_sales['Predicted_Sales'], label='Predicted Sales', color='red', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.title('Sales Forecasting')
    plt.legend()
    plt.grid(True)
    plt.show()
else:
    print("Cannot plot data: Missing 'Date' column in one or both datasets")
    
    
