
from fractions import Fraction
import math

## The group operations. P and Q are points in the plane. A is the coefficient of the x term in the EC equation
## (it doesn't depend on B). 

def ECA(P, Q, A):
    x_1, y_1 = P[0], P[1]
    x_2, y_2 = Q[0], Q[1]
    # The case where x1 != x2
    try:
        m = Fraction(y_2 - y_1, x_2 - x_1)
        x_3 = m**2 - x_1 - x_2
        y_3 = m*(x_1 - x_3) - y_1
    # Handles the case where x1 = x2
    except ZeroDivisionError:
        if y_1 != y_2:
            return 'inf'
        else:
            if y_1 != 0:
                m_t = Fraction(3*x_1**2 + A, 2*y_1)
                x_3 = m_t**2 - 2*x_1
                y_3 = m_t*(x_1 - x_3) - y_1
            else:
                return 'inf'
    return x_3, y_3

## Associativity is hard to prove. But here are some examples. You have to verify first
## that the points are actually on the curve before you can add them together. We'll try y^2 = x^3 - 25x. 

# B, C, D = (0,0), (5,0), (-4,6)
# Check for associativity of B, C, and D. 
# R = ECA(B, C, -25)
# print(f"R = {R}")
# print(ECA(R, D, -25))

# S = ECA(C, D, -25)
# print(f"S = {S}")
# print(ECA(B, S, -25))

## We now implement multiple additions.


## We now implement integer multiplication, starting with doubling (this is faster). 
def doubling(k, point, A):
    X = point
    # k is the exponent of 2. 
    for _ in range(k):
        X = ECA(X, X, A)
    return X

'''An example demonstrating that EC arithmetic mod n is tricky, at least if n is composite.'''
P, Q, A = (1,1), (21,4), -1

# One can see that the denominator of the x-coordinate is 0 modulo 25. What to do?
SUM = ECA(P, Q, A)

'''Another example, this time we want to know if E(Q) -> E(F_7) is a homomorphism. Note that the two points are congruent mod 7,
so mod 7 one would use the tangent line formula to compute the sum. On the other hand, if we did the arithmetic in E(Q) first, 
they are obviously distinct so one does not use the tangent formula. Turns out this isn't a problem, but that's not obvious. '''
P, Q, A = (1,1), (Fraction(571, 361), Fraction(16379, 6859)), 3

SUM = ECA(P, Q, A)
print(SUM)

'''Elliptic curve arithmetic over finite fields'''