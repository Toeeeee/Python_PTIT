import os 
import math 
os.system('cls')

def souocso(n) : 
    dem = 0 
    us = 1 
    while n % 2 == 0: 
        dem+=1 
        n = int(n/2) 
    us = us*(dem+1) 
    if us > 9 : return 0 
    for i in range(3,int(math.sqrt(n)+1), 2 ): 
        dem = 0 
        while n % i == 0 : 
            dem+=1 
            n = int(n/i) 
        us = us*(dem+1) 
        if us > 9 : return 0 
    if n > 1 : us = us*2
    if us == 9 : 
        return 1 
    return 0  

t = int(input()) 
dem = 0 
for i in range(1,t+1): 
    if souocso(i) == 1 : 
        dem+=1 
print(dem)
