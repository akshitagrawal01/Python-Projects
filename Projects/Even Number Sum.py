numbers = input("Enter Your Number: ")
l1 = numbers.split(",")
l1 = [int(x) for x in l1]
l2 = []

for num in l1:
    if num % 2 == 0:
        l2.append(num)

l2 = [int(y) for y in l2]

sum_even = 0
for num in l2:
    sum_even += num 
        
print(sum_even)



