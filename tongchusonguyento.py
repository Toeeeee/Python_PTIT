import os 
import math 
os.system('cls')
t = int(input())
def tongchuso (s) : 
    S = 0 
    for i in s : 
        S = S + int(i)
    return S 
def nguyento (n) : 
    if n < 2 : return 0 
    for i in range(2,int(math.sqrt(n))+1) : 
        if n % i == 0 : return 0 
    return 1 

while t > 0 : 
    t = t - 1 
    s = input() 
    if nguyento(tongchuso(s)) == 1 : print("YES")
    else : print("NO")
