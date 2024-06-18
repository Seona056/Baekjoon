from fractions import Fraction

def solution(num1, den1, num2, den2):   
    answer = Fraction(num1, den1) + Fraction(num2, den2)
    return [answer.numerator, answer.denominator]