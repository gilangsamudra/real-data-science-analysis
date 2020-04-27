# import necessary libraries
import pandas as pd
import os
import matplotlib.pyplot as plt
from itertools import combinations
from collections import Counter

def get_city(address):
    return address.split(',')[1]

def get_state(address):
    return address.split(',')[2].split(' ')[1]


# plt.style.use('fivethirtyeight')

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

# max sales by Month
sales1 = all_data.groupby('Month').sum()
maxi_month = sales1['Sales'].idxmax()

# Plot
plt.figure(num=1, dpi=300)
ax1 = sales1.plot.bar(y='Sales', grid=False, rot=0, legend=False, ax=plt.gca())
ax1.set_ylabel('Sales in USD $')
ax1.grid(b=True, which='major', axis='y', ls='--', lw=.5, c='k', alpha=.3)


# extracting cities data
all_data['City'] = all_data['Purchase Address'].apply(lambda x: f"{get_city(x)} ({get_state(x)})")

# Max Sales by City
sales2 = all_data.groupby('City').sum()
maxi_city = sales2['Sales'].idxmax()

plt.figure(num=2, dpi=300)
ax2 = sales2.plot.bar(y='Sales', grid=False, rot=90, legend=False, ax=plt.gca())
ax2.set_ylabel('Sales in USD $')
ax2.grid(b=True, which='major', axis='y', ls='--', lw=.5, c='k', alpha=.3)

# a techinque to extract values from a dataframe in similiar order as the original
cities = [city for city, datafra in all_data.groupby('City')]


# Parsing date
all_data['Order Date'] = pd.to_datetime(all_data['Order Date'])
all_data['Hour'] = all_data['Order Date'].dt.hour
all_data['Minute'] = all_data['Order Date'].dt.minute

hours = [hour for hour, datfra in all_data.groupby('Hour')]
plt.figure(dpi=300)
plt.plot(hours, all_data.groupby('Hour').count())
plt.xlabel('Hour')
plt.ylabel('# of Orders')
plt.xticks(hours)
plt.grid(b=True, which='major', ls='--', lw=.5, c='k', alpha=.3)
plt.title('Order count by hour')

# What products are most often sold together?
df = all_data[all_data['Order ID'].duplicated(keep=False)]
df['Grouped'] = df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))
df = df[['Order ID', 'Grouped']].drop_duplicates()

# Counting combination
count = Counter()
for row in df['Grouped']:
    row_list = row.split(',')
    count.update(Counter(combinations(row_list,2)))

for key, value in count.most_common(10):
    print(key, value)
