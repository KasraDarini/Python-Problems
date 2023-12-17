n,m = map(int,(input().split()))
x=0
for i in range (n):
    for j in range(m): 
        if (i) % 2==0 and i !=0: 
            x = (i * m)+1 +j
        elif i ==0 : 
            x = 1 +j
        else : 
            x= (i+1)*m -j
        print(x,end=' ')
    print('')