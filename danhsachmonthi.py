import os 
os.system('cls')
class Mon : 
    def __init__(self,ma, ten,ht) :
        self.ma = ma 
        self.ten = ten 
        self.ht = ht 
    def output(self) :
        print(self.ma, self.ten,self.ht) 

t = int(input())
a = [] 
while t > 0 : 
    t-=1
    ma = input()
    ten = input()
    ht = input()
    a.append(Mon(ma,ten,ht))
a = sorted(a, key=lambda x : x.ma ) 
for i in a : 
    i.output()  