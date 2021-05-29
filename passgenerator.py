#Password generator
print("Welcome to the PyPassword Generator v1.0")
key_art = ('''
               .--.
              /.-. '----------.
              \'-' .--"--""-"-'
               '--'
''')
print(key_art)


import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



letter_len = int(input("How many letters would you like in your password?\n"))
symbol_len = int(input("How many symbols do you want in your password?\n"))
number_len = int(input("How many numbers would you like in your password?\n"))


print("\nNumber of letters:", letter_len) 
print("Number of symbols:", symbol_len) 
print("Number of numbers:", number_len) 

#Init empty password
password = []

for i in range(0, letter_len):
  random_letters = random.choice(letters)
  random_numbers = random.choice(numbers)
  random_symbols = random.choice(symbols)
  password.append(random_letters)
  password.append(random_numbers)
  password.append(random_symbols)


#Converting the list into a string
final_password = ""
for letter in password:
  final_password += "".join(letter)

print(f'\nHere is your random generated password: {final_password}')
print("Length of password:", len(final_password))