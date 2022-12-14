import os 
os.system('cls')
t = int(input()) 
while t > 0 : 
    t = t - 1 
    n = int(input())
    a = [int(x) for x in input().split()] 
    b = [int(x) for x in input().split()]
    a.sort() 
    b.sort() 
    kt = 1 
    for i in range(n) :
        if a[i] > b[i] : 
            kt = 0 
            print("NO")
            break 
    if kt == 1 : print('YES') 
    