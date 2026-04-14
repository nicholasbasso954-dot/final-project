import pandas as pd

# Load data
inflation = pd.read_csv("data/raw/inflation.csv")
construction = pd.read_csv("data/raw/construction_costs.csv")

# Rename columns for easier use
inflation.columns = ["date", "inflation_index"]
construction.columns = ["date", "construction_index"]

# Convert date to datetime
inflation["date"] = pd.to_datetime(inflation["date"])
construction["date"] = pd.to_datetime(construction["date"])

# Extract year
inflation["year"] = inflation["date"].dt.year
construction["year"] = construction["date"].dt.year

# Group by year (average)
inflation_yearly = inflation.groupby("year")["inflation_index"].mean().reset_index()
construction_yearly = construction.groupby("year")["construction_index"].mean().reset_index()

# Merge datasets
df = pd.merge(inflation_yearly, construction_yearly, on="year")

# Filter years
df = df[(df["year"] >= 2015) & (df["year"] <= 2025)]

# Save cleaned data
df.to_csv("data/processed/final_data.csv", index=False)

# Print result
print(df.head())
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned data
df = pd.read_csv("data/processed/final_data.csv")

st.title("Impact of Inflation on Construction Costs")

# Show data
st.subheader("Dataset")
st.write(df)

# Plot
st.subheader("Trends Over Time")

plt.figure()
plt.plot(df["year"], df["inflation_index"], label="Inflation")
plt.plot(df["year"], df["construction_index"], label="Construction Costs")
plt.legend()
plt.xlabel("Year")
plt.ylabel("Index Value")

st.pyplot(plt)