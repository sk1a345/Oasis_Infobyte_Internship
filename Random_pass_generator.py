import random
import string

def get_yes_no(prompt):
    while True:
        answer = input(prompt + " (y/n): ").strip().lower()
        if answer in ('y', 'n'):
            return answer == 'y'
        print("Please enter 'y' or 'n'.")

def get_password_length():
    while True:
        try:
            length = int(input("Enter desired password length (e.g., 8-32): "))
            if 8 <= length <= 32:
                return length
            print("Please enter a number between 8 and 32.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def generate_password(length, use_letters, use_digits, use_symbols):
    char_pool = ""
    if use_letters:
        char_pool += string.ascii_letters
    if use_digits:
        char_pool += string.digits
    if use_symbols:
        char_pool += string.punctuation

    if not char_pool:
        print("You must select at least one character type.")
        return None

    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    print("=== Random Password Generator ===")

    length = get_password_length()
    use_letters = get_yes_no("Include letters?")
    use_digits = get_yes_no("Include digits?")
    use_symbols = get_yes_no("Include symbols?")

    password = generate_password(length, use_letters, use_digits, use_symbols)
    if password:
        print("\nGenerated password:")
        print(password)

if __name__ == "__main__":
    main()
