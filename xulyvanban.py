import os 
import re 
os.system('cls')

s = ""
x = '[\w\s,:]+'

while True : 
    try :
        s = s + input()
    except EOFError : break 
s = re.findall(x,s) 
# print(s) 
for i in s : 
    a = i.lower().split() 
    a[0] = a[0].title() 
    print(' '.join(a) )
    
