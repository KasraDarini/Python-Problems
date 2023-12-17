n = int(input())
if n %2 ==0 : 
    for i in range(n):
        print((n-i) * '*',end='')
        print(' ' * 2 * i,end='')
        print((n-i) * '*')
    for i in range(2,n+1):
        print(i * '*',end= '')
        print((n - i) * ' ' *2 ,end='')
        print(i * '*')
else : 
    for i in range(n):
        print((n-i) * '*',end='')
        print(' ' * 2 * i,end='')
        print((n-i) * '*')
    for i in range(1,n):
        print(i * '*',end= '')
        print((n - i) * ' ' *2 ,end='')
        print(i * '*')

#BEAUTY