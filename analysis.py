import pandas as pd

# Load dataset
df = pd.read_csv("data/sales_data.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Create revenue column
df["revenue"] = df["quantity"] * df["price"]

# ===== Business Insights =====

total_revenue = df["revenue"].sum()
total_orders = len(df)
average_order_value = df["revenue"].mean()

top_product = df.groupby("product")["revenue"].sum().idxmax()
top_region = df.groupby("region")["revenue"].sum().idxmax()

print("===== SALES REPORT =====")
print(f"Total Revenue: ${total_revenue}")
print(f"Total Orders: {total_orders}")
print(f"Average Order Value: ${round(average_order_value,2)}")
print(f"Top Product: {top_product}")
print(f"Top Region: {top_region}")
