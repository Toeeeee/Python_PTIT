
from decimal import Decimal
import os 
import math 
os.system('cls')
class Point : 
    def __init__(self,x,y) : 
        self.x = x 
        self.y = y 
    def distance(self,b) : 
        S = float(math.sqrt((self.x -b.x)*(self.x - b.x) + (self.y - b.y)*(self.y - b.y)))
        return "{:.4f}".format(S)

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1