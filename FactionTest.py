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
        if comparator == 'ge':
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
        elif comparator == 'le':
            if fract1 <= fract2:
                return True
            else:
                return False
        elif comparator == 'lt':
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
        return crossmulitiply(self.num, self.den, other.num, other.den, 'gt')

    # Greater or equal to
    def __ge__(self, other):
        return crossmulitiply(self.num, self.den, other.num, other.den, 'ge')

    # Less than
    def __lt__(self, other):
        return crossmulitiply(self.num, self.den, other.num, other.den, 'lt')

    # Less or equal to
    def __le__(self, other):
        return crossmulitiply(self.num, self.den, other.num, other.den, 'le')

    # Multiply
    def __mul__(self, other):
        top = self.num * other.num
        bottom = self.den * other.den

        if top%bottom == top:
            return Fraction(top/top, bottom/top)
        else:
            return Fraction(top, bottom)

    # Division
    def __div__(self, other):

        top =  self.num * other.den
        bottom = self.den * other.num

        result = Fraction(top,bottom)

        if top%bottom == 0:
            return top/bottom
        else:
            return Fraction(top,bottom)

    def show(self):
        print(self.num,"/",self.den)


x = Fraction(1,2)
y = Fraction(2,4)

print(x/y)
print (y*x)
