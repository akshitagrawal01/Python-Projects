a = input("Enter any number: ")
uniqdigit = []
for digit in a:
    if digit not in uniqdigit:
        uniqdigit.append(digit)
        
print("List of unique digits in entered number is:", uniqdigit)