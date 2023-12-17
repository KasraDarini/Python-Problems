n =int(input())
Sum =0 
for i in range(1,n+1) : 
    x = int(input())
    Sum += (2/pow(2,i)) * x
print(Sum / n)