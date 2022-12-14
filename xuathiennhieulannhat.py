import os 
os.system('cls')
t = int(input())
while t > 0 : 
    t-=1
    n = int(input())
    a = [int(x) for x in input().split()]
    m = {}
    for i in a :
        if i in m : 
            m[i]+=1 
        else : 
            m[i] = 1 
    MIN = 1000006 ; j = -1000 
    for i in m : 
        if m[i] > j : 
            j = m[i] 
            MIN = i 
        elif m[i] == j : 
            MIN = min (i,MIN) 
    if j > n/2 : print(MIN)
    else : print("NO")

