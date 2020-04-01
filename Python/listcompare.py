import random as r

randomlistofint = [r.randint(1, 99) for iter in range(r.randint(1, 9))]
randomlistofint2 = [r.randint(1, 99) for iter in range(r.randint(1, 9))]


list1 = list(dict.fromkeys(randomlistofint))
list2 = list(dict.fromkeys(randomlistofint2))
print(list1)
print(list2)


for ele in list1:
    if ele in list1 and ele in list2:
        print(ele)


a = [1, 2, 3, 4, 5]
b = [9, 8, 7, 6, 5]
print(set(a) & set(b))