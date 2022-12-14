import os 
import functools
os.system('cls')

class SV : 
    def __init__(self, ten, ac , sub ) : 
        self.ten = ten 
        self.ac = ac
        self.sub = sub 
def cmp (a,b) : 
    if  a.ac < b.ac : return 1 
    elif a.ac == b.ac : 
        if a.sub > b.sub : return 1 
        elif a.sub == b.sub : 
            if a.ten > b.ten : return 1 
    return -1 

t = int(input())
l = []
while t > 0 : 
    t-=1
    s = input()
    a,b = [int(x) for x in input().split()]
    l.append(SV(s,a,b)) 

l = sorted(l,key = functools.cmp_to_key(cmp))
for i in l : 
    print(i.ten, i.ac, i.sub ) 

    