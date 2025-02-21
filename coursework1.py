# -*- coding: utf-8 -*-
"""
MATH20621 - Coursework 1
Student name: Wei Chung-Yu
Student id:   10680317
Student mail: chung-yu.wei@student.manchester.ac.uk
"""
import math

# Problem 1

def limiter(a, b, limitertype="mean"):
    if limitertype == "WENO":
        w_a = 1.0 / (a**2 + 1e-6)  
        w_b = 1.0 / (b**2 + 1e-6)
        result = (w_a * a + w_b * b) / (w_a + w_b)
    elif limitertype == "MINMOD":
        if a * b > 0:
            result = min(2 * a, 2 * b, (a + b) / 2)
        elif a < 0 or b < 0 :
            result = 0
    else:
        result = (a + b) / 2

    return float(result)



# Problem 2

def pow_mod(a, b, c):
    if a < 0 or b < 0 or c <= 0:
        raise ValueError("a and b must be positive integers, and c must be a positive integer greater than 0")

    result = 1
    a = a % c
    
    while b > 0:
        if b % 2 == 1:
            result = (result * a) % c 
        a = (a * a) % c 
        b = b // 2

    return result


# Problem 3


def is_prime(n):
    if n < 2:
        return False
    for k in range(2, n):
        if n % k == 0:
            return False
    return True

def two_knodel(m):
    if ((m <= 2) | is_prime(m)):
        return False
    for i in range(2, m):
        if math.gcd(i, m) == 1 and pow_mod(i, m-2, m) != 1:
            return False
        return True


def main():
    # TODO (optional): do any testing you wish here
    # This main function will not be assessed
    print("should return 0:   ", limiter(-0.5, -4, 'MINMOD'))
    print("should return 0.120001...:   ", limiter(0.1, 0.2, 'WENO'))
    print("should return 5...:   ", pow_mod(3,5,7))
    print("should return False:  ", two_knodel(9))
    print("should return True:  ", two_knodel(480))
    
main() # call main() function to run all tests