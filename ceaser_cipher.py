# Method 1 using Dictionary
alphabets = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11, 'm': 12,
             'n': 13, 'o': 14, 'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24,
             'z': 25}
alphabets_keys, alphabets_values, new_list, key = list(alphabets.keys()), list(alphabets.values()), [], 3


def encrypt(plaintext):
    string_list = list(plaintext.lower())
    for char in string_list:
        cipher = (alphabets[char] + 3) % 26
        new_list.append(alphabets_keys[alphabets_values.index(cipher)])
    return "".join(new_list).upper()


def decrypt(ciphertext):
    string_list = list(ciphertext.lower())
    for char in string_list:
        cipher = (alphabets[char] - 3) % 26
        new_list.append(alphabets_keys[alphabets_values.index(cipher)])
    return "".join(new_list).lower()


text = input("Enter your text: ")
choice = input("1- Encrypt, 2- Decrypt ").lower()
if choice == '1' or choice == 'e' or choice == "encrypt":
    print(encrypt(text))
elif choice == '2' or choice == 'd' or choice == 'decrypt':
    print(decrypt(text))
else:
    print("Wrong Input!")


# Method 2  using chr and ord
def encrypt(plaintext, key):
    ciphertext = ""
    for i in range(len(plaintext)):
        char = plaintext[i].lower()
        ciphertext += chr((ord(char) + key - 97) % 26 + 97)
    return ciphertext.upper()


def decrypt(ciphertext, key):
    plaintext = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i].lower()
        plaintext += chr((ord(char) - key - 97) % 26 + 97)
    return plaintext


text, key = input("Enter your text: "), int(input("Enter the key: "))
choice = input("1- Encrypt, 2- Decrypt ").lower()
if choice == '1' or choice == 'e' or choice == "encrypt":
    print(encrypt(text, key))
elif choice == '2' or choice == 'd' or choice == 'decrypt':
    print(decrypt(text, key))
else:
    print("Wrong Input!")
