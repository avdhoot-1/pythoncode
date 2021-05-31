a =input('what was the purchase price?  ')
b =input('what was the sale price ?     ')
c = float(b) - int(a)
if c>0:
  print ('net profit was', c)
else: print ('net loss was',c) 

d = ((float(c)/float(a))*100)

print ('percent gain /loss was',d)

x =input('what was the investment amount  ')
y =(float(d)*(float(x))/100)
if (float (y) > float (x)):
    print ("you would have ",int(y)+int(x)) 
else: 
    print ("you would have ",int(y) + int(x))



