import os 
import math 
os.system('cls')
def kiemtra (a,b,c) : 
    if  math.gcd(a,b) == 1 and math.gcd(b,c) == 1  and math.gcd(c,a) == 1  : return 1 
    return 0 

[l,r] = [ int(x) for x in input().split()] 
for i in range(l,r-1) : 
    for j in range(i+1,r) : 
        for k in range(j+1,r+1) : 
            if kiemtra(i,j,k) == 1 : 
                print ("(", end = '' ) 
                print(i,end = ', ' )
                print(j,end = ', ')
                print(k, end = ')\n' )
                
 