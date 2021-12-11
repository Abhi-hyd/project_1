n =6
for i in range(0,n):
    for j in range(n-1,i,-1):
        print(j,"",end=" ")
    for k in range(i):
        print(" *  ",end= "  ")
    for y in range(i+1,n):
        print(y,"",end="  ")
    print('\n')