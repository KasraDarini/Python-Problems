a = int(input())
b = int(input())
res =1
for i in range(a,b+1):
    boolean = True 
    if i == 1 :
        continue
    for j in range(2,i //2 +1):
        if(i % j ==0):
            boolean = False
    if(boolean == True) : 
        print(i, end=',')
print(chr(8),chr(8))