import pandas as pd
import numpy as np
excel_file = "emp1.xlsx"
excel_data = pd.read_excel(excel_file)
print(excel_data.head())
print(excel_data)

# Fetch specific columns using dataframe
excel_data = pd.DataFrame(excel_data, columns=["Name", "Title"])
print(excel_data)

# stat function using dataframe
excel_data = pd.read_excel(excel_file)
sum1 = excel_data['Wages'].sum()
print(sum1)

mean1 = excel_data['Wages'].mean()
print(mean1)

max1 = excel_data['Wages'].max()
print(max1)

# sort
sort1 = excel_data.sort_values(['Name'], ascending=True)
print(sort1)


# graph function
import matplotlib.pyplot as plt
sort1['Wages'].plot(kind="bar")
plt.show()


# Dataframe from a dictionary
olympic_dict = {"London": {2012: 205}, "Beijing": {2008: 204}}
df = pd.DataFrame(olympic_dict)
print(df)


olympic_dict1 = {"HostCity": ["London", "Beijing", "Athens", "Sydney", "Atlanta"],
                 "Year": [2012, 2008, 2004, 2000, 1996],
                 "No. of Countries": [205, 204, 203, 200, 190]}

df1 = pd.DataFrame(olympic_dict1)
print(df1)

# Dataframe from a dataframe
print(pd.DataFrame(df1, columns=['HostCity', 'Year']))


# Writing to excel file
df2 = pd.DataFrame(olympic_dict)
writer = pd.ExcelWriter('olympic.xlsx', engine="xlsxwriter")
df2.to_excel(writer, sheet_name="Sport")
writer.save()

df2_file = "olympic.xlsx"
df2_data = pd.read_excel(df2_file)
print(df2_data)

# using numpy
data = {'name': ['test', 'testerino', 'peperino', 'asdfg', 'qwerty'],
        'year': [2012, 2013, 2012, 2014, 205],
        'reports:': [4, 56, 67, 2, 565],
        'coverage': [25, 45, 56, 65, 12]}
df = pd.DataFrame(data, index=['Cochine', 'Pima', 'Santa Cruz', 'Maricopa', 'Yuma'])
print(df)

# drop name
df = df.drop('name', axis=1)
print(df)

# return square root of every numeric data
print(df.applymap(np.sqrt))
