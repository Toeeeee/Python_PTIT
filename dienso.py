import os
os.system('cls')
t = int(input())
while t > 0 : 
    t-=1
    n = int(input())
    a = [int(x) for x in input().split()]
    m = [] 
    for i in a : 
        if i not in m : 
            m.append(i) 
    m.sort()
    print(m[len(m) -1] - m[0] + 1 - len(m))  