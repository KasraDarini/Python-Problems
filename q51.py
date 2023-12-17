n =int(input())
lst=[]
for i in range(n):
    lst.append(int(input()))
res=0
for i in range(len(lst)-1):
    if lst[i] != lst[i+1]:
        res+=1
print(res)