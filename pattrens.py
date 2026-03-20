n = int(input("number"))
for i in range (1, n+1):
    for j in range(i):
        print("*",end=" ")
    print()

for k  in range (n,0, -1):
    for j in range(k):
        print("*",end=" ")
    print()

for i in range (1,n+1):
    for j in range (n-i):
        print(" ",end="")
    for k in range(i):
        print("*",end=" ")
    print()

for i in range (n,0,-1):
    for j in range (n-i):
        print(" ",end="")
    for k in range (i):
        print("*",end=" ")
    print()
