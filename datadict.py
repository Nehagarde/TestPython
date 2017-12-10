#PYLINT STANDARDS

#Load data from json
"""This module Loads data from json"""

import json
from difflib import get_close_matches
DAT = json.load(open("/home/neha/Practice_Project/env2/bin/app1dictionary/data.json"))


def fetchmeaning(word):
    """This function fetches data from json file"""
    word = word.lower()
    lengthofls = len(get_close_matches(word, DAT.keys())) > 0
    if word in DAT:
        return DAT[word]
    elif word.title() in DAT:
        return DAT[word.title()]
    elif word.upper() in DAT:
        return DAT[word.upper()]     
    elif lengthofls > 0:
        yesno = input("Did u mean %s? " % get_close_matches(word, DAT.keys())[0])
        if yesno == 'Y':
            return DAT[get_close_matches(word, DAT.keys())[0]]
        elif yesno == 'N':
            return "Word Does not Exists"
        else:
            return "Invalid User Input"
    else:
        return "Word doesn't exist."

USRINP = input("Enter a word to find out its meaning: ")


RES = fetchmeaning(USRINP)

if isinstance(RES, list):
    for eachitem in RES:
        print(eachitem)
else:
    print(RES)
