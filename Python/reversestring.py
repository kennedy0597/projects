str1=input("Enter a string: ")

length=len(str1)
reversedstr=[]

while length>0:
    reversedstr += str1[length-1]
    length= int(length)-1

reversedstr = ''.join(reversedstr)
print(reversedstr)


print(str1[::-1])