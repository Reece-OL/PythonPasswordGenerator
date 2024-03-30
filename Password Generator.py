import random

char = '~`!@#$%^&*()-_+=[]|\/:;"<>,.?1234567890AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
fileName = input('File name: ')
fileName += ".txt"
passwordLength = input('Password Length: ')
passwordLength = int(passwordLength)

password = ''.join(random.choices(char, k=passwordLength))

with open(fileName, 'w') as file:
    file.write(password) 
