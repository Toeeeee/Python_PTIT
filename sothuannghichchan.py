import os 
os.system('cls')
def dieukien (n) :
    S = 0 
    s = n 
    dem = 0 
    while n > 0 : 
        x = n %10
        if x % 2 != 0 : return 0 
        dem = dem + 1 
        S = S*10 + x 
        n = int(n/10) 
    if S == s and dem % 2 == 0 : return 1 
    return 0
t = int(input()) 
while t > 0 : 
    t = t - 1 
    n = int(input())
    for i in range(22,n+1) : 
        if dieukien(i) == 1 :  print(i,end=' ') 
    print()
