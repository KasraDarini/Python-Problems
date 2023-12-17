number = int(input())
res = number %10
while number > 0 : 
    if res < number %10:
        res = number%10
    number //=10
print(res)