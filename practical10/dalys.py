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

#the third column (the year) for the first 10 rows
print("\nthe third column (the year) for the first 10 rows:")
print(dalys_data.iloc[0:10, 2]) 

# the 10th year with DALYs data recorded in Afghanistan
afghanistan_data = dalys_data.loc[dalys_data.Entity == "Afghanistan"]
print("\n the 10th year with DALYs data recorded in Afghanistan:", afghanistan_data.iloc[9, 2]) 
# so, the 10th year with DALYs data recorded in Afghanistan is 1999.

# use a Boolean to show DALYs for all countries in 1990.
dalys_1990 = dalys_data.loc[dalys_data.Year == 1990, "DALYs"]
print("\nDALYs in 1990:", dalys_1990)

# compute the mean DALYs in the UK and France
uk_data = dalys_data.loc[dalys_data.Entity == "United Kingdom", "DALYs"]
france_data = dalys_data.loc[dalys_data.Entity == "France", "DALYs"]
uk_mean = uk_data.mean()
france_mean = france_data.mean()
print(f"\nmean DALY in the UK:{uk_mean:.2f},the mean DALY in the France:{france_mean:.2f}")
# the mean DALY in the UK is greater than France

plt.figure(figsize=(10, 6))
plt.plot(uk_data.index, uk_data.values, 'b-', marker='o', label='DALYs in the UK')
plt.title('the DALYS over time in the UK')
plt.xlabel('years')
plt.ylabel('DALYs')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#question: Is the trend of DALYs in China and the UK the same between 1990 and 2019?
china_data = dalys_data.loc[dalys_data.Entity == "China", ["Year", "DALYs"]]
uk_data_time = dalys_data.loc[dalys_data.Entity == "United Kingdom", ["Year", "DALYs"]]
plt.figure(figsize=(12, 6))
plt.plot(china_data.Year, china_data.DALYs, 'r-', marker='s', label='China')
plt.plot(uk_data_time.Year, uk_data_time.DALYs, 'b-', marker='o', label='UK')
plt.title('comparison of the DALY trend in China and UK')
plt.xlabel('years')
plt.ylabel('DALYs')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('china_uk_dalys_comparison.png', dpi=300, bbox_inches='tight')
plt.show()
