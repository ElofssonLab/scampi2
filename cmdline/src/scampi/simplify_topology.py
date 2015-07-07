import os
import sys

topoSeq = ""
headerLine = ""

with open(sys.argv[1]) as inFile:
    for line in inFile:
        if line.find(">") == -1:
           topoSeq += line
        else:
           headerLine = line

with open(sys.argv[1],"w") as outFile:
    outFile.write(headerLine + topoSeq.replace("x","M").replace("y","M").replace("e","M").replace("l","M").replace("J","I").replace("a","M").replace("b","M"))
