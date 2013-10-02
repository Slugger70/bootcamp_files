#!/usr/bin/env python

import sys
from rodents import Rodent


filename = sys.argv[1]

f = open(filename,"r")

rodents = {}

for line in f:
    l = line.strip().split(",")
    if l[0] in rodents:
        rodents[l[0]].add_weight(float(l[1]))
    else:
        rodents[l[0]] = Rodent(l[0])
        rodents[l[0]].add_weight(float(l[1]))
        
for i in rodents:
    print rodents[i].to_string()
