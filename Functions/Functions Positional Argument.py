def greet_user(first_name, last_name):
    print(f'Hi {first_name} {last_name}')
    print("Welcome Aboard")


user_name = input("Enter Your Name: ")
user_surname = input("Enter Your Surname: ")
print("Start")
greet_user(user_name, user_surname)
print("End")
