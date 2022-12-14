import os 
os.system('cls') 
t = int(input()) 
while t > 0 : 
    t = t - 1 
    s = input() 
    for i in range(len(s)) : 
        if i % 2 == 0 : x = s[i] 
        else : 
            for j in range(int(s[i])) : print(x, end='') 
    print('') 