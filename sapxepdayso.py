import os 
os.system('cls')
t = int(input())
while t > 0 : 
    t = t- 1 
    [n,k] = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    Max = -10000 
    kt = 0 
    for i in range(n) : 
        Max = max(Max,a[i]) 
    
    for i in range (n) : 
        if a[i] < 0 :
            if a[i] == Max and kt == 0 : 
                print (k,end = ' ')
                kt = kt + 1 
            print(a[i],end=' ')
    for i in range(n) : 
        if a[i] >= 0 : 
            if a[i] == Max and kt == 0 : 
                print (k,end = ' ')
                kt = kt + 1 
            print(a[i], end = ' ')
    print()