import random
import string

def generate_password():
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Length must be positive.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return

    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    chars = ''
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        print("You must select at least one character set.")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    print(f"Generated password: {password}")
