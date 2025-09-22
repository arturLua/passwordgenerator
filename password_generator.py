import string
import secrets
import requests

print('\n|| RANDOM PASSWORD GENERATOR ||\n')


def get_words():
    try:
        url = "https://www.cs.utexas.edu/~mitra/csFall2022/cs313/assgn/words.txt" # Curated word list file
        resp = requests.get(url)
        words = resp.text.splitlines()
        return words

    except requests.RequestException:
        print("Error acessing the word list.")
        exit(1)

# -------------------- #

def randomize_word(word, capitalize=False, include_special=False):
    if capitalize:
        word = word.capitalize()
    
    if include_special:
        special_char = secrets.choice(symbols)
        word = word + special_char

    return word

# -------------------- #

words = []
while not words:
    words = get_words()
    if not words:
        print("Trying again in 5 seconds...")
        import time
        time.sleep(5)

num_words = None
while num_words is None or num_words < 5:
    try:
        num_words = int(input("Enter amount of words for your password (min 5): "))
        if num_words < 5:
            print("Must be at least 5 words! Try again.")
    except ValueError:
        print("Invalid input. Please enter a number. ")

# -------------------- #

symbols = string.digits + "!@#$%^&*"

capitalize_choice = input("Capitalize the first letter of each word? [Y] / [N]: ").lower()
capitalize = capitalize_choice == "y"

include_special_choice = input("Include special characters / numbers in words? [Y] / [N]: ").lower()
include_special = include_special_choice == "y"

# -------------------- #

while True:
    password_list = [randomize_word(secrets.choice(words), capitalize, include_special) for _ in range(num_words)]
    password = "-".join(password_list)

    print("\nSuccessfully Generated! Copy below:")
    print(f"\n{password}\n")
    
    tryAgain = input("Generate another one? [Y] / [N]: ").lower()
    if tryAgain != "y":
        input("Press [Enter] to exit ")
        break

