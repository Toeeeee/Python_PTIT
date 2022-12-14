import os 
import math 
os.system('cls')
t = int(input())
def nguyento (n):
    if n < 2 : return 0 
    for i in range(2,int(math.sqrt(n)) + 1 ) : 
        if n % i == 0 : return 0 
    return 1 
def kiemtra (s) : 
    for i in range(len(s)) :
        if nguyento (int(s[i])) == 1 and nguyento(i) == 0 : return 0 
        if nguyento(int(s[i])) == 0 and nguyento(i) == 1 : return 0 
    return 1 

while t > 0 : 
    t = t - 1 
    s = input() 
    if kiemtra(s) == 1 : print("YES")
    else : print("NO")



