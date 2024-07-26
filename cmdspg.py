import string
from random import choice

def generate_password(length, use_lower, use_upper, use_numbers, use_symbols):
    characters = ''
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        return "Please select at least one character type."
    
    return ''.join(choice(characters) for _ in range(length))

def main():
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")

    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_lower, use_upper, use_numbers, use_symbols)
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()