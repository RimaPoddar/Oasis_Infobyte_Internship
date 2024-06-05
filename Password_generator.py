import random
import string

# Function to shuffle all the characters of a string
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

# Function to generate a password
def generate_password(length, use_uppercase, use_lowercase, use_digits, use_punctuation):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation

    if len(characters) == 0:
        raise ValueError("At least one character set must be selected")

    password = ''.join(random.choice(characters) for _ in range(length))
    return shuffle(password)

# Main program starts here
try:
    # User inputs
    password_length = int(input("Enter the desired password length: "))
    include_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == 'yes'
    include_lowercase = input("Include lowercase letters? (yes/no): ").strip().lower() == 'yes'
    include_digits = input("Include digits? (yes/no): ").strip().lower() == 'yes'
    include_punctuation = input("Include punctuation signs? (yes/no): ").strip().lower() == 'yes'

    # Generate password
    password = generate_password(password_length, include_uppercase, include_lowercase, include_digits, include_punctuation)

    # Output
    print(f"Generated password: {password}")

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
