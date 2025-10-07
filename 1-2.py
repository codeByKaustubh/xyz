#monoalphabetic substitution cipher
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
keyword = "ZYXWVUTSRQPONMLKJIHGFEDCBA"  # Simple substitution cipher: reversed alphabet

def encrypt(Plaintext):
    result = ""
    for char in Plaintext:
        if char in alphabet:
            num = alphabet.find(char)
            result += keyword[num]
        else:
            result += char  # Keeps spaces or non-alphabet characters as-is
    print("Encrypted Text:", result)

def decrypt(Ciphertext):
    result = ""
    for char in Ciphertext:
        if char in keyword:
            num = keyword.find(char)
            result += alphabet[num]
        else:
            result += char
    print("Decrypted Text:", result)

while True:
    try:
        n = int(input("Enter Value:\n1) Encrypt Text\n2) Decrypt Text\n3) See Key\n4) Exit\nChoice: "))
    except ValueError:
        print("Invalid input; please enter a number between 1 and 4.")
        continue

    if n == 1:
        Plaintext = input("Enter Text to Encrypt: ")
        encrypt(Plaintext.upper())

    elif n == 2:
        Ciphertext = input("Enter Text to Decrypt: ")
        decrypt(Ciphertext.upper())

    elif n == 3:
        print("Substitution Key (Keyword):", keyword)

    elif n == 4:
        print("Exiting the program.")
        break

    else:
        print("Invalid Input; Enter Again!!")