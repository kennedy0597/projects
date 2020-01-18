#Write a Python/Java/.Net program that outputs all possibilities to put + or - or nothing
#between the numbers 1, 2, ..., 9, 0 (in this order) such that the result is always 200.
#For example:
#1+2+3+45+67-8+90
#1+234+56+7-8-90
#(Clue: There are 10 possible combinations and 2 are already provided above. Do note there
#is no + or - sign before the number 1.)
#Please make sure the program can be executed or compiled without error or warning.
#Please indicate the programming language which your code is based

# A recursive solution for subset sum
# problem

# Returns true if there is a subset
# of set[] with sun equal to given sum
def isSubsetSum(set, n, sum):
    # Base Cases
    if (sum == 0):
        return True
    if (n == 0 and sum != 0):
        return False

    # If last element is greater than
    # sum, then ignore it
    if (set[n - 1] > sum):
        return isSubsetSum(set, n - 1, sum);

        # else, check if sum can be obtained
    # by any of the following
    # (a) including the last element
    # (b) excluding the last element
    return isSubsetSum(set, n - 1, sum) or isSubsetSum(set, n - 1, sum - set[n - 1])


# Driver program to test above function
set = [3, 34, 4, 12, 5, 2]
sum = 100
n = len(set)
if (isSubsetSum(set, n, sum) == True):
    print("Found a subset with given sum")
else:
    print("No subset with given sum")


