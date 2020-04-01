# writing a file
# testtext = "aiosdjioasjodoajdjaso x,comaolsmdokqwokek,samocmoaskdoqmeo"
# file_handler = open("test1.txt", "w")
# file_handler.write(testtext)
# file_handler.close()


# reading file method 1
read_handler = open("test1.txt", "r").read()
print(read_handler)

# reading file method 2 line splitting
read_handler = open("test1.txt", "r")
for line in read_handler:
    print('*****', line.rstrip())
read_handler.close()

# reading file method 3 word splitting
rhandler = open("test1.txt", "r")
for line in rhandler:
    print('*****', line.split())
rhandler.close()

# reading file method 4 converting to list
rhandler = open("test1.txt", "r")
print(rhandler.readlines())
rhandler.close()

# writing file
file1 = open("test1.txt", "a")
file1.write("\nHello nice")
file1.close()

rhandler = open("test1.txt", "r")
print(rhandler.readlines())
rhandler.close()

