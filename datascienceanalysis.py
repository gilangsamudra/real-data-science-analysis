# import necessary libraries
import pandas as pd
import os
import matplotlib.pyplot as plt

# Merging 12 months of sales data into a singe file
data1 = pd.read_csv('D:/Phyton Code/Contoh dari Github/Pandas-Data-Science-\
Tasks-master/SalesAnalysis/Sales_Data/Sales_April_2019.csv')

all_data = pd.DataFrame()

files = [file for file in os.listdir('D:/Phyton Code/Contoh dari Github/\
Pandas-Data-Science-Tasks-master/SalesAnalysis/Sales_Data')]

for file in files:
    temp = pd.read_csv('D:/Phyton Code/Contoh dari Github/Pandas-Data-Science-\
Tasks-master/SalesAnalysis/Sales_Data/' + file)
    all_data = pd.concat([all_data, temp])

# Clean up Nan Values
all_data.isnull().sum()
all_data.dropna(axis=0, how='any', inplace=True)


all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']

# Add an additional column
all_data['Month'] = all_data['Order Date'].str[0:2]
all_data['Month'] = all_data['Month'].astype('int32')

all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])

all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']

# max sales
sales = all_data.groupby('Month').sum()
maxi = sales['Sales'].idxmax()

# Plot
ax = sales.plot.bar(y='Sales', rot=1, legend=False)
ax.set_ylabel('Sales in USD $')

