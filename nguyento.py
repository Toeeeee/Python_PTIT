import os 
import math 
os.system('cls')
def nguyento (n) : 
    if n < 2 : return 0 
    for i in range(2,int(math.sqrt(n)) + 1 ) : 
        if n % i == 0 : return 0 
    return 1 
t = int(input())
while t > 0 : 
    t = t - 1 
    n = int(input()) 
    dem = 0 
    for i in range(1,n) :
        if math.gcd(i,n) == 1 : 
            dem = dem + 1 
    if nguyento(dem) == 1 : print("YES")
    else : print("NO") 
