a_dict = {"Testerino": ["05/08/1992"],
          "Peperino": ["02/07/1992"],
          "qwerty": ["02/07/1992"],
          "asdfgh": ["03/07/1992"],
          "Hobbies": []}

# print(a_dict)
# name = input("Enter name: ")
# print(a_dict[name])

for x in a_dict:
    name1 = x
    if x == "Hobbies":
        break
    hobby = input("please enter the hobby for %s :" % name1)
    a_dict["Hobbies"].append(hobby)


count = 0
samehobby = []

for i in a_dict["Hobbies"]:
    for j in a_dict["Hobbies"]:
        if i == j:
            count += 1
        if count > 1:
            if i not in samehobby:
                samehobby.append(i)
        count = 0

print(a_dict)
print(len(samehobby), "same hobbies")
