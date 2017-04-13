'''
Created on 10/04/2017
Author:     Connor Perill
Program:    Fraction Handler
Usage:      fraction class to handle fractions (perform basic functions and display data)
                Functions:
                    Fraction Class
                    gcd (Greatest Common Denominator)
                        for displaying fractions as lowest possible values
                Classes:
                    Fraction
                        the main fraction class
                    
Lesson: http://interactivepython.org/runestone/static/pythonds/Introduction/ObjectOrientedProgramminginPythonDefiningCla
        sses.html
'''

def gcd(m, n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldm
        n = oldm % oldn
    print(n)
    return n

def crossmulitiply(f1num, f1den, f2num, f2den, comparator):
    fract1 = f1num * f2den
    fract2 = f2num * f1den

# Greater than || Greater or equal than
    try:
        if comparator == 'gte':
            if fract1 >= fract2:
                return True
            else:
                return False
        elif comparator == 'gt':
            if fract1 > fract2:
                return True
            else:
                return False
    # Less than || Less or equal than
        elif comparator == 'lte':
            if fract1 <= fract2:
                return True
            else:
                return False
        elif comparator == 'gt':
            if fract1 < fract2:
                return True
            else:
                return False
    except:
        print("!!!ERROR!!!")
        print("Have you forgotten the comparator?")
        print("Have you entered two fractions?")


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def __add__(self, otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.den
        newden = self.den * otherfraction.den

        common = gcd(newnum, newden)

        return Fraction(newnum//common, newden//common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    # Greater than
    def __gt__(self, other):
        # Numerator of first fraction, denominator of the second fraction
        fract1 = self.num * other.den
        # Numerator of  second fraction, denominator of the first fraction
        fract2 = other.num * self.den

        # Compare
        if fract1 > fract2:
            return True
        else:
            return False

    # Greater or equal to
    def __ge__(self, other):
        # Numerator of first fraction, denominator of the second fraction
        fract1 = self.num * other.den
        # Numerator of  second fraction, denominator of the first fraction
        fract2 = other.num * self.den

        # Compare
        if fract1 >= fract2:
            return True
        else:
            return False

    # Less than
    def __lt__(self, other):
        # Numerator of first fraction, denominator of the second fraction
        fract1 = self.num * other.den
        # Numerator of  second fraction, denominator of the first fraction
        fract2 = other.num * self.den

        # Compare
        if fract1 < fract2:
            return True
        else:
            return False

    # Less or equal to
    def __le__(self, other):
        # Numerator of first fraction, denominator of the second fraction
        fract1 = self.num * other.den
        # Numerator of  second fraction, denominator of the first fraction
        fract2 = other.num * self.den

        # Compare
        if fract1 <= fract2:
            return True
        else:
            return False

    def show(self):
        print(self.num,"/",self.den)


x = Fraction(2,3)
y = Fraction(3,5)
# print(x+y)
# print(x == y)

# Should be false
print(x < y)

# Should be false
print(x <= y)

# Should be true
print(x >= y)

x = Fraction(2,3)
y = Fraction(2,3)
# Should be true
print(x >= y)


