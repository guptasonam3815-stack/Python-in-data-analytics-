import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run_analytics_pipeline():
    print("--- 1. Data Ingestion Step ---")
    # Creating a sample dataset automatically for demonstration
    data = {
        'OrderID':,
        'Product': ['Laptop', 'Mouse', 'Monitor', 'Keyboard', np.nan, 'Mouse', 'Laptop'],
        'Quantity': [1, 2, np.nan, 1, 3, 5, 2],
        'Price': [75000, 1500, 12000, 2500, 1500, 1500, 75000]
    }
    df = pd.DataFrame(data)
    print("Dataset loaded successfully!")
    print(df.head())

    print("\n--- 2. Data Cleaning Step ---")
    # Checking for missing values
    print("Missing values before cleaning:\n", df.isnull().sum())
    
    # Filling missing values safely
    df['Product'] = df['Product'].fillna('Unknown Product')
    df['Quantity'] = df['Quantity'].fillna(1)
    print("Data cleaning completed.")

    print("\n--- 3. Exploratory Data Analysis (EDA) ---")
    # Calculating Total Sales
    df['Total_Sales'] = df['Quantity'] * df['Price']
    
    # Getting basic statistics
    print("\nSummary Statistics:")
    print(df.describe())

    print("\n--- 4. Visual Reporting Step ---")
    # Setting up the plot style
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(8, 5))
    
    # Creating a bar plot of total sales per product
    sns.barplot(x='Product', y='Total_Sales', data=df, estimator=sum, errorbar=None, palette="viridis")
    plt.title('Total Sales by Product Profile')
    plt.xlabel('Product')
    plt.ylabel('Total Sales (INR)')
    
    # Saving the chart locally
    chart_filename = 'sales_report_chart.png'
    plt.savefig(chart_filename)
    print(f"Success! Analysis completed and visual chart saved as '{chart_filename}'.")

if __name__ == "__main__":
    run_analytics_pipeline()
