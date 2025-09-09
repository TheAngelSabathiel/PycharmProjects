letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy level
#import random
#password = ""
#for count in range(1,nr_letters+1):
    #password[x] = letters[random.randint(0,51)]
    #x = random.randint(0,51)
    #password += letters[x]
#for count in range(1,nr_symbols+1):
    #y = random.randint(0,8)
    #password += symbols[y]
#for count in range(1, nr_numbers+1):
    #z = random.randint(0, 9)
    #password += numbers[z]
#print(f"Your password is: {password}")
#random.choice(list)
# Hard Level
import random
passwordlist = []
for count in range(1,nr_letters+1):
    x = random.randint(0,51)
    passwordlist.append(letters[x])
for count in range(1,nr_symbols+1):
    y = random.randint(0,8)
    passwordlist.append(symbols[y])
for count in range(1, nr_numbers+1):
    z = random.randint(0, 9)
    passwordlist.append(numbers[z])
random.shuffle(passwordlist)
password = ""

for count in range(0,nr_letters + nr_numbers + nr_symbols):
    password += passwordlist[count]

print(f"Your password is: {password}")