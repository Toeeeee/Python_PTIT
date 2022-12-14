import os 
os.system('cls')
import re 

s = ""

t = int(input()) 
while t > 0 : 
    s = s + input().lower() + " "
    t -=1 

s = re.findall("\w+",s) 
m = {}

for i in s :
    x = i.split()
    for j in x :
        if j in m : 
            m[j] += 1 
        else : m[j] = 1 
m = sorted(m.items(), key = lambda x: (-x[1], x[0]))
for i in m :
    print(i[0], i[1])