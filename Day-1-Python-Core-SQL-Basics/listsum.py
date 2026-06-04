#Sum of List Elements 
n = int(input("How many numbers? "))
numbers = []

for i in range(n):
    value = int(input("Enter number: "))
    numbers.append(value)
    
total = 0

for num in numbers:
    total += num

print("Sum =", total)