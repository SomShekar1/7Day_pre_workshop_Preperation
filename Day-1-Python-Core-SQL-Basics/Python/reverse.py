#Reverse a string using loops
str = input("Enter a String to Reverse : ")
rev = ""
for ch in str:
    rev = ch + rev
print(rev)


#using slicing Method
text = input("Enter a String to be Reverse : ")
reversed = text[::-1]
print(reversed)