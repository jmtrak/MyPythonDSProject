# loading_data.py
import os
import pandas as pd
# Load the data from the folder data_project
data_folder = "data_project" # Folder's name
loaded_dataframes = {} # Dictionary to store DataFrames

if not os.path.exists(data_folder):
    print(f"Folder '{data_folder}' does not exist.")
else:
    for filename in os.listdir(data_folder):
        if filename.endswith(".csv"):
            file_path = os.path.join(data_folder, filename)
            df_name = os.path.splitext(filename)[0]
            print(f"\n --- Loading and Describing {df_name}---")
            try:
                df = pd.read_csv(file_path)
                loaded_dataframes[df_name] = df
                print(f"Successfully loaded {df_name}. Shape: {df.shape})")
                print(df.info())
                print(f"Showing first 5 rows of {df_name}.")
                print(df.head())
                print(f"Describing {df_name}.")
                print(df.describe())

            except Exception as e:
                print(f"Error loading {df_name}: {e}")
        else:
            print(f"Skipping {filename}, no a CSV file.")

print("\n--- All DataFrames loaded ---")
if loaded_dataframes:
    for name, df in loaded_dataframes.items():
        print(f"DataFrame '{name}': Rows ={df.shape[0]}, Colums={df.shape[1]}")
else:
    print("No CSV file were loaded")