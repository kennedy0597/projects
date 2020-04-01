i=2
while (i<100):
    j=2
    while(j<=i/j):
        if not (i%j): break
        j=j+1
    if (j>i/j): print(i,"is prime")
    i+=1

x=1
while True:
  print(x)
  x=x+1
  if x>20:
      break

for x in range(100):
    if(x%2)==0:
        continue
    print(x)