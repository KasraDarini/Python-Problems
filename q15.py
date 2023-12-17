number = (input())
maxP=int(number[0])
maxp =0
for i in range(len(number)) : 
    if maxP < int(number[i]):
        maxP = int(number[i])
        maxp= i
minP = int(number[0])
for i in range(len(number)) : 
    if minP > int(number[i]):
        minp = i
        minP = int(number[i])
print(minp+1 , ' ',maxp+1)