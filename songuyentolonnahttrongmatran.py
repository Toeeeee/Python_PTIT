
import os 
import math 
os.system('cls')
def nguyento (n) : 
    if n < 2 : return 0 
    for i in range(2,int(math.sqrt(n))+ 1 ) : 
        if n % i == 0 : return 0 
    return 1 

[n,m] = [ int(x) for x in input().split()]
a = [0]*n 
for i in range(n) : 
    a[i] = [int(x) for x in input().split()]
dem = 0 
Max = -10000 
for i in range(n) : 
    for j in range (m) : 
        if nguyento(a[i][j] ) == 1 : 
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

            

