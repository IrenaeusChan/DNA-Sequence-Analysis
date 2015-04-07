# DNA-Sequence-Analysis
Used to analyze the string complexity of over 1 million CO1 gene sequences

s_complex.py
------------
Main code that will read in a file organized as followed:
Taxon, Process ID, Sample ID, DNA Sequence

Will analyze the String Complexity of the given DNA Sequence using three methods:
- Zip File Compression Ratio
- Shannon's Entropy
- Evolutionairy Method

Creates an "output.txt" file with the results of the analysis in the form:
    Zip-File Compression Ratio  Shannon's Entropy   Evolutionairy Method

s_subsitution.py
----------------
Supporting code used for further analysis of the DNA Sequence. Will apply random subsitutions to the existing DNA Sequence
and calculate the Hamming Distance between the new sequence and the original sequence.

Subsitutions are applied based on 1/10th of the original length and the subsitutions to be applied are originally weighted:
  25% A
  25% T
  25% G
  25% C

s_complex_unused_functions.py
-----------------------------
Other functions that were initially used during the testing phase, but ultimately removed due to performance issues or
inefficiency. However, may be useful for further analysis and testing.
