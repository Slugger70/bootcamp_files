#!/usr/bin/env python
#this is a really crap program
l = 20
s = "apple"
x = s + str(" "*(l - len(s)))
print len(x),x
c = s.ljust(20)
print len(c),c
