number = int(input())
list = [number %10 , (number/(10)) %10 ,(number/(100)) %10,(number/(1000)) %10 ]
res=1
x=1
for x in range(3): 
    boolean = False
    for y in range(x+1,5):
        if(list[x-1] == list[y-1]):
            boolean =True
    if(boolean== False):
        res = list[x-1]
        print(x)
        break
print(res)

