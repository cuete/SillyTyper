#!/usr/bin/env python

#Silly script to print out text from a file with a 
#variable time delay after each line
#See "test" file for input format

from time import sleep
import sys
import random
import os
from termcolor import colored

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

for line in batchfile:
    a,b,c = line.split('\t')
    batch.append(Line(a,int(b),int(c)))

batchfile.close()
os.system('clear')
sys.stdout.write("\033[0;32m")
print ('\n')
sleep(2)

for line in batch:
    chars = list(line.text)
    for c in chars:
        sys.stdout.write(c)
        sys.stdout.flush()
        if not line.charWait:
            spacing = random.uniform(0, 0.2)
        else:
            spacing = float(line.charWait)/1000
        sleep(spacing)
    print ('')
    if line.waitB4ms != 0:
        sleep(line.waitB4ms/1000)

sleep(5)

