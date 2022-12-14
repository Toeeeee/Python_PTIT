import os 
os.system('cls')
t = int(input()) 
while t > 0 : 
    t-=1 
    n = int(input()) 
    if n == 1 : print('2')
    else : 
        f = 2 
        for i in range(2,n+1) : 
            f = f + 2**(i-2) 
        print(f) 