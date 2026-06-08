# Python program to Check the Number is prime or Not
num = int(input("Enter a Number : "))

if num > 1:
    for i in range(2,num):
        if (num % i) == 0:
            print(num,"is not a prime number.")
            break
    else:
        print(num,"is a prime number.")
else:
    print("Enter a Number greater than 1")