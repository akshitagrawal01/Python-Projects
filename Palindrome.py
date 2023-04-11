palindrome = input("Enter Your Word: ")
forward = palindrome[0:]
backword = palindrome[::-1]
if forward==backword:
    print("True")
else:
    print("False")
