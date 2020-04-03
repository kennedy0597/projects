import pandas as pd
import matplotlib.pyplot as plt
import pygal
import plotly.io as pio

### question 4 ####
#### Part 1 ####

excel_file = "CompleteDataset.csv"
excel_data = pd.read_csv(excel_file)
df = pd.DataFrame(excel_data)

#### Part 2 and Part 3 #######
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

dfclean = df.drop(columns=["Photo", "Flag", "Dribbling"])
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

# graph 3
age2 = pd.DataFrame(df, columns=["Age", "Name"])
age2 = age2.groupby('Age').count()

gr2 = pygal.Bar(title="Player count per age", y_title="Count")
gr2.x_labels = range(16, 50)
for x in age2:
    gr2.add(x, age2[x])

gr2.render_in_browser()

# graph 4
clubs1 = pd.DataFrame(df, columns=["Nationality", "Club"])
clubscount = clubs1.groupby('Nationality').count()
countrylist = df["Nationality"].unique()
countrylist = sorted(countrylist)
xvalue1 = []
for y in countrylist:
     xvalue1.append(y)

gr2 = pygal.Bar(title="Count of clubs per country")
gr2.x_labels = xvalue1

for x in clubscount:
    gr2.add(x, clubscount[x])

gr2.render_in_browser()

# graph 5
data = [dict(
  type = 'scatter',
  x = excel_data['Club'],
  y = excel_data['Overall'],
  mode = 'markers',
  transforms = [dict(
    type = 'aggregate',
    groups = excel_data['Club'],
    aggregations = [dict(
        target = 'y', func = 'avg', enabled = True),
    ]
  )]
)]

fig_dict = dict(data=data)

pio.show(fig_dict, validate=False)