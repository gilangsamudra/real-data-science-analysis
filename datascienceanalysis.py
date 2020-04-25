# import necessary libraries
import pandas as pd
import os

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
