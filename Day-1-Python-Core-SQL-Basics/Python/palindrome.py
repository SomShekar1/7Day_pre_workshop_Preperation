str = input("Enter a String to Reverse : ").lower()
rev = ""
for ch in str:
    rev = ch + rev
if str == rev:
    print("The Given String is Palindrome")
else:
    print("The Given String is Not a Palindrome")