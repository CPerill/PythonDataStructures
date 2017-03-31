'''
Created on 19 Mar 2017

@author: perillc
'''
from random import randint
import string

# Function
# function to create the sentence "methinks it is like a weasel" from random characters
# 
# Method:
#    Write function that will generate a string that is 28 characters long
#    Write function to score generated string against goal
#    Write function to repeatedly call these two and score, print progress every 1000 calls
# 

goal = "methinks it is like a weasel"
testString = "methinks it is like a weasel"


letterList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]


def start():
    finished = False
    count = 0
    
    print("Starting")
    while finished == False:
        genString = generateStringSequence()
        #print("STRING: %+10s"%(genString))
        score = scoreStringsequence(genString)
        
        # For making sure code works, uncomment to test comparsion
        #testScore = test()
        
        if score == 100:
            print("Finished!")
            finished = True
            
        #if testScore == 100:
        #    print("Compare works")
        #    finished = True;
            
        count += 1
        
        if count % 10000 == 0:
            print("Still trying. Currently on count %d"%(count))
            
    print("Final count: %d"%(count))

def generateStringSequence():
    string = ''
    
    if not string:
        count = 0
        
        while count <= 27:
            string += str(letterList[randomNumber()])
            count += 1  
            
        return string
    
    else:
        del string
        count = 0
        
        while count <= 26:
            string += str(letterList[randomNumber()])
            count += 1  
            
        return string

def scoreStringsequence(genString):
    
    #print("%s"%(goal))
    #print("%s"%(genString))
    
    #print("String lengths: GOAL: %s and GEN: %s"%(len(goal),len(genString)))
    
    if goal == string:
        print("We got a match!")
        score = 100
        
        return score
    
    score = 55
    return score

def randomNumber():
    number = randint(0, 26)
    #print("Random number is %d"%(number))
    return number

def test():
    if goal == testString:
        print("We got a match for testing!")
        score = 100
        
        return score

start()