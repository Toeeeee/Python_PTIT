import os 
os.system('cls')
n = int(input()) 
a = [int(x) for x in input().split()]  
m = {} 
a.sort() 
for i in a : 
    m[i] = 1 
kt = 1 
for i in range(1,a[len(a)-1] + 1) : 
    if i not in m : 
        print(i) 
        kt = 0 
        break 
if kt == 1 : 
    print(n+1) 

