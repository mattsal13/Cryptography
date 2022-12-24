from ECC import *


P, Q, R = (1,2), (6,7), (-4,-3)

X = ECA(P, P, -34)

Y = ECA(P, Q, -34)

print(X)

print(Y)