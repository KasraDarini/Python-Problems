Cm,Gm= map(int,(input().split()))
Cs,Gs= map(int,(input().split()))
rate= int(input())
res1 = Gm *rate + Cm
res2 = Gs*rate + Cs
if res1 >= res2 : 
    print('Yes')
else : 
    print('No')