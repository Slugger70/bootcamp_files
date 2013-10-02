#!/usr/bin/env python

from DNA_sequence import DNA_sequence
from DNA_sequence import RNA_sequence

data = "AGCTCGAAACCAATTGGGCAAA"
RNA = "AGCUCUAGCUAUCGUCUAGAUU"

s = DNA_sequence(data)
r = RNA_sequence(RNA)

print "%3.2f" % s.gc_content()
print s.sequence
print s.reverse_complement()
print "%3.2f" % r.gc_content()
print r.sequence
print r.reverse_complement()

valid = False
x = ""
while not valid:
    try:
        valid = True
        x = raw_input("Please type in a DNA sequence: ")
    except:
        valid = False       
    
dna = DNA_sequence(x)
    
print dna.gc_content()
