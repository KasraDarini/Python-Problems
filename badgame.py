import random
x =random.randrange(1, 101)
f=x
print(f)
n = int(input("ENTER YOUR GUESSED NUMBER:"))

while(n !=f):
    for i in range (101):
        if(i==n):
            print('',end ='')
        if(i !=n and i%10 !=0):
            print(i,end=' ')
        if(i %10 ==0):
            print(i,end='\n')
    n=int(input())
    
print("\n*********************YOU WON***********************")