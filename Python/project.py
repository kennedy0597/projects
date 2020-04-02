import pandas as pd
import matplotlib.pyplot as plt


a_dict = {"testerino": "05/08/1994",
          "peperino": "02/07/1993",
          "qwerty": "02/07/1991",
          "asdfgh": "03/07/2000",
          "bob": "05/10/1997",
          "bobby": "12/09/1994",
          "kumar": "03/02/1996",
          "ahbeng": "09/08/1992",
          "ahseng": "04/05/1993",
          "ahleng": "04/06/1999",
          "ahsiao": "05/07/1991"}

# name = input("Enter name: ")
# print(a_dict[name])

months = []
for i in a_dict:
    birthdate = (a_dict[i])
    birthday = (a_dict[i].split("/"))
    getmonth = birthday[1]
    month = int(getmonth)
    months.append(month)
    a_dict[i] = [birthdate, month]

monthdict = {1: months.count(1), 2: months.count(2), 3: months.count(3), 4: months.count(4), 5: months.count(5), 6: months.count(6),
             7: months.count(7), 8: months.count(8), 9: months.count(9), 10: months.count(10), 11: months.count(11), 12: months.count(12)}

for x in monthdict:
    print(" the count of month", x, "is", monthdict[x])

df = pd.DataFrame(a_dict)
writer = pd.ExcelWriter('players.xlsx', engine="xlsxwriter")
df.to_excel(writer, sheet_name="birthdays")
writer.save()

# question 3
keys = monthdict.keys()
values = monthdict.values()
plt.bar(keys, values, color='g', width=0.5)
plt.xlabel("Month")
plt.ylabel("Count")
plt.title("Birthday count per month")
plt.show()

