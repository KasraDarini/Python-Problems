sec = int(input())
days = sec // (3600*24)
hours =(sec // (3600)) - (days *24)
minutes =  (sec // (60)) - ((hours + (days*24)) * 60)
list_0= [days , hours , minutes,sec%60]
for i in range(len(list_0)) : 
    if list_0[i] < 10 and i!= 0 : 
        print(f"0{list_0[i]}",end='')
    else :
        print(list_0[i],end='')
    if i !=3 :
        print(':',end='')