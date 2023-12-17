a , b  = map(int,(input().split()))
for i in range(a):  
    print(' ',end='')
    print('_ ' * b)
    print('| '* (b+1))
print(' ',end='')
print('_ ' * b)
