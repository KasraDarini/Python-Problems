n = int(input())
seq = 9
res =0 
addition = 0
for i in range(n):
    res += seq
    seq = (abs(seq) *10) + 9
    if i %2==0 : 
        seq *=-1
    print(seq)

print (f'result is {res}')