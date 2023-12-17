def armstrong(n):
    sum_ =0
    x= int(n)
    while x > 0 : 
        sum_ += (x %10) ** len(n)
        x//=10
    if sum_ == int(n):
        return True
    return False
num=input()
print(armstrong(num))