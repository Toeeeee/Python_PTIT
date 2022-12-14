import os 
import math 
os.system('cls')
t = int(input())
def nguyento(n) : 
    if n < 2 : return 0 
    for i in range(2, int(math.sqrt(n)) + 1 ) : 
        if n % i == 0 : return 0 
    return 1 
while t > 0 : 
    t = t - 1 
    s = input()
    dem = 0 
    for i in range(len(s)) : 
        if nguyento(int(s[i])) == 1 : dem = dem + 1 
    if nguyento(len(s)) == 1 and dem > len(s) - dem : 
        print("YES")
    else : 
        print("NO") 
        
