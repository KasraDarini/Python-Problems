from cmath import log
n=int(input())
sum_n=0
for i in range(1,n): 
    if n % i ==0:
        sum_n+=i
ISAVAL =False
for i in range(sum_n):
    if pow(2,i)==sum_n:
        ISAVAL =True
        break
if ISAVAL : 
    print('1')
else:
    print('0')