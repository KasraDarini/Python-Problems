c= int(input())
h = int(input())
o = int(input())
m  =int(input())
if m % (c*12 + h*1 + o*16) !=0:
    print('Not Valid!')
else : 
    zarib = m // (c*12 + h*1 + o*16)
    print(f'C{c*zarib}H{h*zarib}O{zarib*o}')