# data_exploratory.py

# Import the pandas library, commonly aliased as 'pd'
import pandas as pd

print("--- My first pandas series---")
#Create a simple pandas series
data_series = pd.Series([10,20,30,40,50])
print(data_series)

print("--- My first pandas DataFrame---")
#Create a Simple pandas DataFrame
data_frame = pd.DataFrame({
    "Product": ["Laptop Pro","Mouse X","Keyboard K", "Monitor Z"],
    "Price": [1200.00, 25.50, 75.00, 300.25],
    "Quantity": [10, 50,30,15]
    })
print(data_frame)

print("\n--- Basic Df Info---")
print(data_frame.info())

print("--- Describe Df ---")
print(data_frame.describe())

print("\n--- Loading Data from CSV---")
# Load the sales_data.csv into DataFrame
try: 
    sales_df = pd.read_csv("sales_data.csv")

    print("\n--- Sales DataFrame .head() ---")
    print(sales_df.head())
    print("\n--- Sales DataFrame .tail() ---")
    print(sales_df.tail(3))
    print("\n--- Sales DataFrame .info() ---")
    print(sales_df.info())
    print("\n--- Descriptive Statistics of sales_df (describe()): ---")
    print(sales_df.describe())
except FileNotFoundError:
    print("Error: 'sales_data.csv' not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")