import os 
os.system('cls')
def giaithua(n) : 
    s = 1 
    for i in range(1,n+1) :
        s = s*i 
    return s 
def tinh(n) : 
    return giaithua(n)/(2*giaithua(n-2)) 
n = int(input())
s = 0 
a = ['']*n 
for i in range(n) : 
    a[i] = input()
for i in range(n) : 
    dem = 0 
    for j in range(n) : 
        if a[i][j] == 'C' : dem += 1 
    s = s + tinh(dem) 
for i in range(n) : 
    dem = 0 
    for j in range(n) : 
        if a[j][i] == 'C' : dem += 1 
    s = s + tinh(dem) 
print(int(s))