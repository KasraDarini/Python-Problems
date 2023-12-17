t =int(input())
for i in range(t):
    string=input()
    starting_index=0
    for i in range(len(string)):
        if string[i] =='0':
            starting_index =i
            break
    result =0
    for i in range(starting_index,len(string)):
        if string[i] == '1' and string[i -1]=='0':
            result+=1

    if string[len(string)-1] =='0':
        result+=1
    print(result)