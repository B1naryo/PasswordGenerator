# -*- coding: utf-8 -*-
import itertools

# Define the password length and allowed characters
password_length = 7
allowed_characters = '1234567'

# Generate all possible combinations
combinations = itertools.product(allowed_characters, repeat=password_length)

# Create a TXT file to save the combinations
file_name = 'password.txt'

with open(file_name, 'w') as file:
    for combination in combinations:
        password = ''.join(combination)
        file.write(password + '\n')

print(f'All possible combinations have been saved in the "{file_name}" file.')

# Be aware that this file can be extremely large and take a long time to generate.

