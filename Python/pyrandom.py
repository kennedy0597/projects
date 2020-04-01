import random

print('-'*10, "Method 1", '-'*10)
rd=random.randint(1,9)
guess=0
c=0

while guess != rd and guess !="exit":
    guess=input("Enter a guess between 1 to 9: ")

    if guess=="exit":
        break
    
    guess=int(guess)
    c+=1


    if guess<rd:
        print("too low")
    elif guess>rd:
        print("too high")
    else:
        print("right, you took only",c,"tries!")