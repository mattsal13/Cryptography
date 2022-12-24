from fractions import Fraction
import math

## The group operations. P and Q are points in the plane.
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