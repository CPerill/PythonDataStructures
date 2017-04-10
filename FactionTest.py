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

def multiplyer(self, newden):
    # Now that we have gcd, we need to rearrange top numbers, multiply NUM by # of times DEN divides into gcd
    while self.den % newden != 0:
        return False

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
        #first we gcd for comparison
        common = gcd(self.den, other.den)

        #Now that we have gcd, we need to rearrange top numbers, multiply NUM by # of times DEN divides into gcd
        multiplyer(self.den, common)

        return False

    #Greater or equal to
    def __ge__(self, other):
        return False


    #Less than
    def __lt__(self, other):
        return False


    #Less or equal to
    def __le__(self, other):
        return False


    def show(self):
        print(self.num,"/",self.den)


x = Fraction(2,3)
y = Fraction(3,5)
print(x+y)
print(x == y)


