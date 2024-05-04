import random

upper_case_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                      'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower_case_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                      't', 'u', 'v',
                      'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

upper = int(input("How many Upper Case Characters you want in your in Password: "))
lower = int(input("How many Lower Case Characters you want in your Password: "))
digits = int(input("How many digits you want in your Password : "))
symbol = int(input("How many symbols you want in your Password: "))
print("\n")

password = []

for i in range(0, upper):
    password.append(random.choice(upper_case_letters))

for i in range(0, lower):
    password.append(random.choice(lower_case_letters))

for i in range(0, digits):
    password.append(random.choice(numbers))

for i in range(0, symbol):
    password.append(random.choice(symbols))

random.shuffle(password)
new_password = ""
for i in range(0, len(password)):
    new_password = new_password + password[i]

print("The auto generated password is : " + new_password)
