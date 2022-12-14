import os 
os.system('cls')
def tongcs (n) :
    s = 0 
    while n > 0 : 
        x = int(n%10)
        s = s + x 
        n = int(n/10)
    return s 
def chuso (n) : 
    n1 = int(n%10) 
    n = n / 10
    while n > 0 : 
        n2 = int(n%10) 
        if abs(n2-n1) != 2 : return 0 
        n = int(n / 10) 
        n1 = n2 
    return 1 
t = int(input()) 
while t > 0 : 
    t = t - 1 
    n = int(input())
    if  chuso(n) == 1 and tongcs(n) % 10 == 0  : print("YES") 
    else : print("NO")