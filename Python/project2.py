import pandas as pd
import matplotlib.pyplot as plt
import pygal
#### Part 1 ####

excel_file = "CompleteDataset.csv"
excel_data = pd.read_csv(excel_file)
df = pd.DataFrame(excel_data)
df1 = df['Name']
df2 = df['Club']
df3 = df['Wage']

df1 = df1.str.replace(r"[^a-zA-Z\d\_\s]+", "")
df2 = df2.str.replace(r"[^a-zA-Z\d\_\s]+", "")
df3 = df3.str.replace(r"[^a-zA-Z\d\_\s]+", "")

print(df1)
print(df2)
print(df3)

df.update(df1)
df.update(df2)
df.update(df3)
print(df)


#### part 4 ######

dfclean = df.drop(columns=["Photo", "Flag"])
print(dfclean)

#### part 5 #######
# aggregate function 1, find number of players in each club
count1 = df2.value_counts()
print(count1)

# aggregate function 2, find player with highest overall score
max1 = df['Overall'].max()
for x, y in df.iterrows():
    if y['Overall'] == max1:
        print(y['Name'], "has the highest overall performance score of", str(max1))

# aggregate function 3, average age of all players
average = df['Age'].mean()
print("The average age of all players is", average)

# youngest player
min1 = df['Age'].min()
print("youngest player is", min1, "years old")

# average age for each club
test123 = pd.DataFrame(df, columns=["Club", "Age"])
avg1 = test123.groupby('Club').mean()
print(avg1)



# Question 6
pd.set_option('display.max_columns', None,)
df['Wage'] = df['Wage'].str.replace("K", "")
df['Wage'] = df['Wage'].astype(int)
sort2 = df.sort_values(['Club', 'Wage'], ascending=False)
print(sort2)

# part 7
groupby1 = df.sort_values(['Nationality'], ascending=False)
print(groupby1)

# part 8
excel_data2 = pd.DataFrame(df, columns=["Age", "Potential"])
avg2 = excel_data2.groupby('Age').mean()
print(avg2)

# part 9
# graph 1
plt.plot(avg2)
plt.xlabel("Age")
plt.ylabel("Average potential")
plt.title("The average potential for each age group")
plt.show()


# graph 2
dfnation = df["Nationality"].value_counts()
xvalue1 = df["Nationality"].unique()
print(dfnation)
plt.bar(xvalue1, dfnation)
plt.show()

