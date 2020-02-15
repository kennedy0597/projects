from random import randint

v = ["rock", "paper", "scissors"]

Computer = v[randint(0,2)]

player = False

while player == False:
    player = input("rock, paper, scissors? ")
    if player == Computer:
        print("Draw")
    elif player == "rock":
        if Computer == "paper":
            print("You lose")
        elif Computer == "scissors":
            print("You win")
    elif player == "paper":
        if Computer == "rock":
            print("You win")
        elif Computer == "scissors":
            print("You lose")
    elif player == "scissors":
        if Computer == "rock":
            print("You lose")
        elif Computer == "paper":
            print("You win")
    else:
        print("Wrong input, please check your spelling")
    player = False
    Computer = v[randint(0, 2)]



