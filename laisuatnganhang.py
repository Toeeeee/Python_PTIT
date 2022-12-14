import os 
import math 
os.system('cls')
t = int(input()) 
while t > 0 : 
    t -= 1 
    n,x,m = [float(x) for x in input().split()] 
    x = x /100 
    r = math.log(m/n, 1 + x ) 
    if r != int(r) : print(int(r)+1)
    else : print(int(r))
