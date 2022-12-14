import os
os.system('cls')
n, m = [int(x) for x in input().split()] 
a = [ int(x) for x in input().split()] 
b = [ int(x) for x in input().split()] 
m1 = set() ; m2 = set() 
for i in a : 
    m1.add(i) 
for i in b : 
    m2.add(i) 
if len(m1) != len(m2) : 
    print("NO") 
else : 
    kt = 1 
    for i in m1 : 
        if i not in m2 : 
            print("NO")
            kt = 0 
            break 
    if kt == 1 : 
        print("YES")
