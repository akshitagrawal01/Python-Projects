numbers = input("Enter Your Numbers with commas: ")
l1 = list(numbers.split(", "))
l1 = list({int(x) for x in l1})
max_sum = [0]
x = 0
while x < len(l1):
    y = 1
    checker = sum(l1[x:y])
    if checker > sum(max_sum):
        max_sum.clear
        max_sum.append(checker)
    y += 1
print(max_sum)
