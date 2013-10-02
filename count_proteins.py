#!/usr/bin/env python
import sys
filename = sys.argv[1]

f = open(filename, "r")

total = 0

for line in f:
    if (">" in line and "OS=Homo sapiens" in line):
        total += 1
        
print total
