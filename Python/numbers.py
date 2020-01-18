number = int(input("Enter a number "))
if number != 200:
    if number < 200:
        number2 = (200 - number)
        print("your number needs to be added by " + str(number2) + " to be 200")
    elif number > 200:
        number2 = (number - 200)
        print("your number needs to be decreased by " + str(number2) + " to be 200")
elif number == 200:
    print("number is already  200")




