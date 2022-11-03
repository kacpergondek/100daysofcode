#Password Generator Project
import random
import assets
#Take initial input
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Take total lengths of lists -1, then create new list with characters for
#our password
len_let = len(assets.letters) - 1
len_sym = len(assets.symbols) - 1
len_num = len(assets.numbers) - 1

new_pass = []

#While the number of selected letters is bigger than 0, pick random
#letters for the password.
while 0 < nr_letters:
  ran_num = random.randint(0, len_let)
  new_pass.append(assets.letters[ran_num])
  nr_letters -= 1
  
#While the number of selected symbols is bigger than 0, pick random
#symbols for the password.
while 0 < nr_symbols:
  ran_num = random.randint(0, len_sym)
  new_pass.append(assets.symbols[ran_num])
  nr_symbols -= 1
  
#While the number of selected numbers is bigger than 0, pick random
#numbers for the password. 
while 0 < nr_numbers:
  ran_num = random.randint(0, len_sym)
  new_pass.append(assets.numbers[ran_num])
  nr_numbers -= 1

#Take the length of the list (-1) and then, for each randomly picked
#item, remove it from the list and add it to the end string
pass_len = len(new_pass) - 1
new_password = ""
while pass_len >= 0:
  ran_num = random.randint(0, pass_len)
  new_password += new_pass.pop(ran_num)
  pass_len -= 1

print (new_password)