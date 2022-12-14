import os 
os.system('cls')
t = int(input())
while t > 0 : 
    t-=1 
    n = int(input())
    m = {}
    while n > 0 :
        n-=1  
        x = int(input())
        if x in m :
            m[x]+= 1 
        else :
            m[x] = 1 
    MIN = 1005 ; j = -1005
    for i in m : 
        if m[i] > j : 
            MIN = i 
            j = m[i] 
        elif m[i] == j :
            MIN = min(i, MIN)
    print(MIN)
