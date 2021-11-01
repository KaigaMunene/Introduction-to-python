#3. Write a password generator function in Python. Strong passwords have a mix of
# lowercase letters, uppercase letters, numbers, and symbols. The passwords
# should be random, generating a new password every time the user asks for a
# new password. Include your run-time code in a main method.
#For extra credit:
# ● Ask the user how strong they want their password to be.

import random
import string
# x = input("Want weak strength password: ") 
# y = input("Want medium strength password:")
z = input("Want strong strength password:")
def password_generator(password_strength):
    password_strength = 8
#     weak_password = ''.join(random.choice(string.ascii_uppercase)) 
#     for i in range(password_strength) :
#         if x == "yes":
#             print(weak_password)
    
#     medium_password = ''.join(random.choice(string.ascii_letters))
#     for i in range(password_strength):
#         if y == "yes":
#             print(medium_password)
    
    strong_password = ''.join(random.choice(string.printable))
    for i in range (password_strength):
        if z == "yes":
            print(strong_password)

print(password_generator(f"Random password is: "))

