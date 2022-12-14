import os 
os.system('cls')
s = input()
n = len(s) 
if  n >= 3 and s[n-3:n].lower() == ".py" : print('yes')
else : print('no')