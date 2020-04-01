# creating list
bicycle = ['trek', 'cannondale', 'redline', 'specialized']
print('Elements of Bicycle: ', bicycle)

# accessing list elements
print(bicycle[0])

my_folders = ['python', 'java', 'sql', 'C', 'C++']
print("Elements of my folder: ", my_folders)
print('\n')  # new line

print("Index of java in my folders: ", my_folders.index('java'))

# counting for values in a list
fruits = ['apple', 'orange', 'grapes', 'apple']
print('Number of apples in list: ', fruits.count('apple'))

# Adding items to list
num_books = int(input("Enter number of books to add: "))
book_list = ['test']

i = 0
while i < num_books:
    book = input("key in a book name: ")
    book_list = book_list + [book]  # string book -> list
    i += 1
print("adding elements to list: ", book_list)

# Insert at specified index
book_list.insert(3, 'testerino')
print("adding element by index: ", book_list)

# Appending to a list
book_list.append('nice')
print("adding element using append: ", book_list)

# Extending a list
book_list.extend(['HarryPotter', 'asdasd'])
print("extending list ", book_list)

# Removal of element from list
del fruits[2]
print('After removing 2nd element ', fruits)

fruits.remove(fruits[2])
print('After removing 2nd element ', fruits)

fruits.remove('apple')
print('After removing apple ', fruits)

print("Before pop: ", my_folders)
my_folders.pop()
print("after pop: ", my_folders)

# Finding length of list
print(len(my_folders))

# Sorting
my_folders.sort()
print(my_folders)

# Reversing
my_folders.reverse()
print(my_folders)

# using in operator - membership operator
name = input("Enter the name of bicycle to search: ")
if name in bicycle:
    print(name, "exist in bicycle")
else:
    print('not found')

print("\n")

##### TUPLES ###########

# Creating a Tuple
multiple = ('Sunday', 2, False)
print(multiple)

# Tuple to list

list(multiple)
print(type(list(multiple)))

multiple_list = []
multiple_list = list(multiple)
print(multiple_list)

# List to tuple
print(multiple_list)
multiple_tuple = tuple(multiple_list)
print(multiple_tuple)

num_tuple = (1, 2, 2, 4, 67, 34)
print(len(num_tuple))
print(max(num_tuple))


# Pass tuple and get set
def cubeOf(n):
    return n * n * n


result = map(cubeOf, num_tuple)
print(result)
num_set=set(result)
print(num_set)