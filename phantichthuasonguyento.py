import os 
os.system('cls')
import math

def phantich (n) :
    print ("1", end=' ')
    for i in range(2,int(math.sqrt(n))+1) :
        dem = 0 
        while n % i == 0 :
            dem = dem + 1 
            n = n/i
        if dem > 0 : 
            print (" * ", end='')
            print(i, end='^')
            print(dem,end='') 
    if n > 1 :
        print (" * ", end='')
        print (int(n),end='^1') 
    print ()

t = int(input()) 
while t > 0 : 
    t = t - 1 
    n = int(input())
    phantich(n)
