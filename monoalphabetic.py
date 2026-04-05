import random as r
import string

def gen_key():
    pt_pool = list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.digits)
    ct_pool = list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.digits)
    r.shuffle(ct_pool)
    return dict(zip(pt_pool, ct_pool))

key = gen_key()
print("Encryption Key:", key)

msg = input("Enter your message for Encryption: ")

def encrypt(msg, key):
    cipher = ""
    for char in msg:
        if char in key:
            cipher += key[char]
        else:
            cipher += char
    return cipher

def decrypt(cipher, key):
    rev_key = {v: k for k, v in key.items()}
    plain = ""
    for char in cipher:
        if char in rev_key:
            plain += rev_key[char]
        else:
            plain += char
    return plain

encrypted_msg = encrypt(msg, key)
print("Encrypted:", encrypted_msg)

print("Decrypted:", decrypt(encrypted_msg, key))
