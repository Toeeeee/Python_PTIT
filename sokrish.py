import os 
os.system('cls')
def giaithua (n) :
    s = 1 
    for i in range(1,n+1) : s = s*i
    return s 
def tinh(n) :
    s = 0 
    while n > 0 :
        x = n%10 
        s = s + giaithua(x) 
        n = int(n/10)
    return s 
t = int(input())
while t > 0 : 
    t = t - 1 
    n = int(input()) 
    if tinh(n) == n : print ("Yes")
    else : print("No")
