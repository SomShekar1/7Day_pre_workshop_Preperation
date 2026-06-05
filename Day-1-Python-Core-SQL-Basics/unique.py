#Remove Duplicates from a List


numbers = [10, 20, 10, 30, 20, 40, 50, 40]

uniq_list= []

for num in numbers:
    if num not in uniq_list:
        uniq_list.append(num)

print("Original List: \n", numbers)
print("List After Removing Duplicates:\n", uniq_list)