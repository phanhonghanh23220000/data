import pandas as pd 
import matplotlib.pyplot as plt

customer_df = pd.read_csv('Cleaned_Customer.csv')
product_df = pd.read_csv('Cleaned_Product.csv')
store_df = pd.read_csv('Cleaned_Store.csv')
state_df = pd.read_csv('Cleaned_State.csv')
sell_df = pd.read_csv('Cleaned_Sell.csv')
revenue_df = pd.read_csv('Cleaned_Revenue.csv')

# Convert 'Day' to datetime in revenue_df
revenue_df['Day'] = pd.to_datetime(revenue_df['Day'])

# Group by day to sum up the revenue
revenue_by_day = revenue_df.groupby('Day')['Revenue'].sum()

# Plot the revenue over time as a line chart
plt.figure(figsize=(12, 6))
revenue_by_day.plot(kind='line', marker='o', color='b')
plt.title('Revenue Over Time')
plt.xlabel('Date')
plt.ylabel('Revenue (USD)')
plt.grid(True)
plt.show()


#=============================================================

# Group by store to sum up the revenue
revenue_by_store = revenue_df.groupby('StoreID')['Revenue'].sum()

# Plot the revenue by store as a bar chart
plt.figure(figsize=(10, 6))
revenue_by_store.plot(kind='bar', color='skyblue')
plt.title('Total Revenue by Store')
plt.xlabel('Store ID')
plt.ylabel('Total Revenue (USD)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

#====================================================================

# Merge sell_df with product_df on ProductID
merged_df = pd.merge(sell_df, product_df, on='ProductID')

# Group by product name to sum up the revenue
revenue_by_product = merged_df.groupby('ProductName')['Revenue'].sum()

# Plot the revenue by product as a bar chart
plt.figure(figsize=(12, 6))
revenue_by_product.plot(kind='bar', color='coral')
plt.title('Total Revenue by Product')
plt.xlabel('Product Name')
plt.ylabel('Total Revenue (USD)')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

#==========================================================================
# Group customer data by state
customer_by_state = customer_df.groupby('StateID').size()

# Plot the customer distribution by state as a bar chart
plt.figure(figsize=(10, 6))
customer_by_state.plot(kind='bar', color='purple')
plt.title('Customer Distribution by State')
plt.xlabel('State ID')
plt.ylabel('Number of Customers')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
