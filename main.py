#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#Input the number of letters, symbols and numbers you want
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Total characters is the number of letters plus the number of symbols plus the number of numbers
total_Characters = nr_letters + nr_symbols + nr_numbers
password = ''

for i in range(0, total_Characters):
  random_letter = random.randint(0, len(letters))
  random_number = random.randint(0, len(numbers))
  random_symbol = random.randint(0, len(symbols))
  if i < nr_letters:
    password += letters[random_letter - 1]
  elif i < nr_letters + nr_symbols:
    password += symbols[random_symbol - 1]
  elif i < nr_letters + nr_symbols + nr_numbers:
    password += numbers[random_number - 1]
print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#Hard password is the same length. Letters, numbers, and symbols are scrambled
hard_password = ''
password_list = []
characters = [letters, numbers, symbols]
for i in range(0, total_Characters):
  random_character = random.randint(0, len(characters)-1)
  if random_character == 0:
    random_letter = random.randint(0, len(letters))
    password_list.append(letters[random_letter - 1])
  elif random_character == 1:
    random_number = random.randint(0, len(numbers))
    password_list.append(numbers[random_number - 1])
  elif random_character == 2:
    random_symbol = random.randint(0, len(symbols))
    password_list.append(symbols[random_symbol - 1])
for i in range(0, len(password_list)):
  hard_password += password_list[i]
print(hard_password)
