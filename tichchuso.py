import os 
os.system('cls')
t = int(input())
while t > 0 : 
    t = t - 1 
    s = input() 
    S = 1 
    for i in range(len(s)) : 
        if s[i] != '0' : S = S*int(s[i]) 
    print(S) 