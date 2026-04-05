import random,math
msg = input("Enter the message to encrypt: ").replace(" ","")

def genprimes(n1,n2):
    primes=[]
    for i in range(n1,n2+1):
        if i>1:
            for j in range(2,i):
                if i%j ==0:
                    break
            else:
                primes.append(i)
    return primes

def genPUPRkeys():
    p = random.choice(genprimes(20,50))
    q = random.choice(genprimes(60,90))
    n=p*q
    phi = (p-1)*(q-1)

    #1<e<phi
    e=2
    while (e<phi):
        if math.gcd(e,phi) == 1:
            break
        e+=1

    i=1
    while True:
        d=((phi*i)+1)/e

        if int(d) == d:
            break

        i+=1

    return[e,d,n]

def rsaencrypt(e,n,msg):
    codes = [ord(sym) for sym in msg]

    ct = [chr((pt**e) % n ) for pt in codes]
    return ct

def rsadecrypt(d,n,cipher):
    codes = [ord(sym) for sym in cipher]

    pt = [chr((ct**int(d)) % n ) for ct in codes]
    return pt

keys=genPUPRkeys()
e=keys[0]
d=keys[1]
n=keys[2]

ctxt = rsaencrypt(e,n,msg)
print("Cipher", ctxt)
print("Decrypted", rsadecrypt(d,n,ctxt))
