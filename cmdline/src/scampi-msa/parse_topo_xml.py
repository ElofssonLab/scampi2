import os
import sys


def simplifyTopo(topoSeq):
    return topoSeq.replace("x","M").replace("y","M").replace("e","M").replace("l","M").replace("J","I").replace("a","M").replace("b","M")

xml_file = sys.argv[1]
outFile = sys.argv[2]

with open(outFile, "w") as outFile:
    with open(xml_file) as inFile:
        seq_name = ""
        topo_seq = ""
        for line in inFile:
            if line.find("pure_seq_name_a") != -1:
                if seq_name != "":
                    outFile.write(">" + seq_name + "\n" + simplifyTopo(topo_seq) + "\n")
                    seq_name = ""
                    topo_seq = ""
                seq_name = line.split(">")[1].split("<")[0]
            if line.find("<label>") != -1:
                topo_seq += line.split(">")[1].split("<")[0]

        outFile.write(">" + seq_name + "\n" + simplifyTopo(topo_seq) + "\n")

        
