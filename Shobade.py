n =int(input())
res=1
for i in range(n):
    move1,move2 = map(int,(input().split()))
    if move1 ==res : 
        res=move2
    elif move2==res:
        res =move1
print(res)