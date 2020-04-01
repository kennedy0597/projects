# function without parameters


def add(x, y):
    return x + y


def multi(x, y):
    return x * y


def sub(x, y):
    return x - y


def div(x, y):
    return x/y


num1 = int(input("enter the first number: "))
choice = input("add/sub/multi/div? ")
num2 = int(input("enter the second number: "))


def main():
    if choice == "add":
        print(add(num1, num2))
    elif choice == "sub":
        print(sub(num1, num2))
    elif choice == "multi":
        print(multi(num1, num2))
    elif choice == "div":
        print(div(num1, num2))
    else:
        print("invalid choice")


def one_argument(arg):
    print("One argument: ", arg)


# any number of values
def flexible_number_of_arguments(*args):
    asd1 = 0
    for n in args:
        asd1 += n
        print("Sum of arguments in *args ", asd1)


# any number of values and any type of value
def two_argument_with_one_flexible_number_arguments(arg, *args):
    print("1st argument ", arg)
    for one in args:
        print(one, "from * args")


def two_argument_with_variable_length_argument_and_dict(*args, **kargs):
    for arg in args:
        print(arg)
    for k,v in kargs.items():
        print("Print dict", k, ":", v)


one_argument(4)
flexible_number_of_arguments(2, 4, 5)
args = ("34", 3443, "a", 5)  # Tuple
two_argument_with_one_flexible_number_arguments(7, args)
kargs={'name':'kennedy', 'role':'trainee'}  # dictionary
two_argument_with_variable_length_argument_and_dict(args, kargs)