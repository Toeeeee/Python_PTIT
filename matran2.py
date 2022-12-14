import os 
os.system('cls')
n = int(input())
a = [0]*(n+1)  
for i in range(n): 
    a[i] = [int(x) for x in input().split()] 
k = int(input())
S = 0 
for i in range(n) : 
    for j in range(n) : 
        if j > n - i - 1:
            S = S + a[i][j] 
s = 0 
for i in range(n) : 
    for j in range(n) : 
        if j < n - i - 1:
            s = s + a[i][j] 
if abs(S-s) <= k : print("YES") 
else : print("NO")
print(abs(S-s))


