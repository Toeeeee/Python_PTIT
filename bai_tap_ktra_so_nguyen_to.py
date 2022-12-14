
import os 
os.system('cls')

n = int(input("Nhập số nguyên: "))

kt = 0 
if n < 2 : kt = 1 
else : 
    for i in range (2,n,1) :
        if n % i == 0 : 
            kt = 1 
            break 

if kt == 0 : print (n, "số nguyên tố ")
else:  print (n, "không phải số nguyên tố ")
i = 0 
while (1) :
    print ('1')
    i+= 1 
    if i == 10 : 
        break 

