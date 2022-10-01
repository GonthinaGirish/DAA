import math


# To calculate and find gcd of public key and phi
def find_gcd(v1, v2):
    while True:
        temp = v1 % v2
        if temp == 0:
            return v2
        v1 = v2
        v2 = temp


# Encrypting the given message using public key and modulo operation
def encrypt(given_text, public_key):
    result = pow(given_text, public_key)
    result = math.fmod(result, n)
    return result


# Decrypting the given cipher text using private key and modulo operation
def decrypt(given_cipher, private_key):
    result = pow(given_cipher, private_key)
    result = math.fmod(result, n)
    return result


p, q = int(input("Enter 1st prime number: ")), int(input("Enter 2nd prime number: "))
# Checking whether the inputs are correct (in case if user enter numbers which are not prime
while True:
    flag = 2
    if p % 2 != 0:
        flag -= 1
    else:
        print("Wrong input for p!\n enter a prime number...")
        p = int(input("Enter a prime number: "))
    if q % 2 != 0:
        flag -= 1
    else:
        print("Wrong input for q!\n enter a prime number...")
        q = int(input("Enter a prime number: "))
    if flag == 0:
        break
# Calculating n and phi values
n = p * q
phi = (p - 1) * (q - 1)
e = 2
# Finding e or public key value
while e < phi:
    if find_gcd(e, phi) == 1:
        break
    else:
        e += 1
# using key to convert result to integer in case if it is not (normalization)
k = 2
d = (1 + (k * phi)) / e
user_input = int(input("Enter your message value number: "))
print("\t\t *** Choose an Option *** \t\t")
choice = input("1- Encrypt 2- Decrypt: ")
if choice == '1' or choice == 'e' or choice == 'encrypt':
    print(f"Encrypted message is: {encrypt(user_input, e)}")
elif choice == '2' or choice == 'd' or choice == 'decrypt':
    print(f"Decrypted message is: {decrypt(user_input, d)}")
else:
    print("OOPS Wrong Input!\n Try again...")
