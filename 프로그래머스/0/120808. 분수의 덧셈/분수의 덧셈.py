from fractions import Fraction

def solution(num1, den1, num2, den2):   
    frac = Fraction(num1, den1) + Fraction(num2, den2)
    return [frac.numerator, frac.denominator]