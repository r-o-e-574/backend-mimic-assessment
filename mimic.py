#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

"""Mimic exercise

Read in the file specified on the command line.
Do a simple split() on whitespace to obtain all the words in the file.
Rather than read the file line by line, it's easier to read it into
one giant string and split it once.

Note: the standard python module 'random' includes a random.choice(list)
method which picks a random element from a non-empty list.

You can try adding in line breaks around 70 columns so the output looks
better.
"""

__author__ = "Ruben Espino worked with Paul Racisz we found the solution at this github account @geetarista."

import random
import sys


def create_mimic_dict(filename):
    with open(filename, 'r') as textfile:
        mimicDict = {}
        words = textfile.read()
        splitWords = words.split()
        previousWord = ''
        for word in splitWords:
            # previousWord is not in dictionary then add it
            if previousWord not in mimicDict:
                mimicDict[previousWord] = [word]
            # otherwise append the new previous word to previous word
            else:
                mimicDict[previousWord].append(word)
            previousWord = word
    return mimicDict


def print_mimic(mimic_dict, start_word):
    """Given a previously created mimic_dict and start_word,
    prints 200 random words from mimic_dict as follows:
        - Print the start_word
        - Look up the start_word in your mimic_dict and get its next-list
        - Randomly select a new word from the next-list
        - Repeat this process 200 times
    """
    start_word = random.choice(list(mimic_dict.keys()))
    for i in range(200):
        print(start_word, end= " ")
        next_word_list = mimic_dict.get(start_word)
        if next_word_list is None:
            next_word_list = mimic_dict[""]
        start_word = random.choice(next_word_list)


# Provided main(), calls mimic_dict() and print_mimic()
def main():
    if len(sys.argv) != 2:
        print('usage: python mimic.py file-to-read')
        sys.exit(1)

    d = create_mimic_dict(sys.argv[1])
    print_mimic(d, '')


if __name__ == '__main__':
    main()
