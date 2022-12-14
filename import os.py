import os 
import math 
os.system('cls')
t = int(input())
def nguyento (n) :
    if n < 2 : return 0 
    for i in range(2,int(math.sqrt(n))+1) :
        if n % i == 0 : return 0 
    return 1 
def tongchuso (s) :
    S = 0 
    for i in s : 
        S = S + int(i) 
    return S
def ktra(s) :
    if nguyento(tongchuso(s)) == 0 : return 0 
    for i in range(0,len(s)) :
        x = int(s[i])  
        if i % 2 == 0 : 
            if x % 2 != 0 : return 0 
        else :
            if x % 2 == 0 : return 0 
    return 1 
while t > 0 : 
    t = t - 1 
    s = input() 
    if ktra(s) == 1 : print("YES")
    else : print("NO")

