def calculate_floor(string):
    res =0
    for i in string:
        if i =='D':
            res -=1
        else : 
            res+=1
    return res
string=input()
print(calculate_floor(string))