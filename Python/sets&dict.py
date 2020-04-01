# creating a set

names = set()
names.add("Michelle")
names.add("Robin")
names.add("Michelle")
print("Names in set", names)

a_set = {0, 4, 2, 'hello', 8, False}
print(a_set)

# Updating set
a_set.add(12)
print(a_set)
print("length of set: ", len(a_set))

a_set.update({11, 12, 13})
print(a_set)

a_set.update({44, 7, 50}, {45, 46, 47})
print(a_set)
a_set.update('a', 'b', 'c')
print(a_set)

# discard
a_set.discard(12)
print(a_set)

# remove
a_set.discard('a')
print(a_set)

# poping
a_set.pop()
a_set.discard(12)
print(a_set)
a_set.clear()
print(a_set)



######## DICT ########
# creating dict
a_dict = {'test': '99', 'testerino': '89', 'qwerty': '70', 'asdf': '55'}
print("elements of dict with key value", a_dict)

# Getting individual element
print(a_dict["testerino"])

# update dict
a_dict["asdf"] = 88
print(a_dict)

b_dict = {'server': 'db.fdmgroup.org', 'database': 'mysql'}
print('Elements of dict with key values:', b_dict)

# getting specific key
print(b_dict["server"])

# update dict
b_dict['database'] = "oracle"
print(b_dict)

# adding element
b_dict["user"] = "Kenny"
print(b_dict)


# keys mapped with lists
employee_table = {1001: ["John Doe", "Manager", 8000],
                  1002: ["Testerino", "qwerty", 20000],
                  1010: ["Peperino", "Boss", 9999]}
print(employee_table)
print(employee_table[1002])