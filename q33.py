string=input()
res=0
Max =res
for i in string:
    if i == '0': 
        res +=1
    if Max < res : 
        Max = res
    if i =='1':
        res=0
print(Max)
