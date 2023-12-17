x1 , y1= map(int,(input().split()))
x2 , y2= map(int,(input().split()))
x3 , y3= map(int,(input().split()))
x4 , y4= map(int,(input().split()))
res=0
if(x1 == x3 or x1==x4) :
    res +=1
elif y1==y3 or y1==y4:
    res=res+1
if x2 == x3 or x2==x4:
    res +=1
elif y2==y3 or y2==y4: 
    res+=1
if res==1 : 
    print('happy')
else:
    print('unhappy')