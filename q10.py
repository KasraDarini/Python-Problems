num =input()
numcopy= int(num) 
res='' 
for i in num : 
    if int(i) %2 !=0: 
        continue
    else :
        res +=i
if len(res) == 0: 
    print('no felan')
else : 
    print(res)