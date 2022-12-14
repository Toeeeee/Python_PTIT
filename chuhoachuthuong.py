import os 
os.system('cls') 
s = input() 
thuong = 0 ;
hoa = 0 ;
for i in s : 
    if ( i <= 'Z' and i >= 'A' ) : hoa = hoa+ 1 
    else : thuong = thuong + 1 

if ( thuong >= hoa ) : print(s.lower()) 
else : print(s.upper())  
