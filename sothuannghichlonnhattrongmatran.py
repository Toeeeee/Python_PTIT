
import os 
import math 
os.system('cls')
def sothuannghich (n) : 
    dem = 0 
    s = n 
    S = 0 
    while n > 0 : 
        x = n % 10 
        S = S*10 + x 
        dem = dem + 1 
        n = int(n/10)

    return s == S and dem >= 2 

[n,m] = [ int(x) for x in input().split()]
a = [0]*n 
for i in range(n) : 
    a[i] = [int(x) for x in input().split()]
dem = 0 
Max = -10000 
for i in range(n) : 
    for j in range (m) : 
        if sothuannghich(a[i][j] ) == 1 : 
            Max = max(Max,a[i][j]) 
            dem = dem + 1 
if dem == 0 : print ("NOT FOUND") 
else : 
    print (Max) 
    for i in range (n) : 
        for j in range(m) : 
            if a[i][j] == Max : 
                print ("Vi tri [", end = '') 
                print (i, end ='][' ) 
                print (j, end = ']\n') 

            

