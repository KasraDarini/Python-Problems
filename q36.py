T=int(input())
for i in range(T):
    a , b , c = map(int,(input().split()))
    print(b*a + c*(a-1))