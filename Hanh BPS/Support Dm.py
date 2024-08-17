import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression

customer_df = pd.read_csv('Cleaned_Customer.csv')
product_df = pd.read_csv('Cleaned_Product.csv')
store_df = pd.read_csv('Cleaned_Store.csv')
state_df = pd.read_csv('Cleaned_State.csv')
sell_df = pd.read_csv('Cleaned_Sell.csv')
revenue_df = pd.read_csv('Cleaned_Revenue.csv')


# Convert 'Sale Date' to datetime format
sell_df['Date'] = pd.to_datetime(sell_df['Date'])

# Sort the data by date
sell_df = sell_df.sort_values('Date')

# Extract features and target variable
sell_df['Date_ordinal'] = sell_df['Date'].map(pd.Timestamp.toordinal)
X = sell_df[['Date_ordinal']]
y = sell_df['Revenue']  # Ensure 'Revenue' is the correct column for the target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")


# Plot the actual revenue and predicted revenue
plt.figure(figsize=(12, 6))

# Plot actual data
plt.plot(sell_df['Date'], sell_df['Revenue'], label='Actual Revenue', color='blue')

# Plot predictions (on the test set)
plt.scatter(X_test['Date_ordinal'].map(pd.to_datetime), y_pred, color='red', label='Predicted Revenue', marker='x')

# Add labels and title
plt.title('Actual vs Predicted Revenue Over Time')
plt.xlabel('Date')
plt.ylabel('Revenue')
plt.legend()
plt.grid(True)
plt.show()

#=====================================================================================
# Extract month from the sale date
sell_df['Month'] = sell_df['Date'].dt.to_period('M')

# Group by month to sum up the revenue
revenue_by_month = sell_df.groupby('Month')['Revenue'].sum()

# Plot the revenue by month as a bar chart
plt.figure(figsize=(10, 6))
revenue_by_month.plot(kind='bar', color='orange')
plt.title('Total Revenue by Month')
plt.xlabel('Month')
plt.ylabel('Total Revenue (USD)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
