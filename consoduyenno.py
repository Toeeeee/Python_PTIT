import os 
os.system('cls')
t = int(input())
while t > 0 :
    t = t - 1
    s = input()
    if ( s[0] == s[len(s)-1] ) : print("YES")
    else  : print("NO")