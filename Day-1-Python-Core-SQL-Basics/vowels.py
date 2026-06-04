# Count Vowels in a String
text = input("Enter a string: ")
count = 0

for ch in text:
    if ch in "aeiou" and "AEIOU":
        count += 1
print("Number of vowels:", count)