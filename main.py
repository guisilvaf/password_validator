import secrets
import string

# variables for checking characters in the current password
password_letters = 0
password_digits = 0
password_special = 0

clients_input = input("You already has a password? Y/N: ")

if clients_input.upper() == 'Y':
    # input for user current password
    password_input = input("What is your current password? ")

    # checking password strength
    if len(password_input) >= 16:
        for i in password_input:
            if i in string.ascii_letters:
                password_letters += 1
            if i in string.digits:
                password_digits += 1
            if i in string.punctuation:
                password_special += 1

    if password_letters >= 1 and password_digits >= 1 and password_special >= 1 and password_letters\
            + password_special + password_digits == len(password_input):
        print("Valid Password")
    else:
        print("Invalid Password")

if clients_input.upper() == 'N':
    # defining alphabet
    letters = string.ascii_letters
    digits = string.digits
    special_charts = string.punctuation

    alphabet = letters + digits + special_charts

    # password length
    pwd_length = 12

    # generating password constraints
    while True:
        pwd = ''
        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))

        if (any(char in special_charts for char in pwd) and
                sum(char in digits for char in pwd)):
            break

    print(f'Your new password is: {pwd}')
