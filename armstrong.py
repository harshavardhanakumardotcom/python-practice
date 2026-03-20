#sum of (each digit ^ no of digits) = original number
n = int(input("enter a number:"))
x=n
sum =0
d = len(str(n))
while n>0:
    y=n%10                   #153 = 3(remainder)
    sum = sum + y**d         #sum=0+3**3
    n =  n//10               #153//10 =15(qutioent)             
   
if sum == x:
    print("armstrong")
else:
    print("not a armstrong")

