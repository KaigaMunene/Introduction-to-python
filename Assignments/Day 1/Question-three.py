#3. Write a password generator function in Python. Strong passwords have a mix of
# lowercase letters, uppercase letters, numbers, and symbols. The passwords
# should be random, generating a new password every time the user asks for a
# new password. Include your run-time code in a main method.
#For extra credit:
# ● Ask the user how strong they want their password to be.


import random
import string

def password_generator(password_strength):
  password = []
  if password_strength == "weak":
    for a in range(8):
      password.append(random.choice(string.ascii_lowercase))
  elif password_strength == "medium":
    for a in range(10):
      password.append(random.choice(string.ascii_letters))
  
  elif password_strength == "strong":
    for a in range(12): 
      password.append(random.choice(string.printable))

  return ''.join(password)

while True:
  password_strength = input("Enter the password strength:\n weak\n medium\n strong\n: ")
  if password_strength == "weak" or password_strength =="medium" or password_strength == "strong": 
    break
  else:
    print("enter valid password strength")
#print(random.choice(string.ascii_lowercase))

print(password_generator(password_strength))
   

