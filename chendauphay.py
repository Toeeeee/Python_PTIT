import os 
os.system('cls')
s = input()
x = ""
n = len(s)
dem = 0 
for i in range (n-1,-1,-1) : 
    x = x + s[i] 
    dem = dem + 1 
    if dem % 3 == 0 and i != 0 :
        x = x + "," 

for i in range(len(x)-1,-1,-1) : print(x[i],end='')

