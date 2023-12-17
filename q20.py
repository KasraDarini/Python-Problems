t = int(input())
for i in range(t): 
    res=0
    x=int(input())
    for j in range(x): 
        a , b= map(str,(input().split()))
        if res==0 : 
            if a == 'buy_one' or b =='buy_one':
                res +=1
            else : 
                res =0
        elif res > 0 : 
            if a =='copy_paste' or b == 'copy_paste':
                res +=res
            else : 
                res +=1
    print(res)