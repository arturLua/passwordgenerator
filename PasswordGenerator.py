import secrets
import requests

print('|| RANDOM PASSWORD GENERATOR ||\n')

url = "https://www.cs.utexas.edu/~mitra/csFall2022/cs313/assgn/words.txt" # Curated word list file
resp = requests.get(url)
words = resp.text.splitlines()

num_words = None
while num_words is None or num_words < 4:
    try:
        num_words = int(input("Enter number of words for length: "))
        if num_words < 4:
            print('Must be at least 4 words! Try again.')
    except ValueError:
        print('Invalid input. Please enter a number. ')

password_list = [secrets.choice(words) for _ in range(num_words)]
password = "-".join(password_list) # Separates words by a hyphen

print(f"Generated Password below:\n > {password} < " )
input("Press Enter to exit ... ")
