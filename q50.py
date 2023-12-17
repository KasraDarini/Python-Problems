def YES_OR_NO(a,b):
    if len(a) != len(b):
        return 'NO'
    x = 0   
    listA = []
    for i in a:
        listA.append(i)
    listB=[]
    for i in b:
        listB.append(i)
    for i in listA:
        for j in listB:
            if i==j : 
                listB.remove(j)
                x+=1
                break
    if x == len(a):
        return 'YES'
    return 'NO'
n=int(input())
list1=[]
for i in range(n):
    a , b= map(str,(input().split())) 
    list1.append(YES_OR_NO(a,b))
for i in list1:
    print(i)    