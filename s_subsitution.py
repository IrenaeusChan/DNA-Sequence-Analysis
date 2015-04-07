import sys
import string
import random
import csv
import math
import operator
from itertools import imap

substitution = 'ATGC'

""" Weighted Probability... Maybe...
from random import random
from bisect import bisect

def weighted_choice(choices):
    values, weights = zip(*choices)
    total = 0
    cum_weights = []
    for w in weights:
        total += w
        cum_weights.append(total)
    x = random() * total
    i = bisect(cum_weights, x)
    return values[i]

>>> weighted_choice([("A",25), ("T",25), ("G",25), ("C", 25)])
"""

def hammingDistance(s1, s2):
    """
    Hamming distance.
    Counts the number of differences between equal lengths of s1 and s2
    """
    assert len(s1) == len(s2)
    ne = operator.ne
    return sum(imap(ne, s1, s2))

def randomSubstitution(s):
    """
    Apply n substitutions based on the total length of the string (n = 1/10th of String)
    by Irenaeus Chan
    """
    if (len(s) == 0):
        return 0;

    new_string = list(s)
    total_sub = len(s)/10                               #Total number of substituions that must be made
    for i in xrange(total_sub):
        random_index = random.randint(0, len(s)-1)      #Randomly chooses an index in the string
        new_string[random_index] = ''.join([random.choice(substitution)])
    return ''.join(new_string)

def readFile(file_name):
    seq = []
    with open(file_name, "r") as stream:
        for i, line in enumerate(csv.reader(stream, delimiter=",")):
            if i == 10:
                break
            seq.append(line)
    return seq
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "ERROR:  Please provide a file:"
        print "\tTaxon, Process ID, Sample ID, DNA Sequence"
        print "\tDeliminted by Commas"
        sys.exit(1)

    tags = readFile(sys.argv[1]);
    
    for i, line in enumerate(tags):
        print ""
        print tags[i][0] + " " + tags[i][1] + " " + tags[i][2]
        new_string = randomSubstitution(tags[i][3])
        print new_string
        print hammingDistance(new_string, tags[i][3])