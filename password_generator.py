import string
import secrets
import requests

print('\n|| RANDOM PASSWORD GENERATOR ||\n')

try:
    url = "https://www.cs.utexas.edu/~mitra/csFall2022/cs313/assgn/words.txt" # Curated word list file
    resp = requests.get(url)
    words = resp.text.splitlines()
    
except requests.RequestException:
    print("Error acessing the word list.")
    exit(1)

num_words = None
while num_words is None or num_words < 5:
    try:
        num_words = int(input("Enter amount of words for your password (min 5): "))
        if num_words < 5:
            print("Must be at least 5 words! Try again.")
    except ValueError:
        print("Invalid input. Please enter a number. ")

symbols = string.digits + "!@#$%^&*"

capitalize_choice = input("Capitalize letters? [Y] / [N]: ").lower()
capitalize = capitalize_choice == "y"

# Randomization with special characters / numbers
def randomize_word(word):
    if capitalize:
        word = word.capitalize()
    token = secrets.choice(symbols)
    word = word + token
    return word

while True:
    password_list = [randomize_word(secrets.choice(words)) for _ in range(num_words)]
    password = "-".join(password_list)
    
    print("\nSuccessfully Generated! Copy below:")
    print(f"\n{password}\n")
    
    tryAgain = input("Generate another one? [Y] / [N]: ").lower()
    if tryAgain != "y":
        input("Press [Enter] to exit ")
        break

