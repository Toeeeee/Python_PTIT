from math import gcd
import os 
import math
os.system('cls') 
class Phanso : 
    def __init__(self,tu,mau): 
        self.tu = tu
        self.mau = mau 
    
    def rutgon(self):
        x = math.gcd(self.tu,self.mau)
        self.tu = int(self.tu/x) 
        self.mau = int(self.mau/x) 
    def output(self):
        print(self.tu,"/",self.mau,sep = "") 
    
a, b = [int(x) for x in input().split() ]
x = Phanso(a,b) 
x.rutgon()
x.output()
