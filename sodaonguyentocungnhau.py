import os 
os.system('cls')
import math

def sodao (n) :
    s = 0 
    while n > 0 :
        t = int(n%10)
        s = s*10 + t 
        n = int(n/10) 
    return s 

t = int(input()) 
while t > 0 : 
    t = t- 1 
    n = int( input()) 
    x = sodao(n)
    if math.gcd(x,n) == 1 : print("YES")
    else : print("NO")
