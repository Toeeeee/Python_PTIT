import os 
import math
os.system('cls')
t = int(input())
def songuyento (n) :
    if n < 2 : return 0 
    for i in range(2,int(math.sqrt(n))) :
        if n % i == 0 : return 0 
    return 1 
def dieukien (s) : 
    n = len(s) 
    if songuyento(n) == 0 : return 0 
    dem = 0 
    for i in s :
        if i != '2' and i != '3' and i != '5' and i != '7' : dem = dem + 1 
    if n - dem > dem : return 1 
    return 0 
while t > 0 : 
    t = t - 1 
    s = input()
    if dieukien(s) == 1 : print("YES")
    else : print("NO")
    

