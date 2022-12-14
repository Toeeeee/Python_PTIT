import os 
os.system('cls')
t = int(input())
def ktra (s) : 
    if len(s) % 2 == 0 : return 0 
    if s[0] == s[1] : return 0 
    for i in range(2,len(s),2) : 
        if s[i-2] != s[i] : return 0 
    return 1 

while t > 0 : 
    t = t- 1 
    s = input() 
    if ktra(s) == 1 : print("YES")
    else : print("NO")
