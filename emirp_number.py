import os 
import math
os.system('cls')

def songuyento (n) :
    if n < 2 : return 0
    for i in range(2,int(math.sqrt(n)+1)) :
        if n % i == 0 : return 0 
    return 1

def dieukien(n, N) :
    S = 0 
    s = n 
    while n > 0 :
        x = n%10 
        S = S*10 + x 
        n = int(n/10)
    if songuyento(S) == 1 and S > s and S < N : print (s,S, end=' ') 

t = int(input())
while t > 0 : 
    n = int(input())
    for i in range (11,n) :
        if songuyento(i) == 1 and dieukien(i,n) == 1 : pass 
    print()
    t = t - 1 
