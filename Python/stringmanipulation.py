string_value="Everything in python is an object"
print("string length is ",len(string_value))
print(string_value, "length is ",len(string_value))
print('string length of "%s"' %string_value ,len(string_value))

a="cats"
b="dogs"
print("I love %s and %s" %(a,b))

c="cakes"
print("I love {c}".format(c="cakes"))
print("I love {c}".format(c=input("what is your favourite food?")))

##concatenation

print(a+b)
z=a+b
print(z)

#split

testString="This is a test string"
result=testString.split('t')
print(result)
print("on splitting %s based on 't' is %s" %(testString,result))

#slicing 

print("Slicing %s by 6 letters: is" %string_value, string_value[0:6])
print(string_value.count('e'))
print(string_value.split(' '))

#striding
stringValue=string_value[::-1]
print(stringValue)
stringValue=" ".join(stringValue[::-1])
print(stringValue)

#Arithmetic operations on string
print(a+b)
print('^'*25)


origPrice=float(input("enter original price: $"))
discount=float(input("enter discount %: "))
newprice=(1-discount/100)*origPrice
print(origPrice, "discounted by" , discount,"%" ,"is", newprice )
print('${} discounted by {}% is ${}.'.format(origPrice, discount, newprice))
