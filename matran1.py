import os 
os.system('cls')
n = int(input()) 
a = [0]*n 
for i in range(n) : 
    a[i] = [ int(x) for x in input().split()] 
k = int (input())
S1 = 0 
S2 = 0 
for i in range(n) : 
    for j in range(n) : 
        if i < j : S2 = S2 + a[i][j] 
        elif i > j : S1 = S1 + a[i][j] 
    
if abs(S2 - S1 ) <= k : print ("YES")
else : print("NO")

print (abs(S2-S1)) 
