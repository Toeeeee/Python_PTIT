import os 
os.system('cls')
n,m = [int(x) for x in input().split()]
a = [0]*n 
for i in range(n) : 
    a[i] = [int(x) for x in input().split()] 
Max = -10000000 ; Min = 10000000 
for i in range(n) : 
    for j in range(m) : 
        Max = max(Max,a[i][j])
        Min = min(Min,a[i][j])

S = Max - Min 

kt = 0 
k = 0 
for i in range(n) : 
    for j in range(m) : 
        if  a[i][j] == S : 
            if k == 0 : 
                print(S)
                k+=1
            kt = 1 
            print(f"Vi tri [{i}][{j}]") 

if kt == 0 : print("NOT FOUND")

