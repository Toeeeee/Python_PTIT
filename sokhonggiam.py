import os 
os.system('cls')
t = int(input()) 
while t > 0 : 
    s = input() 
    kt = 0 
    for i in range(1,len(s)) : 
        if s[i-1] > s[i]: 
            kt = 1 
            break
    if kt == 0 : print("YES")
    else : print("NO")
    t = t - 1