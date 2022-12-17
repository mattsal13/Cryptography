## The group operations. P and Q are points in the plane.
def ECA_real(P, Q, A):
    x_1, y_1 = P[0], P[1]
    x_2, y_2 = Q[0], Q[1]
    # The case where x1 != x2
    try:
        m = (y_2 - y_1)/(x_2 - x_1)
        x_3 = m**2 - x_1 - x_2
        y_3 = m*(x_1 - x_2) - y_1
    # Handles the case where x1 = x2
    except ZeroDivisionError:
        if y_1 != y_2:
            return 'inf'
        else:
            if y_1 != 0:
                m_t = (3*x_1**2 + A)/(2*y_1)
                x_3 = m_t**2 - 2*x_1
                y_3 = m_t*(x_1 - x_3) - y_1
            else:
                return 'inf'
    return x_3, y_3

## Associativity is hard to prove. But here are some examples.
# B, C, D = (0,4), (2,-5), (4, 9)

# print(ECA_real(ECA_real(B, C, -2), D, -2))
# print(ECA_real(B, ECA_real(C, D, -2), -2))