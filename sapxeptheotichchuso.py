import os 
os.system('cls')
def tichchuso(n) : 
    S = 1 
    while n > 0 : 
        x = n%10 
        S = S*x 
        n = int(n/10)
    return S 
t = int(input())
while t > 0: 
    t-=1
    n = int(input())
    a = [int(x) for x in input().split()]
    m = {} 
    for i in a : 
        m[i] = tichchuso(i)
    m1 = sorted(m.items(), key = lambda x : (x[1],x[0]))
    for i in m1 : 
        print(i[0],end = ' ')
    print()
