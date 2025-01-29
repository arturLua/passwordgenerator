# Project Name
print('[WIP] Password Generator 0.2!\n')

# Importing functions
import string
import random

# Characters that will be used in the password
characterList = list(string.ascii_letters + string.digits + string.punctuation)

def generate_password(length):
    # Makes sure the password has at least one of each type.
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    password += random.choices(characterList, k=length-4)

    # Ensure randomness in the password
    random.shuffle(password)
    return ''.join(password)

# Defining password length
length = None
while length is None or length < 8:
    print('Choose the length of your password (8+ characters)')
    try:
        length = int(input("Enter password length: "))
        if length < 8:
            print('Password length must be at least 8 characters')
    except ValueError:
        print('Invalid input. Please enter an integer numeric value')


# Generating password results
password = generate_password(length)
print(f'Your generated password is: {password}')

input("\nPress Enter to exit the CMD")

