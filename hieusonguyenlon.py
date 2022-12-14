import os 
os.system('cls')

t = int(input())
while t > 0 : 
    t-=1
    a = int(input())
    b = int(input())
    m = max(len(str(a)),len(str(b)))
    x = str(abs(a-b))
    for i in range(m - len(x)) : 
        print(0, end='') 
    print(x) 
