#!/usr/bin/env python

#Silly script to print out text from a file with a 
#variable time delay after each line
#See "test" file for input format

from time import sleep
import sys
import random
import os

class Line:
    def __init__(self, text, waitB4ms, charWait):
         self.text = text
         self.waitB4ms = waitB4ms
         self.charWait = charWait

if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    filename = 'test'
batchfile = open(filename,'r')
batch = []
#random.seed(a=None)

for line in batchfile:
    a,b,c = line.split('\t')
    batch.append(Line(a,int(b),int(c)))

batchfile.close()
os.system('clear')
print ('\n')

for line in batch:
    chars = list(line.text)
    for c in chars:
        sys.stdout.write(c)
        sys.stdout.flush()
        if not line.charWait:
            spacing = random.uniform(0, 0.5)
        else:
            spacing = float(line.charWait)/1000
        sleep(spacing)
    print ('')
    sleep(line.waitB4ms/1000)

print ('\n\n')
sleep(5)

