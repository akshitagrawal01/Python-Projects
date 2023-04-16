values = []
i = 0
while i < 5:
    numbers = int(input("Enter your number: "))
    values.append(numbers)
    i += 1

# Sort the list in descending order
values.sort(reverse=True)

print("The sorted list in descending order is: ")
print(values)
