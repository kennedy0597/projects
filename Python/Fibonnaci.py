num = int(input("Enter the number of fibonnaci sequence: "))


num1=0
num2=1

count=0

if num == 1:
    print(num1)
else:
    print("Fibonacci sequence up to",num)
    while count < num:
        print(num1)
        numN = num1 + num2 

        num1 = num2 
        num2 = numN
        count += 1
