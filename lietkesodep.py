import os 
os.system('cls')
t = int(input())
def dieukien (n) : 
    s = str(n) 
    if len(s) % 2 == 1 : return 0 
    S = s[::-1] 
    if s != S : return 0 
    for i in range(len(s) ) : 
        if int(s[i]) % 2 == 1 : return 0 
    return 1 

while t > 0 : 
    t = t - 1 
    n = int(input())
    for i in range(1,n) : 
        if dieukien(i) == 1 : print(i, end = ' ') 
    print()
