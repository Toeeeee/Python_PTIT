import os 
os.system('cls')
def kiemtra(s1) : 
    s2 = "" 
    for i in s1 : s2 = i + s2 

    for i in range(1,len(s1)) : 
        if abs(ord(s1[i]) - ord(s1[i-1])) != abs(ord(s2[i]) - ord(s2[i-1])) : 
            return 0 
    return 1

t = int(input())

while t > 0 : 
    t = t - 1 
    s1 = input() 
    if kiemtra(s1) == 1 : print ("YES")
    else : print("NO") 