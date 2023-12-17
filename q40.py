dict_0 = {} 
name_1 =input()
age_1=int(input())
dict_0[name_1] = age_1
name_2 =input()
age_2=int(input())
dict_0[name_2] = age_2
for k,v in dict_0.items():
    print(f"{k}'s age is {v}")
if age_1 > age_2 :
    print(f'{name_1} is {age_1 - age_2} year(s) older than {name_2}')
elif age_1 < age_2 :
    print(f'{name_2} is {age_2 - age_1} year(s) older that {name_1} ')