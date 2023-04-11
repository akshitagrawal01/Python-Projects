numbers = int(input("Enter A Positive Number: "))
if numbers  < 0:
    print("Please Enter A Positive Number")
else:
    l1 = []
    i = 0
    while i < numbers:
        i += 1
        l1.append(i)
    print(sum(l1))
