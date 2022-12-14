
import os 
os.system('cls') 

n = float(input())
a = [float(x) for x in input().split()] 
a.sort() 
min = a[0] 
max = a[len(a) - 1]
dem = 0 ; s = 0 
for i in a : 
    if i != min and i != max : 
        dem += 1 
        s = s + i 

x = s/dem 
print(round(x,2)) 
