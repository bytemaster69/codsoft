import random
import string

def generate_password(length):
    # Define character sets for different complexities
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Combine character sets based on complexity
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    # Ensure the password length is at least 8 characters
    length = max(length, 8)

    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    if length <= 0:
        print("Invalid length. Please enter a positive number.")
        return

    password = generate_password(length)

    print("\nHere is your freshly generated password:")
    print(password)

if __name__ == "__main__":
    main()
