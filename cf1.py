num = int(input())
sum=0
i=1 
j=1
for i in range(num ):
    a , b , c = map(int,(input().split()))
    sum += a+b+c
if(sum ==0):
    print('Yes'.upper())
else:
    print("NO")
