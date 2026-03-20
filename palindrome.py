num = input("enter the number:")

for i in range(len(num)//2):
    #if num[i]==num[-i-1]:
    if num == num[::-1]:
        print("palindrome")
        break
    else:
        print(" not a palindrome")
        break 