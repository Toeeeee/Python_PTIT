import os
os.system('cls') 

t = int(input()) 

while t > 0 : 
    s = input()
    kt = 0 
    for i in s : 
        if i != '7' and i != '4' : 
            kt = 1 
            break 
    if ( kt == 0 ):  print("YES") 
    else : print("NO")
    t = t - 1 
     