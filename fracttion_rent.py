a=int(input("enter current rent?  "))
b=int(input("enter rate of increase per year  "))
c=int(input("calculate current rent increase till?  "))
x=1
y= a*12
print ("annual rent = ",y)

while x<=c :
 z=(y*(b/100))
 print ("Year", x, "=", y+z)
 x=x+1
 y=y+z
