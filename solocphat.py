import os 
os.system('cls')

t = int(input())
while t > 0 : 
    t = t - 1 
    s = input() 
    n = len(s) 
    if  s[n-2] == '8' and s[n-1] == '6' : print("YES") 
    else : print("NO") 