import os 
os.system('cls')
n , m = [int(x) for x in input().split()] 
a = [int(x) for x in input().split()] 
b = [int(x) for x in input().split()]
m = {}
for i in (a+b) : 
    if i in m : 
        m[i] += 1 
    else: m[i] = 1 
m = sorted(m.items(), key = lambda x : x[0] ) 
for i in m :
    if i[0] in a and i[0] in b : 
        print(i[0], end = ' ') 
print() 
for i in m :
    if i[0] in a and i[0] not in b : 
        print(i[0], end = ' ') 
print() 
for i in m :
    if i[0] not in a and i[0] in b : 
        print(i[0], end = ' ') 
print() 