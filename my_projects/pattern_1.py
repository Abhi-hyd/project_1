n = 5
d = n
c = n
for i in range(1,n+1):
    for j in range(i,n+1):
        print(d,end=" ")
        d -=1
    c -=1
    d = c
    print()