 import random


char = '~`!@#$%^&*()-_+=[]|\\/:;"<>,.?1234567890AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'

# generates 5 letter word
def generate_word():
    return ''.join(random.choices(char, k=5))

# Gset a file name based on user input
file_name = input('File name: ') + ".txt"

# generates three words
word1 = generate_word()
word2 = generate_word()
word3 = generate_word()

# sets three 5 letter password
password = f"{word1} {word2} {word3}"

# store the pasword in a txt file within teh directory 
with open(file_name, 'w') as file:
    file.write(password)

print(f"Password saved in {file_name}")
