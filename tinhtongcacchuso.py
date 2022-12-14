import os 
os.system('cls')

t = int(input())
while t > 0 : 
    t = t - 1 
    s = input() 
    S = 0
    b = [] 
    for i in range (len(s) ) : 
        if s[i] <= '9' and s[i] >= '0' :  S = S + int(s[i]) 
        else : 
            b.append(s[i]) 
    b.sort() 
    for i in range (len(b) ) : 
        print(b[i], end= '') 
    print(S) 