import os 
os.system('cls')
t = int(input())
while t > 0 : 
    t-=1
    n = int(input())
    a = [int(x) for x in input().split()]
    a.insert(0,1000005) 
    b = [-1,0] 
    for i in range(1,n+1):
        x = b.pop()
        while a[x] <= a[i] and len(b) != 0 : 
            x = b.pop()
        b.append(x)
        print (i - x , end = ' ')
        b.append(i)
    print()