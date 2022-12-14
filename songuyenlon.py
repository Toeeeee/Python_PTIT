import os
import math
os.system('cls')
t = int(input())
while t > 0 : 
    t-=1 
    a = int(input())
    b = int(input())
    print(math.gcd(a,b))
