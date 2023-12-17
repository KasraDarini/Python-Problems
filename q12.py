n = int(input())
m = int(input())
res=n
while n>=m:
    n -=m
    res += 1
    n +=1

print(res)

