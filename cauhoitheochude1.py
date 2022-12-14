import os
os.system('cls')
t = int(input())
s = '' 
a = []
while t > 0 : 
    t-=1 
    s = input() 
    a.append(s) 
    if s == '' : 
        t+=1
        print(a[0] + ':', len(a) - 2) 
        a.clear() 
print(a[0] + ':', len(a) - 1) 