# cook your dish here
sum =0
n =int(input())
for i in range(n): 
    for j in range(3):
        x=int(input())
        if j ==2 : 
            print(sum % x)
        else: 
            sum +=x