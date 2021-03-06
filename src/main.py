# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')


def generate_password():
    length_password = random.randrange(8, 17)
    password = []

    for i in range(2):
        num = random.randrange(48, 56)
        upper_char = random.randrange(65, 91)
        lower_char = random.randrange(97, 122)
        symbol = random.randrange(33, 48)
        password.append(chr(num))
        password.append(chr(upper_char))
        password.append(chr(lower_char))
        password.append(chr(symbol))

    for i in range(length_password - 8):
        char = random.randrange(33, 126)
        password.append(chr(char))

    return ''.join(password)


def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
