import os 
os.system('cls')
def bangnhau (a,n) : 
    for i in range(1,n) : 
        if a[i-1] != a[i] : return 0 
    return 1 
while True : 
    n = int(input())
    if n == 0 : break 
    a = [] 
    Max = -10000000 ; Min = 10000000 
    for i in range(n): 
        a.append(int(input()))
    for i in a: 
        Max = max(Max,i) 
        Min = min(Min,i)

    if bangnhau(a,n) == 1 : print("BANG NHAU")
    else :
        print (Min,Max) 
     