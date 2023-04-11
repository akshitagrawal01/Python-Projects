numbers = input("Enter Your Number Separating With Commas: ")
l1 = numbers.split(",")
l1 = [int(x) for x in l1]
l2 = []

for num1 in l1:
    if num1 % 2 == 0:
        l2.append(num1)

print(l2)

