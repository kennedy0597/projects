import pandas as pd

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

#### question 5 #######
# aggregate function 1, find number of players in each club
count1 = df2.value_counts()
print(count1)

# aggregate function 2, find player with highest overall score
max1 = excel_data['Overall'].max()
for x, y in excel_data.iterrows():
    if y['Overall'] == max1:
        print(y['Name'], "has the highest overall performance score of", str(max1))

# aggregate function 3, average age of all players
average = excel_data['Age'].mean()
print("The average age of all players is", average)

# youngest player
min1 = excel_data['Age'].min()
print("youngest player is", min1, "years old")

# average age for each club
test123 = pd.DataFrame(excel_data, columns=["Club", "Age"])
avg1 = test123.groupby('Club').mean()
print(avg1)



# Question 6