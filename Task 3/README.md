# Task 3: Data Analysis using Pandas

## 📌 Objective

This task demonstrates data analysis skills using the Pandas library in Python. The script loads, inspects, cleans, filters, groups, and aggregates a California Housing dataset to derive meaningful insights.

## 🛠️ How to Run

1. Ensure you have the required libraries installed: 
   `pip install pandas numpy`
2. Run the script using: 
   `python task3_data_analysis.py`

## 📸 Screenshots

### 1. Loading and Inspecting Data
![Data Inspection](PASTE_SCREENSHOT_1_LINK_HERE)

### 2. Cleaning Missing Data
![Data Cleaning](PASTE_SCREENSHOT_2_LINK_HERE)

### 3. Filtering Data
![Data Filtering](PASTE_SCREENSHOT_3_LINK_HERE)

### 4. Grouping and Aggregation
![Data Grouping](PASTE_SCREENSHOT_4_LINK_HERE)

## 📖 Explanation of the Code

*   **Loading & Inspection:** Used `pd.DataFrame()` and `df.head()` / `df.info()` to load the dataset and inspect its structure, data types, and initial rows.
*   **Data Cleaning:** Identified missing values using `df.isnull().sum()` and handled them by filling them with the median value using `fillna()`, ensuring no data is lost.
*   **Filtering:** Applied a conditional filter `df[df['median_income'] > 8.0]` to isolate high-income areas for targeted analysis.
*   **Grouping & Aggregation:** Created categorical age bins using `pd.cut()` and applied `groupby()` to calculate the mean house value and income for each age group.
*   **Insight Generation:** Extracted specific statistics from the filtered and grouped data to draw logical conclusions.

## 💡 Short Insight Summary

Based on the analysis, we discovered two key insights:

1.  **Income and House Value:** Areas with a median income greater than 8.0 have a significantly higher average house value (approx. $XXX,XXX) compared to the overall dataset average. This confirms a strong positive correlation between income levels and property values.
2.  **Age of Housing:** "Old" houses (41-60 years) have an average value of $XXX,XXX, which is slightly higher/lower than "New" houses (0-20 years) averaging $XXX,XXX. This suggests that historical value or location may play a role in property pricing over time.

*(Note: Replace the "XXX" values with the actual numbers from your terminal output!)*
