import string
 
msg = input("Enter plain text : ").lower().replace("j", "i")
key = input("Enter the key : ").lower().replace("j", "i")
 
def gen_matrix(key):
    keymat = []
    k = []
    pool = [char for char in list(string.ascii_lowercase) if char != 'j']
    for i in key:
        if i not in k:
            k.append(i)
    for j in pool:
        if j not in k:
            k.append(j)
    for i in range(0, len(k), 5):
        keymat.append(k[i:i+5])
    return keymat
 
def digram(msg):
    for i in range(0, len(msg)+1, 2):
        if i < len(msg)-1:
            if msg[i] == msg[i+1]:
                msg = msg[:i+1] + 'x' + msg[i+1:]
    if len(msg) % 2 != 0:
        msg += 'x'
    return msg
 
def getloc(char, matrix):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return [row, col]
 
def playfair(pt, keytext):
    ct = ""
    pt = pt.replace(" ", "")
    km = gen_matrix(keytext)
    d = digram(pt)
    for i in range(0, len(d), 2):
        c1 = getloc(d[i], km)
        c2 = getloc(d[i+1], km)
        # same row
        if c1[0] == c2[0]:
            c1r = c1[0]
            c1c = (c1[1]+1) % 5
            c2r = c2[0]
            c2c = (c2[1]+1) % 5
        # same column
        elif c1[1] == c2[1]:
            c1r = (c1[0]+1) % 5
            c1c = c1[1]
            c2r = (c2[0]+1) % 5
            c2c = c2[1]
        # When rows and cols mismatch
        else:
            c1r = c1[0]
            c1c = c2[1]
            c2r = c2[0]
            c2c = c1[1]
        ct += km[c1r][c1c] + km[c2r][c2c]
    return ct
 
print("Cipher Text:", playfair(msg, key))
gen_matrix(key)
