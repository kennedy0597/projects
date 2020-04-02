import pandas as pd

a_dict = {"testerino": "05/08/1994",
          "peperino": "02/07/1993",
          "qwerty": "02/07/1991",
          "asdfgh": "03/07/2000",
          "bob": "05/10/1997",
          "bobby": "12/09/1994",
          "kumar": "03/02/1996",
          "ahbeng": "09/08/1992",
          "ahseng": "04/12/1993",
          "ahleng": "04/03/1999",
          "ahsiao": "05/07/1991"}

# name = input("Enter name: ")
# print(a_dict[name])

months = []
for i in a_dict:
    birthdate = (a_dict[i])
    birthday = (a_dict[i].split("/"))
    getmonth = birthday[1]
    month = int(getmonth)
    months.append((month))
    a_dict[i] = [birthdate, month]

samemonth = set()
months.sort()
for month1 in months:
    if month1 not in samemonth:
        print("the count for month", month1, "is", months.count(month1))
        samemonth.add(month1)

df = pd.DataFrame(a_dict)
writer = pd.ExcelWriter('players.xlsx', engine="xlsxwriter")
df.to_excel(writer, sheet_name="birthdays")
writer.save()