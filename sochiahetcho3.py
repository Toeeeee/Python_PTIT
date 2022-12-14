import os 
os.system('cls')
t = int(input())
while t > 0 : 
    t = t - 1 
    s = input() 
    S = 0 
    for i in s : 
        S = S + int(i) 
    if S % 3 == 0 : print("YES") 
    else : print("NO")