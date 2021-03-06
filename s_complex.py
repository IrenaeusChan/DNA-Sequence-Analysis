"""
String Complexiy Calculations
3 Methods:
    Standard Bit Compression Ratio 
    Shannon's Entropy
    Evolutionairy Method (Randomly Generating String)

by Irenaeus Chan
"""

import sys
import string
import random
import zlib
import csv
import bisect
from math import log

def weightedChoice(choices):
    """
    Raymond Hettinger - http://stackoverflow.com/questions/3679694/a-weighted-version-of-random-choice
    """
    values, weights = zip(*choices)
    total = 0
    cum_weights = []
    for w in weights:
        total += w
        cum_weights.append(total)
    x = random.random()*total
    i = bisect.bisect(cum_weights, x)
    return values[i]

def bitCompress(s):
    """
    Compares the ratio of the compressed string to its original bit size
    by Irenaeus Chan
    """
    if (len(s) == 0):
        return 0;
    else:
        return float(len(zlib.compress(s)))/len(s);                 #Standard Compression

def entropyInBits(S):
    """
    Compute entropy of a string, on a per-character basis.
    by Eddie Ma
    """
    if (len(S) == 0):
        return 0;

    D = len(S)                                                      #Denominator
    N = {}                                                          #Numerators     Dictionary, of (Key, Value)
    for s in S:
        if s not in N: N[s] = 0                                     #If the Char is "new". Create a New Spot for it
        N[s] += 1                                                   #Adds 1 to the Character Count
    p = lambda(s): 1.*N[s]/D                                        
    """Creates a function P(x) = 1.*N[x]/D
    1.* converts the entire value into a float. Same as N[s]/float(D)
    This is the probability of the character appearing in the String"""
    return -sum([p(s)*log(p(s), 2) for s in N])                     #Find the Entropy Summation for every character seen in the String

def evolution(s):
    """ 
    Creates a skeleton string and attempts to randomly build the string using Weighted Averages.
    Tries to build the string Character by Character (Faster)
    by Irenaeus Chan
    """
    if (len(s) == 0):
        return 0
    s = s.upper();

    """
    Creating the Weighted Averages to use for Random Selection
    """
    N = {}                                                          #Numerators     Dictionary, of (Key, Value)
    for char in s:
        if char not in N: N[char] = 0                               #If the Char is "new". Create a New Spot for it
        N[char] += 1

    skeleton = list(''.join('0') for i in xrange(len(s)));          #Creates the skeleton e.g. GATTACA = 000000
    complexity_count = 0;
    used = [];

    for i in xrange(len(skeleton)):
        del used[:]
        c = ''.join([weightedChoice(dict.items(N))]);               #Randomly chooses a character from the dictionary
        used.append(c);
    
        while True:
            """
            Keeps randomly changing each character until the character matches the original string
            Once the character finally matches the original string character, moves on to the next character
            Only ends once it iterates over every single character in the Skeleton String
            """
            complexity_count += 1;

            if (c == s[i]):
                skeleton[i] = c;
                break;              

            c = ''.join([weightedChoice(dict.items(N))]);
            while (c in used):                                      #Ensures no repeats
                c = ''.join([weightedChoice(dict.items(N))]);
            used.append(c);
    complexity_count = 1.*complexity_count/len(s)
    return complexity_count;                                        #Return how many iterations it took to create the word

def readFile(file_name):
    seq = []
    with open(file_name, "r") as stream:
        for i, line in enumerate(csv.reader(stream, delimiter=",")):
            seq.append(line)
    return seq
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "ERROR:  Please provide a file:"
        print "\tTaxon, Process ID, Sample ID, DNA Sequence"
        print "\tDeliminted by Commas"
        sys.exit(1)

    tags = readFile(sys.argv[1]);

    with open("output.txt", "w") as output:
        for i, line in enumerate(tags):
            #print tags[i][0] + " " + tags[i][1] + " " + tags[i][2]
            #print bitCompress(tags[i][3]), entropyInBits(tags[i][3]), evolution(tags[i][3])
            value = str(bitCompress(tags[i][3])) + " " + str(entropyInBits(tags[i][3])) + " " + str(evolution(tags[i][3])) + "\n"
            print tags[i][0] + " " + tags[i][1] + " " + tags[i][2] + " " + value
            output.write(tags[i][0] + " " + tags[i][1] + " " + tags[i][2] + " " + value)