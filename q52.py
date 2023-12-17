string = input()
list_1 = string.split(' ')
num = int(list_1[0])
mabna = int(list_1[1])
str1= ''
dict1= {'10' : 'A' , '11' :'B', '12':'C', '13':'D', '14':'E','15':'F','16':'G','17':'H','18':'I','19':'J','20':'K'}
while num > 0 :
    if num % mabna >=10:
        str1+=dict1[str(num%mabna)]
    else : 
        str1+=str(num%mabna)
    num //=mabna
print(str1[len(str1)-1 : 0:-1] + str1[0])