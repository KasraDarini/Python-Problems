loop , length  = map(int,(input().split()))
n= int(input())
t,v = map(int,(input().split()))
second = t + loop*length/v
mini =1
for i in range(n-1): 
    t,v = map(int,(input().split()))
    if second > t + length*loop/v:
        mini= i +2
        second = t + length*loop/v
print(mini)
