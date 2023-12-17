n = int(input())
nplus = int(input())
n2 = (nplus % 7 )+n
if(n2 == 1):
    print("sunday")
if(n2 == 2):
    print("monday")
if(n2 == 3):
    print("thursday")
if(n2 == 4):
    print("wendesday")
if(n2 == 5):
    print("thursday")
if(n2 == 6):
    print("friday")
if(n2 == 7):
    print("saturday")