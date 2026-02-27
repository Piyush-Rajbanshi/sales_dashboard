import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/sales_data.csv")
df["date"] = pd.to_datetime(df["date"])
df["revenue"] = df["quantity"] * df["price"]

# Monthly Revenue Trend
df["month"] = df["date"].dt.to_period("M")
monthly_revenue = df.groupby("month")["revenue"].sum()

plt.figure()
monthly_revenue.plot()
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_revenue.png")

# Top Products
product_revenue = df.groupby("product")["revenue"].sum()

plt.figure()
product_revenue.plot(kind="bar")
plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("product_revenue.png")

print("Charts generated successfully.")
