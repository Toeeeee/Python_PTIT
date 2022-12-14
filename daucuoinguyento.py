import os 
import math 
os.system('cls')
t = int(input()) 
def nguyento (n) : 
    if n < 2 : return 0 
    for i in range(2,int(math.sqrt(n))+ 1 ) :
        if n % i == 0 : return 0 
    return 1 
while t > 0 : 
    t = t - 1 
    s = input() 
    S1 = 0 
    S2 = 0
    for i in range(0,3) :
        S1 = S1*10 + int(s[i])
    for i in range(len(s)-3,len(s)) :
        S2 = S2*10 + int(s[i]) 
    if nguyento(S1) == 1 and nguyento(S2) == 1 : print("YES")
    else : print("NO") 

