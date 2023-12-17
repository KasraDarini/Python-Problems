n =int(input())
str_1 = input()
str_2 = input()
dif=0
for i in range(n):
    if str_1[i] != str_2[i]:
        dif +=1
if dif %2 ==0 : 
    print(dif //2)
else:
    print('NO')
