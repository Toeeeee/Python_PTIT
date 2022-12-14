import os
os.system('cls')
n = int(input())
a = [0]*n 
for i in range(n) :
    a[i] = [int(x) for x in input().split() ] 

for i in range(n) : 
    for j in range(n) : 
        print(a[i][j] , end = ' ') 
    print()

k = int ( input()) 

    