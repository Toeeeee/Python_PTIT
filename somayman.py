import os
os.system('cls') 

s = input()
dem = 0 
for i in s : 
    if i == '7' or i == '4' : dem = dem + 1 
if ( dem == 4 or dem == 7 )  : print("YES") 
else : print("NO") 
    