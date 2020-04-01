import pandas as pd

pd.set_option('display.max_columns', None,)
pd.set_option('display.max_rows', None,)
excel_file = "Automobile_data.csv"
excel_data = pd.read_csv(excel_file)

# 1.Print the first five and last five rows
print(excel_data.iloc[0:5, :])
print(excel_data.iloc[56:61, :])

# 2.Clean the data and update CSV. Replace all column values which contain ‘?’ and n.a with NA
print(excel_data.dropna)
print(excel_data.fillna("NA"))

# 3.Find the most expensive car company name
max1 = excel_data['price'].max()
print(max1)

# 4.Print all audi car details
audicars = excel_data[excel_data['company'] == 'audi']
print(audicars)

# 5.Count total cars per company
count1 = excel_data['company'].value_counts()
print(count1)

# 6.Find each company’s highest price car
excel_data1 = pd.DataFrame(excel_data, columns=["company", "price"])
maxcount1 = excel_data1.groupby('company').max()
print(maxcount1)

# 7.Sort all the cars by price
sort1 = excel_data.sort_values(['price'], ascending=False)
print(sort1)

# 8.Find the average mileage of each car
excel_data2 = pd.DataFrame(excel_data, columns=["company", "average-mileage"])
avg1 = excel_data2.groupby('company').mean()
print(avg1)

