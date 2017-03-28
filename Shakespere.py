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

finished = ''
finding = True
counting =1


def generator():
    gen = ''
    global finding
    i = 1
    firstgo = True
    global counting

    while finding:
        counting += 1
        print(counting)
        x = random.choice(choices)

        if x != gen[:i] and firstgo is True and x == goal[:i]:
            gen += x
            i += 1
            firstgo = False
            if gen == goal:
                finding = False
                return gen
        elif x != gen[i-1:i] and firstgo is False and x == goal[i-1:i]:
                gen += x
                i += 1
                if gen == goal:
                    finding = False
                    return gen
        elif counting % 10 == 0:
                print("Count: %s, progress is %s" % (counting, finished))


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
    global finished

    i = 1
    k = 1

    while k <= len(goal):
        if k == 1:
            k += 1
            if goal[:i] == genstring[:i] and genstring[:i] != finished[:i]:
                finished += genstring[:i]
                print(finished)
                i += 1

        else:
            k += 1
            if goal[i-1:i] == genstring[i-1:i]:
                if genstring[i-1:i] != finished[i-1:i]:
                    print("goal: %s and gen: %s" % (goal[i - 1:i], genstring[i - 1:i]))
                    raw_input("Press Enter to continue...")
                    finished += genstring[i-1:i]
                    print(finished)
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
            if count % 100000 == 0:
                print("Count: %s, progress is %s" % (count, finished))


start()
