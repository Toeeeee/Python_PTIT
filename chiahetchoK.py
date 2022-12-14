import os 
os.system('cls') 
a,k,n = [int(x) for x in input().split()]
dem = 0 
x = int(n/k) 
for i in range(1,x+1) :
    y = i*k - a 
    if y > 0 : 
        dem+=1
        print (y,end = ' ')
if dem == 0 : print("-1")