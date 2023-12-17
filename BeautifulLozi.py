s= (input())
f=(input())
Len = ord(s) - ord(f)
for i in range(0,Len):
    print((Len - i-1) * ' ',end='')
    x =i 
    res=''
    while x >=  0 : 
        res+=chr(ord(f)+x)+' '
        x -=1

    print(res[len(res) -1 : 0 : -1] ,end='')
    print(res[0])

for i in range(ord(f) , ord(s)+1):
    print(chr(i),end=' ')

print('\n',end='')

for i in range(Len-1 , 0 ,-1):
    print((Len -i-1 ) * ' ',end='')
    x =i
    res=''
    while x >=  0 : 
        res+=chr(ord(f)+x)+' '
        x -=1
    print(res[len(res) -1 : 0 : -1] ,end='')
    print(res[0])
print((Len-1)*' ', f)