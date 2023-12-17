x,y = map(int,(input().split()))
l = int(input())
x1,y1 = map(int,(input().split()))
inner = True
if x1 < x or x1 > x + l :
    inner = False
if y1 > y or y1 <y-l : 
    inner =False
if inner==True:
    print('Mahdi')
else :
    print('Parsa')