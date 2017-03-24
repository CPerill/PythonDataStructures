"""
Author:     Connor Perill
Program:    String Generator
Usage:      Generates and compares "methinks it is like a weasel"
                Functions:
                    StringGenerator
                    StringScore
                    StringCompare
"""

import string
import random

goal="methinks it is like a weasel"
choices=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]

def stringGenerator():
    genString=''
    go=True
    count = 0
    while go==True:
        while count<28:
            '''num=random.randint(0,1)
            if num == 1:
                genString += random.choice(string.letters)
            else:
                genString += " "
            '''
            x=random.choice(choices)
            print(x)
            genString += x
            count += 1
        go=False
    return genString

def stringScore(s):
    score=0
    return score

def stringCompare(goal, string):
    return

def start():
    print("Program started")
    "print(string.lowercase)"

    test = stringGenerator()

start()