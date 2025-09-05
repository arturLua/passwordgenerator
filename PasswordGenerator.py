import string
import random
import secrets

print('Random Password Generator\n')

characterList = list(string.ascii_letters + string.digits + string.punctuation)

def generate_password(length): # Generated password will have one of each type, randomize it(shuffle) and put it all together(join).
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    password += random.choices(characterList, k=length-4)
    random.shuffle(password)
    return ''.join(password)

length = None
while length is None or length < 8:
    print('Choose the length of the password (8+ characters)')
    try:
        length = int(input("Enter password length: "))
        if length < 8:
            print('Password length must be at least 8 characters! Try again.')
    except ValueError:
        print('Invalid input. Please enter an integer numeric value. ')

password = generate_password(length)
print(f"🔑 - {password}")
input("\nPress Enter to exit . . . ")
