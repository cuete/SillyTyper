#!/usr/bin/env python

#Silly script to print out text from a file with a 
#variable time delay after each line
#See "test" file for input format

from time import sleep
import sys

class Line:
    def __init__(self, text, waitB4ms):
         self.text = text
         self.waitB4ms = waitB4ms

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = 'test'
batchfile = open(filename,'r')
batch = []

for line in batchfile:
    a,b = line.split(",")
    batch.append(Line(a,int(b)))

batchfile.close()
print "\n"

for line in batch:
    print line.text
    sleep(line.waitB4ms/1000)

print '\n\n'
