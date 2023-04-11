numbers = input("Enter your numbers with commas: ")
l1 = numbers.split(", ")
l1 = [int(x) for x in l1]

for i in range(len(l1)):
    for j in range(i+1, len(l1)):
        if l1[i] + l1[j] == 10:
            print(f'({l1[i]}, {l1[j]})')
            break
    else:
        continue
    break
else:
    print("No pair found")
