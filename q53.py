def cal(list1):
    list2=[]
    for i in range(0,len(list1)-1):
        x = (list1[i] + list1[i+1])
        list2.append(x)
    list1 =list2
    list1.append(1)
    list2.insert(0,1)
    return list1
list_1 =[1,1]
n=int(input())
print(1)
for i in range(n-1):
    for i in list_1:
        print(i ,end=' ')
    print('')
    list_1 =cal(list_1)
