a = float(input())
b = float(input())
res = False
if abs((a+b)/a - (a/b)) <= 0.05  : 
    res =True
print(res)