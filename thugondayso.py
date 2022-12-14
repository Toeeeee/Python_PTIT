import os 
os.system('cls')
n = int(input())
a = [int(x) for x in input().split()]
dem = 0 
i = 0 
while i < n - 1 : 
    if (a[i] + a[i+1] ) % 2 == 0 : 
        i = i + 1 
    else: dem = dem + 1 
    i = i + 1 
prin(dem) 




