a=15000 #int(input("enter current rent?  "))
b=10 #int(input("enter rate of increase per year  "))
c=50 #int(input("calculate current rent increase till?  "))
x=1
y= a*12
print ("annual rent = ",y)

while x<=c :
 z=(y*(b/100))
 print ("Annual  Rent Year", x, "=", y+z)
 print ("Monthly Rent Year", x, "=", (y+z)/12)
 x=x+1
 y=y+z
 
