import math
msg = input("Enter text to be encrypted: ").replace(" ", "")
key = input("Enter the key to use: ")

def gentable(msg, col):
    rows = math.ceil(len(msg) / col)
    dcells = (rows * col) - len(msg)
    msg += 'x' * dcells   # pad with x
    table = []
    for i in range(0, len(msg), col):
        table.append(list(msg[i:i+col]))
    return table

def columnar(pt, keyword):
    ct = ""
    mat = gentable(pt, len(keyword))
    
    # Create column order based on alphabetical order of keyword
    order = sorted(range(len(keyword)), key=lambda k: (keyword[k], k))
    
    for col in order:
        for row in mat:
            ct += row[col]
    return ct

print("Ciphertext:", columnar(msg, key))
