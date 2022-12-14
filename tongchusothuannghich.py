import os 
os.system('cls')
def tongchuso (s) :
    S = 0 
    for i in s : 
        S = S + int(i) 
    return S 
def sothuannghich (n) :
    s = n 
    S = 0 
    dem = 0 

    while n > 0 : 
        x = n % 10 
        dem = dem + 1 
        S = S*10 + x 
        n = int(n/10)
    if dem > 1 and s == S : return 1 
    return 0    
t = int(input())
while t > 0 : 
    t = t - 1 
    s = input() 
    if sothuannghich(tongchuso(s)) == 1 : print("YES")
    else : print("NO")
