print("public values")
p= 7
g= 11
x=4
y=2
R1 = g**x % p
R2 = g**y % p
K1=R2**x % p
K2=R1**y % p
print("Shared Keys:")
print("Shared Key obtained for Party1:" , K1)
print("Shared Key obtained for Party2:" , K2)


def diffie_hellman(p, g, x, y):
    print("Public Values:")
    print("p:", p)
    print("g:", g)
    R1 = g**x % p
    R2 = g**y % p
    K1=R2**x % p
    K2=R1**y % p
    S= g**(x*y) % p
    print("Shared Keys:")
    print("Shared Key obtained for Party1:", K1)
    print("Shared Key obtained for Party2:", K2)
    print("Shared Key obtained from formula:",S)
    return K1,K2,S

print(diffie_hellman(7,3,4,2))
