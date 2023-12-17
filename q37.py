import math
T=int(input())
for i in range(T):
    m , t , b = map(int,(input().split()))
    print(math.ceil(((m/t) * b) /8),(math.ceil(((m/t) * b) /8))*8-((math.floor(m/t))*(b-1)))