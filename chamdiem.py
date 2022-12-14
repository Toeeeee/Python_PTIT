import os 
os.system('cls')
n = int(input())
a = [int (x) for x in input().split()] 
k = 0 
s = sum(a) 
MAX = -1000 ; t = 0 
while k < n - 2: 
    k+=1
    s = s - a[k-1] 
    b=a[k:]
    b.sort()
    S = s - b[0] 
    if MAX < S/(n-k-1) : 
        MAX = S/(n-k-1)
        t = k 
print (t)
