N = int(input())
islow =False
Sum = 0
Max =0
for i in range(N): 
    L =int(input())
    if Max < L:
        Max =L
        Sum +=1
print(Sum)
