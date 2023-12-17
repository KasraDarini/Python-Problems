n,a , b , c ,d= map(int,(input().split()))
res=0
for i in range(1,n+1):
    if i %a ==0 or i %b ==0 or i %c ==0 or i %d ==0:
        res+=1
print(res,end='')