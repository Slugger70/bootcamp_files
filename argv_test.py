#!/usr/bin/env python

import sys
sys.argv.pop(0)
sys.argv.sort()
print (", ".join(sys.argv[:-1]) + " and " + sys.argv[-1] + ".").capitalize()
