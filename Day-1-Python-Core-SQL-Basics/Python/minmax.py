#Find Minimum and Maximum Numbers in a List
n = int(input("How many numbers? "))
numbers = []
for i in range(n):
    value = int(input("Enter number: "))
    numbers.append(value)

maximum = numbers[0]
minimum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

    if num < minimum:
        minimum = num

print("Maximum =", maximum)
print("Minimum =", minimum)