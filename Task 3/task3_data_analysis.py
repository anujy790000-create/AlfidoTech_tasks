import pandas as pd
import numpy as np

def run_data_analysis():
    print("--- 1. Loading and Inspecting the Dataset ---")
    
    # Generating a synthetic California Housing dataset to match your screenshot
    # If you have the actual 'california_housing_test.csv', you can use:
    # df = pd.read_csv('california_housing_test.csv')
    np.random.seed(42)
    data = {
        'longitude': np.random.uniform(-124.3, -114.3, 3000),
        'latitude': np.random.uniform(32.5, 42.0, 3000),
        'housing_median_age': np.random.randint(1, 53, 3000),
        'total_rooms': np.random.randint(6, 30000, 3000),
        'total_bedrooms': np.random.randint(2, 5000, 3000),
        'population': np.random.randint(5, 12000, 3000),
        'households': np.random.randint(2, 5000, 3000),
        'median_income': np.random.uniform(0.5, 15.0, 3000),
        'median_house_value': np.random.uniform(22500, 500001, 3000)
    }
    df = pd.DataFrame(data)
    
    # Introduce some missing values to demonstrate data cleaning
    df.loc[0:50, 'total_bedrooms'] = np.nan

    print("Dataset loaded successfully!")
    print("\nFirst 5 rows of the dataset:")
    print(df.head())
    
    print("\nDataset Information:")
    df.info()

    print("\n--- 2. Cleaning Missing Data ---")
    print("Missing values before cleaning:")
    print(df.isnull().sum())
    
    # Fill missing values in 'total_bedrooms' with the median
    df['total_bedrooms'] = df['total_bedrooms'].fillna(df['total_bedrooms'].median())
    
    print("\nMissing values after cleaning:")
    print(df.isnull().sum())

    print("\n--- 3. Filtering Data ---")
    # Filter for areas with a high median income (e.g., > 8.0)
    high_income_df = df[df['median_income'] > 8.0]
    print(f"Filtered dataset (median_income > 8.0): {len(high_income_df)} rows found.")
    print(high_income_df.head())

    print("\n--- 4. Grouping and Aggregation ---")
    # Create age groups for grouping
    bins = [0, 20, 40, 60]
    labels = ['New (0-20)', 'Moderate (21-40)', 'Old (41-60)']
    df['age_group'] = pd.cut(df['housing_median_age'], bins=bins, labels=labels)
    
    # Group by the new age group and calculate the mean
    grouped_df = df.groupby('age_group', observed=True)[['median_house_value', 'median_income']].mean()
    print("Average House Value and Income by Age Group:")
    print(grouped_df)

    print("\n--- 5. Insights Summary ---")
    print(f"1. High-income areas (>8.0) have an average house value of ${high_income_df['median_house_value'].mean():,.2f}.")
    print(f"2. The average house value for 'Old' houses is ${grouped_df.loc['Old (41-60)', 'median_house_value']:,.2f}, while 'New' houses average ${grouped_df.loc['New (0-20)', 'median_house_value']:,.2f}.")

if __name__ == "__main__":
    run_data_analysis()