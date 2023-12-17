N =int(input())
num_of_non_prime =0
sum_of_prime= 0
for i in range(N):
    x = int(input())
    is_prime =True
    if x==1 :
        num_of_non_prime+=1
        continue
    for j in range(2,x//2+1):
        if x % j==0 and x!=2:
            is_prime =False
    if is_prime :
        sum_of_prime +=x
    if is_prime ==False:
        num_of_non_prime+=1
print(f"Number of non-prime :{num_of_non_prime}")
print(f'Sum of prime numbers:{sum_of_prime}')