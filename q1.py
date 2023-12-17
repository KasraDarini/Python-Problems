a = int(input())
b = int(input())
c= int(input())
a1 = a/100 
a2 = a %100 
b1 = b/100
b2 = b%100
c1 = c/100
c2= c%100
x =((a1*a2) + (b1*b2) + (c1*c2) )/ (a1 + b1 + c1)
print(round(x,4))