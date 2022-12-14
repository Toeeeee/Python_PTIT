import os 
os.system('cls')
t = int(input())
list = [] 
list.append(0) 
list.append(1) 
for i in range(2,93) : 
    list.append(list[i-2] + list[i-1] )  

while t > 0 : 
    t = t - 1 
    [a,b] = [int(x) for x in input().split()] 
    for i in range(a,b+1) : 
        print(list[i] , end =' ')  
    print() 
