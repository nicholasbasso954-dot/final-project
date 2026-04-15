import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/processed/final_data.csv")
year_range = st.slider(
    "Select Year Range",
    int(df["year"].min()),
    int(df["year"].max()),
    (int(df["year"].min()), int(df["year"].max()))
)

filtered_df = df[
    (df["year"] >= year_range[0]) &
    (df["year"] <= year_range[1])
]

# Title
st.title("Impact of Inflation on Construction Costs")
st.write(
    "This dashboard explores how inflation affected construction costs in the United States from 2015 to 2025. "
    "The project is designed for project managers, estimators, and construction firms that need to understand how inflation can influence budgeting, pricing, and planning decisions. "
    "By comparing inflation trends with construction cost trends, this dashboard helps users evaluate whether rising inflation is associated with higher construction expenses."
)
# Show dataset
st.subheader("Dataset")
st.write(filtered_df)

# Plot
st.subheader("Trends Over Time")

plt.figure()
plt.plot(filtered_df["year"], filtered_df["inflation_index"], label="Inflation")
plt.plot(filtered_df["year"], filtered_df["construction_index"], label="Construction Costs")
plt.legend()
plt.xlabel("Year")
plt.ylabel("Index Value")

st.pyplot(plt)
st.subheader("Inflation vs Construction Costs Comparison")
st.write("This scatter plot shows the relationship between inflation and construction costs. As inflation rises, construction costs generally increase.")
fig, ax = plt.subplots()
ax.scatter(filtered_df["inflation_index"], filtered_df["construction_index"], color="orange")
ax.set_xlabel("Inflation Index")
ax.set_ylabel("Construction Cost Index")
ax.set_title("Relationship Between Inflation and Construction Costs")
ax.grid(True)
st.pyplot(fig)
correlation = filtered_df["inflation_index"].corr(filtered_df["construction_index"])
st.write(f"Correlation coefficient (r): {correlation:.2f}")

st.write("This value indicates a strong positive relationship between inflation and construction costs.")

st.subheader("Conclusion")

st.write(
    "The analysis reveals a strong positive relationship between inflation and construction costs, as supported by both the visual trends and the correlation coefficient. "
    "As inflation increases, construction costs tend to rise as well, particularly in the years following 2020 where a sharp increase is observed. "
    "This indicates that inflation plays a significant role in driving construction expenses and should be carefully considered in project budgeting and planning."
)


st.subheader("Data and Methods")

st.write(
    "This project uses public economic data from FRED. The datasets were cleaned by converting dates, grouping values by year, "
    "and merging inflation and construction cost indices into one final dataset for analysis."
)
