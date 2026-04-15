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
st.caption("Use the year slider to explore how inflation and construction costs change over time.")
st.subheader("Project Motivation")

st.write(
    "Rising inflation has significantly impacted the construction industry, affecting material prices, labor costs, and overall project budgets. "
    "For project managers and construction firms, understanding how inflation influences costs is critical for accurate budgeting and planning.\n\n"

    "This project aims to analyze the relationship between inflation and construction costs in the United States, helping stakeholders make more informed financial and strategic decisions."
)
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
st.subheader("Key Insight")

st.write(
    "The strongest finding from this analysis is the clear positive relationship between inflation and construction costs. "
    "As inflation increases, construction costs consistently rise as well.\n\n"

    "This suggests that inflation is a major driver of cost increases in the construction industry, "
    "which directly impacts budgeting, project planning, and financial forecasting."
)
st.subheader("Results")

st.write(
    "The analysis reveals a strong positive relationship between inflation and construction costs, as supported by both the visual trends and the correlation coefficient. "
    "As inflation increases, construction costs tend to rise as well, particularly in the years following 2020 where a sharp increase is observed. "
    "This indicates that inflation plays a significant role in driving construction expenses and should be carefully considered in project budgeting and planning."
)
st.subheader("Limitations & Next Steps")

st.write(
    "This project focuses on the relationship between inflation and construction costs using a limited set of economic indicators. "
    "Other important factors such as labor shortages, regional differences, supply chain disruptions, tariffs, and interest rates were not included. "
    "Future work could expand the analysis by adding more variables, comparing regions, or developing a forecasting model to predict future construction cost changes."
)

st.subheader("Data Collection & Preprocessing")

st.write(
    "The data used in this project was sourced from publicly available economic data from FRED (Federal Reserve Economic Data). "
    "The dataset includes yearly inflation index values and construction cost index values.\n\n"

    "Preprocessing steps included:\n"
    "- Cleaning and standardizing column names\n"
    "- Converting data into numerical format for analysis\n"
    "- Handling missing or inconsistent values\n"
    "- Merging inflation and construction datasets by year\n\n"

    "These steps ensured the data was accurate, aligned, and ready for analysis and visualization."
)
