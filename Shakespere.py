"""
Author:     Connor Perill
Program:    String Generator
Usage:      Generates and compares "methinks it is like a weasel"
                Functions:
                    generator
                    genscore (will score each letter out of 27 - next phase)
                    compare
                    
Lesson: http://interactivepython.org/runestone/static/pythonds/Introduction/DefiningFunctions.html
"""

import string
import random

goal = "methinks it is like a weasel"
choices = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
           "v", "w", "x", "y", "z", " "]

finished1 = ''
finished2 = ''

def generator():
    gen = ''
    go = True
    count = 0
    while go:
        while count < 28:
            x = random.choice(choices)
            gen += x
            count += 1
        go = False
    return gen


def genscore(s):


    score = 0
    if goal == s:
        score = 100

    return score


def compare(genstr):
    if goal == genstr:
        return True

    insertstring(genstr)

    if finished == goal:
        return True

    return False

def insertstring(genstring):
    global finished1
    global finished2

    i = 1
    k = 1

    while k <= len(goal):
        if k == 1:
            k += 1
            if goal[:i] == genstring[:i] and genstring[:i] != finished1[:i]:
                finished1 += genstring[:i]
                i += 1

        else:
            k += 1
            if goal[i-1:i] == genstring[i-1:i] and genstring[i-1:i] != finished1[i-1:i]:
                finished2 += genstring[i-1:i]
                i += 1


def start():
    working = True

    print("Program started")
    print("Generating string...")

    count = 0
    while working:
        gen = generator()
        res = compare(gen)

        if res:
            working = False
            print("***STRING COMPLETE***")
            print("Results: %s (goal) equals %s (generated string)" % (goal, gen))
        else:
            count = count + 1
            if count % 10000 == 0:
                print("Count: %s, progress is %s" % (count, finished))


start()
