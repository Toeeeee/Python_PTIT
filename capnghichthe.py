import os 
os.system('cls')
n = int(input())
a = [int(x) for x in input().split()]
dem = 0 
for i in range(n-1) : 
    for j in range(i+1,n):
        if a[i] > a[j] : dem = dem + 1 
print(dem) 