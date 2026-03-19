print("prime numbers between 1 and 50 are")

for num in range (2,51):
    is_prime=True
    for i in range (2,51):
        if num%i==0:
            is_prime=False
            #print(num)   #for composite numbers 
            break
        else:
            is_prime=True
            print(num)
            break

#firstly line 3: declared the numbers between 2 nad 51 and then we assume the given nuber is true
# and next using for look declread varible i which is used to check wether the given number id prime or not 
#so prime number= the factors are only one and itself 
#usinf  if and else we check the prime numbers and use break to break the loop 