#!/usr/bin/env python

import sys
import string

def num_unique(x):
	return len(set(string.lowercase).intersection(set(x.lower())))

def num_intersect(x,y):
	return len(set(x.lower()).intersection(set(y.lower())))

print "Number of unique letters in sentence one:", num_unique(sys.argv[1])

print "Number of unique letters in sentence two:", num_unique(sys.argv[2])

print "Number of letters common to sentences one and two:", num_intersect(sys.argv[1],sys.argv[2])

print "Number of letters unique to sentence one:", num_unique(sys.argv[1]) - num_intersect(sys.argv[1],sys.argv[2])
print "Number of letters unique to sentence two:", num_unique(sys.argv[2]) - num_intersect(sys.argv[1],sys.argv[2])


