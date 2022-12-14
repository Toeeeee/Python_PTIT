import os 
os.system('cls')
m = {} 
for i in range(5) : 
    x = int(input())
    m[x] = 1 
m = sorted(m.items(), key = lambda x : x[0] ) 
for i in m : 
    print(i[0] , i[1])