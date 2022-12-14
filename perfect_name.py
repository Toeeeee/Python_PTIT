import os 
import math
os.system('cls')

def songuyento (n) :
    if n < 2 : return 0
    for i in range(2,int(math.sqrt(n))) :
        if n % i == 0 : return 0 
    return 1
def dieukien(n) :
    s = 0
    S = 0 
    while n > 0 :
        x = n%10 
        if songuyento(x) == 0 : return 0 
        s = s + x 
        S = S*10 + x 
        n = int(n/10)
    if songuyento(s) == 1 and songuyento(S) == 1 : return 1
    return 0 

t = int(input())
while t > 0 : 
    t = t - 1 
    n = int(input())
    if songuyento(n) == 1 and dieukien(n) == 1 : print("Yes") 
    else : print("No")

