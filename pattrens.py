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
        print(k,end=" ")
    print()

for i in range (n,0,-1):
    for j in range (n-i):
        print(" ",end="")
    for k in range (i):
        print(k,end=" ")
    print()

for i in range (1,n+1):
    for j in range(n-i):
        print(" ",end ="")
    for k in range(1,i+1):
        print(k,end=" ")
    print()

    #FLOYD'S TRIANGLE

print("floyd's triangle")
num = 1

for i in range (1,n+1):
    for j in range(i):
        print(num,end=" ")
        num = num+1
    print()
sum=1
for i in range (1,n+1):
    for j in range(i):
        print(sum,end=" ")
        sum+=2
    print()

print("centered number pyramid")
for i in range (1,n+1):
    for j in range(n-i):
        print("  ",end="")
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()
for i in range(n,0,-1):
    for j in range(n-i):
        print("  ",end="")
    for j in range(1,i+1):
        print(j,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print()
