import random
import string
while True:
    length = input("Enter the password length (default is 12) or type 'exit' to quit: ")
    if length == 'exit':
        print("Goodbye!")
        break
    if length.isdigit():
        length = int(length)
    else:
        length = 12
    char_type = input("Enter character types (letters/digits/all) or type 'exit' to quit: ").lower()
    if char_type == 'exit':
        print("Goodbye!")
        break
    if char_type == 'letters':
        characters = string.ascii_letters
    elif char_type == 'digits':
        characters = string.digits
    elif char_type == 'all':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid input. Please enter 'letters', 'digits', or 'all'.")
        continue
    password = ''.join(random.choice(characters) for _ in range(length))
    print("Generated password:", password)
    if input("Generate again? (yes/no): ").lower() != 'yes':
        print("Goodbye!")
        break