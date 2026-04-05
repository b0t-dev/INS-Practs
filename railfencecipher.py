msg = input("Enter message to encrypt here: ").replace(" ","")
rails = int(input("Enter no of rails for encryption: "))

def railfence_encrypt(pt, rails):
    ct=""
    mat = [['' for i in range(len(pt))] for j in range(rails)]
    row, check = 0, 0
    for char_indx in range(len(pt)):
        if check == 0:
            mat[row][char_indx]= pt[char_indx]
            row +=1
            if row == rails:
                check = 1
                row -= 1
        else:
            row -=1
            mat[row][char_indx]= pt[char_indx]
            if row==0:
                check=0
                row=1
    for i in range(rails):
        for j in range(len(pt)):
            if mat[i][j] != '':
                ct += mat[i][j]
    return ct
cipher = railfence_encrypt(msg, rails)
print("Encrypted message:", cipher)
