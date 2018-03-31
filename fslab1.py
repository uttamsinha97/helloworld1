# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 19:40:50 2018

@author: UttamSinha
"""
file1name = input ('enter file name')
infile = open("file1name","w")
file2name = input ('enter file name')
outfile = open("file1name","w")

# note: I have rewrittent the code to iterate using a for loop instead of a while loop; it's much simpler that way!
# aline = infile.readline()
# while aline:
for aline in infile:
    items = aline.split()
    dataline = items[1] + ',' + items[0]
    outfile.write(dataline + '\n')
#    aline = infile.readline()

infile.close()
outfile.close()