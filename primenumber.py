num = int(input("enter the number:"))

#checking wether the given number is prime number or not
if num == 1:
    print("the given number is neither prime nor composite")
else:
    for i in range (2,num):
        if num%i == 0:
            print("not a prime number")
            break
        else:
            print("prime number")
            break