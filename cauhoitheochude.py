import os 
os.system('cls')

t = int(input())
a = [] 
x = '' 
for i in range(t): 
    x = input()
    a.append(x) 
    if x == "" : 
        print(a[0] + ':' , len(a) - 2) 
        a.clear()
print(a[0] +':', len(a) - 1 )
    