import os 
os.system('cls')
t = int(input())
while t > 0 : 
    t = t - 1 
    s = input()
    s = s + " " 
    dem = 1 
    for i in range(1,len(s)) :
        if s[i] == s[i-1] : dem = dem + 1
        else :
            print (dem,end='')
            print (s[i-1],end='') 
            dem = 1 
    print() 
