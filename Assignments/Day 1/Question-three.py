import random
import string

def password_generator(password_strength):
  '''
  A function to generate a password of various strength's according to users input
  Returns a password according to what the user has inputted either weak, medium,or strong
  '''
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
   

