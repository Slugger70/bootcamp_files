#!/usr/bin/env python

import sys

def base_count(seq,base):
    return seq.count(base)

def gc_content(seq):
    total = len(seq)
    return (base_count(seq, "G") + base_count(seq, "C"))/float(total)
    
print "GC content of sequence: %3.2f" % gc_content(sys.argv[1])
    
