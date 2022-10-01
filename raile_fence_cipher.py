def encrypt(plaintext, given_key):
    flag, row = 0, 0
    for i in range(len(plaintext)):
        rail[row][i] = plaintext[i]
        if row == 0:
            flag = 0
        elif row == given_key - 1:
            flag = 1
        if flag == 0:
            row += 1
        else:
            row -= 1
    print(print_cipher(plaintext))


def print_cipher(plaintext):
    cipher = []
    for i in range(key):
        for j in range(len(plaintext)):
            if rail[i][j] != '\n':
                cipher.append(rail[i][j])
    result = "".join(cipher)
    return result.upper()


def decrypt(ciphertext, given_key):
    flag, row = 0, 0
    for i in range(len(ciphertext)):
        rail[row][i] = "*"
        if row == 0:
            flag = 0
        elif row == given_key - 1:
            flag = 1
        if flag == 0:
            row += 1
        else:
            row -= 1
    index = 0
    for i in range(given_key):
        for j in range(len(ciphertext)):
            if rail[i][j] == "*" and index < len(ciphertext):
                rail[i][j] = ciphertext[index]
                index += 1
    print(print_plain(ciphertext))


def print_plain(ciphertext):
    result, row, flag = [], 0, None
    for i in range(len(ciphertext)):
        if row == 0:
            flag = True
        if row == key - 1:
            flag = False
        if rail[row][i] != '*':
            result.append(rail[row][i])
        if flag:
            row += 1
        else:
            row -= 1
    return "".join(result).lower()


input_string, key = list(input("Type your string: ")), int(input("Enter the key: "))
rail = [["\n" for i in range(len(input_string))] for j in range(key)]
print("\t\t\t **** Choose one Option ****\n")
choice = input("1- Encrypt 2- Decrypt: ")
if choice == '1' or choice == 'e' or choice == 'encrypt':
    encrypt(input_string, key)
elif choice == '2' or choice == 'd' or choice == 'decrypt':
    decrypt(input_string, key)
else:
    print("OOPS Wrong Input!\n Try again...")
