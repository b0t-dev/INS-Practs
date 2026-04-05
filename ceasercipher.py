import string
msg = input("Enter message for Encryption:")
def encrypt(msg, key=3):
    pool = list(string.ascii_lowercase) + list(string.ascii_uppercase)+list(string.digits)
    cipher= ""
    for char in msg:
        if char in pool:
            E = (pool.index(char) + key) % len(pool)
            cipher += pool[E]
        else:
            cipher += char
    return cipher

print("Cipher text: ", encrypt(msg))


import string
msg = input("Enter message for Decryption:")
def decrypt(msg, key=3):
    pool = list(string.ascii_lowercase) + list(string.ascii_uppercase)+list(string.digits)
    decipher= ""
    for char in msg:
        if char in pool:
            E = (pool.index(char) - key) % len(pool)
            decipher += pool[E]
        else:
            decipher += char
    return decipher
print("Plain text: ", decrypt(msg))
