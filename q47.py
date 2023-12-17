is_played =''
while is_played.upper() !='Q':
    n =int(input())
    m =int(input())
    is_played = input()
    for i in range(1,n+1) :
        for j in range(1,n+1):
            if i*j % m==0:
                print('H',end=' ')
            elif i*j < 10:
                print(i*j,end= ' ')
            elif i*j > 10 :
                print(i*j, end='')
            if j != n : 
                print(' ',end='')
            else :
                print('')