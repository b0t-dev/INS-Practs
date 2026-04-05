import string
 
def vernamencrypt(msg, key):
    ct = ""
    pool = list(string.ascii_lowercase)
    for i in range(len(msg)):
        pt = pool.index(msg[i])
        k = pool.index(key[i])
        xor = pt ^ k
        if xor >= 26:
            xor = xor - 26
        ct += pool[xor]
    return ct
 
a = input("Enter the text to encrypt : ").lower()
b = input("Enter the key to encrypt : ").lower()
 
if (len(a) == len(b)):
    result = vernamencrypt(a, b)
    print(f"The encrypted text : {result}")
else:
    print(f"Make sure your message and key length is equal")
