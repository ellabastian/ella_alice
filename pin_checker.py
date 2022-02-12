import getpass
# password_number = "4321"
# user_number_of_attempts = 0
# max_number_of_attempts = 3

# while user_number_of_attempts < max_number_of_attempts:
#     supplied_pin = input("Please enter your PIN:")
#     user_number_of_attempts +=1
#
# while user_number_of_attempts < max_number_of_attempts:
#     supplied_pin = input("Please enter your PIN:")
#     if not:
#         print("Wrong pin")
#         continue
#     else:
#         print("Yay right pin")
#         break
# attempts = 3
# user_trys = 0
# required_number = "4321"
#
# while user_trys < attempts:
#     number = input("Enter a number:")
#     if number == required_number:
#         print("Right pin")
#         break
#     else:
#         print("Wrong number, try again")
#         user_trys +=1

# while user_number_of_attempts < max_number_of_attempts:
#     supplied_pin = input("Enter your PIN: ")
#     if supplied_pin == str(password_number):
#         print("You have access to your account")
#         break
#     else:
#         user_number_of_attempts += 1
#         print("You have used", user_number_of_attempts, 'out of', max_number_of_attempts, 'attempts')
#         if user_number_of_attempts == max_number_of_attempts:
#             print("You have no more attempts left. You are blocked from your account.")
password_number = 4321
max_number_of_attempts = 3
user_number_of_attempts = 0

while user_number_of_attempts < max_number_of_attempts:
    # supplied_pin = getpass.getpass("Enter your PIN:")
    supplied_pin = input("Enter your PIN: ")
    if supplied_pin == str(password_number):
         print("Correct PIN. You now have access to your account")
         break
    else:
        user_number_of_attempts += 1
        print("You have used", user_number_of_attempts, 'out of', max_number_of_attempts, 'attempts')
        if user_number_of_attempts == max_number_of_attempts:
            print("You have no more attempts left. You are now blocked from your account.")

# Count down instead of up and then commit to Git





