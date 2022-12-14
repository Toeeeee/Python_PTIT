import os 
os.system('cls')
import math 

n,k = map(int, input().split())
dem = 0 
for i in range(pow(10,k-1),pow(10,k)) : 
    if math.gcd(i,n) == 1 :
        dem = dem + 1 
        print(i,end=' ')
        if dem % 10 == 0 : print('')