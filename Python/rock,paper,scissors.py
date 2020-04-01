from random import randint


def continueorquit():
    cont = input("Continue or quit? ")
    if cont == "cont":
        main()
    elif cont == "quit":
        quit()
    else:
        print("wrong input")


def main():
    player = False
    while player is False:
        player = input("rock, paper, scissors? ")
        if player == "quit":
            quit()
        player2 = input("rock, paper, scissors? ")
        if player == player2:
            print("Draw")
            continueorquit()
        elif player == "rock":
            if player2 == "paper":
                print("Player2 win")
                continueorquit()
            elif player2 == "scissors":
                print("Player1 win")
                continueorquit()
        elif player == "paper":
            if player2 == "rock":
                print("Player1 win")
                continueorquit()
            elif player2 == "scissors":
                print("Player2 win")
                continueorquit()
        elif player == "scissors":
            if player2 == "rock":
                print("Player2 win")
                continueorquit()
            elif player2 == "paper":
                print("Player1 win")
                continueorquit()
        else:
            print("Wrong input, please check your spelling")
            continueorquit()


main()
