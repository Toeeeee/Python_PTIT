import os
os.system('cls')
t = int(input())
while t > 0 : 
    t = t - 1 
    s = input() 
    dem = 0 
    demsochan = 0 
    tong = 0 
    tich = 1 
    for i in range(len(s)) : 
        if i % 2 != 0 : tong = tong + int(s[i]) 
        else :  
            demsochan = demsochan + 1 
            if s[i] == '0' : dem = dem + 1 
            else : tich = tich * int(s[i]) 
    if dem == demsochan : print("0", end = ' ') 
    else : print(tich, end = ' ') 
    print (tong)