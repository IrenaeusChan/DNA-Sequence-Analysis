import operator
import time
from itertools import imap

def levenshteinDistance (s1, s2):
    """
    Levenshtein distance.
    Counts the total number of changes required to make s1 equal to s2
    """
    if len(s1) < len(s2):                           #Length of s1 must be >= s2
        return levenshteinDistance(s2, s1);

    if len(s2) == 0:                                #Special comparison case for no value
        return len(s1);

    previous_row = range(len(s2) + 1);
    for i, char1 in enumerate(s1):
        current_row = [i + 1];
        for j, char2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1;    #j+1 because prev_row and cur_row are longer by 1
            deletions = current_row[j] + 1;
            substitutions = previous_row[j] + (char1 != char2);
            current_row.append(min(insertions, deletions, substitutions));
        previous_row = current_row;

    return previous_row[-1];

def hammingDistance(s1, s2):
    """
    Hamming distance.
    Counts the number of differences between equal lengths of s1 and s2
    """
    assert len(s1) == len(s2)
    ne = operator.ne
    return sum(imap(ne, s1, s2))

def evolutionMethod(s):
    """
    Creates a skeleton string and attempts to randomly build the string.
    The competitive measurement used for the "evolution" is Hamming Distance
    Tries to build the entire string at once (Slower)
    by Irenaeus Chan
    """
    if (len(s) == 0):
        return 0;
    
    s = s.upper();
    skeleton = list(''.join('0' for i in xrange(len(s))));          #Creates the skeleton e.g. GATTACA = 000000
    complexity_count = 0;
    used = [];
    
    c = ''.join([random.choice(stringSet)]);
    used.append(c);                                 #Randomly chooses a character

    while True:
        """
        Goes through the entire skeleton string changing each letter at a time
        If the changed letter helps decrease the levenshtein's distance, then the character is changed
        else the character remains the same
        """
        complexity_count += 1;
        for i in xrange(len(skeleton)):
            old = ''.join(skeleton);
            skeleton[i] = c;
            new = ''.join(skeleton);

            if (hammingDistance(new, s) < hammingDistance(old, s)):   #Checks to see if the new string is closer to the original word
                skeleton = list(new);
            else:                                                     #Else, just use the old word (before the change)
                skeleton = list(old);
        if (hammingDistance(old, s) == 0 or hammingDistance(new, s) == 0):     #If the two words are the same, exit
            break;  
        
        c = ''.join([random.choice(stringSet)]);
        while (c in used):                          #Ensures no repeats
            c = ''.join([random.choice(stringSet)]);
        used.append(c);
    return complexity_count;                        #Return how many iterations it took to create the word

def speedTest(size):
    """
    Used to test which functions are faster
    by Irenaeus Chan
    """
    str1 = ''.join(random.choice(stringSet) for n in range(size))

    print i
    for func in (func1, func2, func3):                              #Make sure to replace func1, func2, and func3 with an actual function
        t1 = time.time()
        func(str1)
        func(str1)
        func(str1)
        func(str1)
        func(str1)
        func(str1)
        func(str1)
        func(str1)
        func(str1)
        func(str1)
        t2 = time.time()
        print t2-t1,
    print