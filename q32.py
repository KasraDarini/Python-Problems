n =int(input())
list1=[]
for i in range(n): 
    a , b= map(str,(input().split()))
    list1.append(a)
    list1.append(b)
index =1
for i in range(1,len(list1),2):
    if int(list1[i]) > int(list1[index]):
        index =i
print(list1[index-1])

