import secrets
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_special=True):
    """
    Generate a random password of the specified length with optional character sets.

    Parameters:
    - length: Desired length of the password.
    - use_uppercase: Include uppercase letters.
    - use_digits: Include digits.
    - use_special: Include special characters.

    Returns:
    - The generated password.
    """
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def prompt_user():
    """
    Prompt the user to enter password preferences.

    Returns:
    - Tuple containing password length, and boolean values for uppercase, digits, and special characters.
    """
    length = int(input("Enter the desired length of the password: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    return length, use_uppercase, use_digits, use_special

def main():
    """
    Main function to execute the password generator.
    """
    print("PASSWORD GENERATOR")

    length, use_uppercase, use_digits, use_special = prompt_user()

    password = generate_password(length, use_uppercase, use_digits, use_special)

    print("\nGenerated Password:", password)

if __name__ == "__main__":
    main()
