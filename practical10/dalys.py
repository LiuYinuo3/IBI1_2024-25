# Import libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set working directory
os.chdir("C:/IBI/IBI1_2024-25/practical10")
# Check current working directory and files
print("Current directory:", os.getcwd())
print("Files in directory:", os.listdir())

# Load the dataset
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# View first 5 rows of datas
print(dalys_data.head(5))
# Get dataframe information(data types, columne names, how many rows)
print(dalys_data.info())
# Get statistical summary( shows the number of entries, mean, standard deviation and a number of quantiles.)
print(dalys_data.describe())

# selection, Show first row, fourth column
print(dalys_data.iloc[0, 3])
# Show third column for first 10 rows
print(dalys_data.iloc[0:10, 2])  # 10th year in Afghanistan is 1999 (0-based index)
# Boolean indexing example, show the columns where the values are True
my_columns = [True, True, False, True]
print(dalys_data.iloc[0:3, my_columns])
# Get all rows where Year is 1990
year_1990 = dalys_data["Year"] == 1990
print(dalys_data.loc[year_1990, "DALYs"])