import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Sales Dashboard")

df = pd.read_csv("data/sales_data.csv")
df["date"] = pd.to_datetime(df["date"])
df["revenue"] = df["quantity"] * df["price"]

# KPIs
st.subheader("Key Metrics")
st.write("Total Revenue:", df["revenue"].sum())
st.write("Total Orders:", len(df))
st.write("Average Order Value:", round(df["revenue"].mean(), 2))

# Monthly Revenue
df["month"] = df["date"].dt.to_period("M")
monthly_revenue = df.groupby("month")["revenue"].sum()

st.subheader("Monthly Revenue Trend")
fig, ax = plt.subplots()
monthly_revenue.plot(ax=ax)
st.pyplot(fig)

# Product Revenue
st.subheader("Revenue by Product")
product_revenue = df.groupby("product")["revenue"].sum()
fig2, ax2 = plt.subplots()
product_revenue.plot(kind="bar", ax=ax2)
st.pyplot(fig2)
