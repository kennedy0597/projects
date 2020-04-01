import random

allchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+=-,./;'[]\{|}<>?"
password = ''
weaklist = ["password", "password123", "12345678", "qwerty"]

choice = input("weak/strong :")

if choice == "strong":
    length = random.randint(10, 20)
    for c in range(int(length)):
        password += random.choice(allchars)
elif choice == "weak":
    password = weaklist[random.randint(0, 3)]
else:
    print("wrong input")

print(password)
