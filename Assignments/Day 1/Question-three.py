#3. Write a password generator function in Python. Strong passwords have a mix of
# lowercase letters, uppercase letters, numbers, and symbols. The passwords
# should be random, generating a new password every time the user asks for a
# new password. Include your run-time code in a main method.
#For extra credit:
# ● Ask the user how strong they want their password to be.

import random
import string
input("What password strength do you want ? ")
def password_generator(password_strength):
    password_strength = len(8)

