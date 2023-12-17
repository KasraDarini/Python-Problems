import math
area_length = int(input())
area_width = int(input())
parket_length =int(input())
parket_width =int(input())
print(math.ceil((area_length * area_width) / (parket_length * parket_width)))