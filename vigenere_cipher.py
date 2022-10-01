def generate_key(new_key):
    new_key = list(new_key.upper())
    if len(user_input) == len(new_key):
        return new_key
    else:
        for i in range(len(user_input) - len(new_key)):
            new_key.append(new_key[i % len(new_key)])
    return "".join(new_key)


def encrypt(given_string, given_key):
    cipher_text, given_string, given_key = [], given_string.upper(), given_key.upper()
    for i in range(len(given_string)):
        value = (ord(given_string[i]) + ord(given_key[i])) % 26
        value += ord("A")
        cipher_text.append(chr(value))
    return "".join(cipher_text)


def decrypt(given_string, given_key):
    plain_text = []
    for i in range(len(given_string)):
        value = (ord(given_string[i]) - ord(given_key[i])) % 26
        value += ord("A")
        plain_text.append(chr(value))
    return "".join(plain_text).lower()


user_input = "attackatdawn"
key = "LEMON"
print("\t\t\t **** Choose one Option ****\n")
choice = input("1- Encrypt 2- Decrypt: ")
if choice == '1' or choice == 'e' or choice == 'encrypt':
    print(encrypt(user_input, generate_key(key)))
elif choice == '2' or choice == 'd' or choice == 'decrypt':
    print(decrypt(user_input, generate_key(key)))
else:
    print("OOPS Wrong Input!\n Try again...")

