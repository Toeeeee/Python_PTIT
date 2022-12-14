import os 
os.system('cls')
import math

def songuyento(n):
    if n < 2 : return 0 
    for i in range (2,int(math.sqrt(n)) + 1 ) :
        if ( n % i == 0 ) : return 0 
    return 1 

def tongcs (n) :
    s = 0 
    while n > 0 :
        t = int(n%10)
        s = s + t 
        n = int(n/10) 
    return s

t = int(input())
while t > 0 :
    t = t - 1 
    a,b  = map(int,input().split())  
    x = int(math.gcd(a,b))
    if songuyento(tongcs(x)) == 1 : print("YES")
    else : print("NO") 

