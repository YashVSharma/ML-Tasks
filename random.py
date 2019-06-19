import numpy as np
import re
x=int(input("enter no of rows: "))
y=int(input("enter no of columns"))
a=np.random.rand(x,y)
print(a)


for i in a:
  f=open("a.txt","w+")
  f.write(str(i))


