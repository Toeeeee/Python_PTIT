
import os 
os.system('cls')
def kiemtra (s) : 
    for i in s : 
        if i != '0' and i != '1' and i != '2' : return 0 
    return 1 
t = int(input())
while t > 0 : 
    t-=1 
    s = input()
    if kiemtra(s) == 1 : print("YES")
    else : print("NO")
