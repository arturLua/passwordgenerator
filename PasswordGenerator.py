import string
import secrets
import requests

print('|| RANDOM PASSWORD GENERATOR ||\n')

url = "https://www.cs.utexas.edu/~mitra/csFall2022/cs313/assgn/words.txt" # Curated word list file
resp = requests.get(url)
words = resp.text.splitlines()

num_words = None
while num_words is None or num_words < 4:
    try:
        num_words = int(input("Enter amount of words for your password (min 4): "))
        if num_words < 4:
            print('Must be at least 4 words! Try again.')
    except ValueError:
        print('Invalid input. Please enter a number. ')

symbols = string.digits + "!@#$%^&*"

# Randomization with special characters
def randomize_word(word):
    word = word.capitalize()
    pos = secrets.randbelow(len(word)+1)
    token = secrets.choice(symbols)
    word = word + token
    return word

password_list = [randomize_word(secrets.choice(words)) for _ in range(num_words)]
password = "-".join(password_list)

print(f"Generated Password below:\n > {password} < " )
input("Press [Enter] to exit")
