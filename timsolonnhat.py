import os
os.system('cls')
t = int(input())
while t > 0 : 
    t = t - 1 
    s = input() 
    s = s + " " 
    max = -1  
    S = 0
    for i in range(0,len(s)) : 
        if s[i] <= '9' and s[i] >= '0' : 
            S = S*10 + int(s[i])
            if s[i+1] > '9' or s[i+1] < '0' :
                if max < S : max = S 
        else : S = 0 
    print(max)
           


