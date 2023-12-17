from cmath import sqrt
a =float(input())
b =float(input())
c =float(input())
delta = b**2 - 4*a*c
if( delta < 0 ):
    print("NO ROOT")
elif(delta ==0):
    print(round(-b/(2*a), 2))
elif (delta >0):
    root1 = (-b + sqrt(delta))/(2*a)
    root2 = (-b - sqrt(delta))/(2*a)
    Roots = "{Root1:.2f} and {Root2:.2f}"
    print(Roots.format(Root1=root1,Root2=root2))
