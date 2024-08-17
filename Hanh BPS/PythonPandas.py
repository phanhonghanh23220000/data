import pandas as pd

customer_df = pd.read_csv('Customer.csv')
product_df = pd.read_csv('Product.csv')
store_df = pd.read_csv('Store.csv')
state_df = pd.read_csv('State.csv')
sell_df = pd.read_csv('Sell.csv')
revenue_df = pd.read_csv('Revenue.csv')

# Check data types and structure
print(customer_df.info())
print(product_df.info())
print(store_df.info())
print(state_df.info())
print(sell_df.info())
print(revenue_df.info())

# Display the first five rows of each DataFrame

print(customer_df.head())
print(product_df.head())
print(store_df.head())
print(state_df.head())
print(sell_df.head())
print(revenue_df.head())


#save data
customer_df.to_csv('Cleaned_Customer.csv', index=False)
product_df.to_csv('Cleaned_Product.csv', index=False)
store_df.to_csv('Cleaned_Store.csv', index=False)
state_df.to_csv('Cleaned_State.csv', index=False)
sell_df.to_csv('Cleaned_Sell.csv', index=False)
revenue_df.to_csv('Cleaned_Revenue.csv', index=False)