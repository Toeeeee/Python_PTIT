import os 
os.system('cls')
n = int(input())
list = [int(x) for x in input().split()] 
dem = 0 
for i in range(1,n) : 
    if ( list[i-1] != list[i] ) : dem = dem + 1 
print (dem ) 