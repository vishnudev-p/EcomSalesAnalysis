import pandas as pd

# Adjust the file path according to where you've saved the unzipped files
orders = pd.read_csv(r'C:\Users\HP\Desktop\E-commerce Sales Forecasting\olist_orders_dataset.csv')
customers = pd.read_csv(r'C:\Users\HP\Desktop\E-commerce Sales Forecasting\olist_customers_dataset.csv')
geolocation = pd.read_csv(r'C:\Users\HP\Desktop\E-commerce Sales Forecasting\olist_geolocation_dataset.csv')
order_items = pd.read_csv(r'C:\Users\HP\Desktop\E-commerce Sales Forecasting\olist_order_items_dataset.csv')
order_payments = pd.read_csv(r'C:\Users\HP\Desktop\E-commerce Sales Forecasting\olist_order_payments_dataset.csv')
order_reviews = pd.read_csv(r'C:\Users\HP\Desktop\E-commerce Sales Forecasting\olist_order_reviews_dataset.csv')
products = pd.read_csv(r'C:\Users\HP\Desktop\E-commerce Sales Forecasting\olist_products_dataset.csv')
sellers = pd.read_csv(r'C:\Users\HP\Desktop\E-commerce Sales Forecasting\olist_sellers_dataset.csv')
product_category_name_translation = pd.read_csv(r'C:\Users\HP\Desktop\E-commerce Sales Forecasting\product_category_name_translation.csv')
# Merging datasets based on order_id
merged_data = pd.merge(orders, order_items, on='order_id', how='inner')
merged_data = pd.merge(merged_data, order_payments, on='order_id', how='inner')
# Check the first few rows
print(merged_data.head())

# Descriptive statistics
print(merged_data.describe())
import matplotlib.pyplot as plt
import seaborn as sns

top_products = merged_data.groupby('product_id')['order_item_id'].count().sort_values(ascending=False).head(10)

sns.barplot(x=top_products.index, y=top_products.values, palette="viridis")
plt.title('Top 10 Selling Products by Quantity')
plt.xlabel('Product ID')
plt.ylabel('Quantity Sold')
plt.xticks(rotation=90)
plt.show()
payment_distribution = merged_data['payment_type'].value_counts()

sns.barplot(x=payment_distribution.index, y=payment_distribution.values, palette="rocket")
plt.title('Distribution of Payment Types')
plt.xlabel('Payment Type')
plt.ylabel('Number of Transactions')
plt.show()
# Convert 'order_purchase_timestamp' to datetime type
merged_data['order_purchase_timestamp'] = pd.to_datetime(merged_data['order_purchase_timestamp'])

# Extract month-year from timestamp and group by this for total sales
merged_data['month_year'] = merged_data['order_purchase_timestamp'].dt.to_period('M')
monthly_sales = merged_data.groupby('month_year')['price'].sum()

monthly_sales.plot(kind='line', figsize=(15,7))
plt.title('Monthly Sales Over Time')
plt.xlabel('Time')
plt.ylabel('Sales Value')
plt.show()
