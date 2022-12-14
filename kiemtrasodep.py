import os 
os.system('cls')
t = int(input())
def sodep (s) : 
    a = set()
    for i in range(len(s)) : 
        a.add(s[i]) 

    if len(a) != 2 : return 0 
    x = s[0] ; y = s[1] 
    for i in range(len(s)) :
        if i % 2 == 0 : 
            if s[i] != x : return 0 
        else : 
            if s[i] != y : return 0 
    return 1 

while t > 0 : 
    t-=1 
    s = input()
    if sodep(s) == 1 : print("YES")
    else : print("NO")
