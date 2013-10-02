#!/usr/bin/env python
import sys
from collections import defaultdict

s = sys.argv[1]
print s

my_dict = defaultdict(int)

total = 0
for i in s:
	my_dict[i] += 1
	total += 1

for i in my_dict:
	print i,":", my_dict[i]
	
#print my_dict
print "GC content: %3.2f" % (float(my_dict['G'] + my_dict['C'])/float(total))
