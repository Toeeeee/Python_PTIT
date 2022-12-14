import os 
os.system('cls')
t = int(input()) 
while t > 0 :
    t = t - 1 
    [n , k] = [int(x) for x in input().split()] 
    list = [int(x) for x in input().split()] 
    for i in range(k,n) : 
        print(list[i], end = ' ') 
    for i in range(k) : 
        print(list[i], end = ' ') 
    print()   
    