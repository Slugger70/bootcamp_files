#!/usr/bin/env python

import sys

def is_even(x):
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"
        
def minor_major(x):
    if(0 < x < 50):
        return "Minor"
    elif(50 <= x < 1000):
        return "Major"
    else:
        return "Severe"

print is_even(int(sys.argv[1]))
print minor_major(int(sys.argv[1]))

total = 0
for i in [85.0,75.0,95.0,110.0,56.0]:
    total += i
    
print total
