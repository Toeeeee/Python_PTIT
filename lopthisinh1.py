import os 
os.system('cls')

class Sinhvien : 
    def __init__(self,ten,ns,d1,d2,d3) :
        self.ten = ten 
        self.ns = ns 
        self.d1 = d1 
        self.d2 = d2 
        self.d3 = d3
    def out(self) : 
        print(self.ten,self.ns,round(self.d1+self.d2+self.d3,1)) 

ten = input()
ns = input() 
d1 = float(input())
d2 = float(input())
d3 = float(input()) 
a = Sinhvien(ten,ns,d1,d2,d3)
a.out() 