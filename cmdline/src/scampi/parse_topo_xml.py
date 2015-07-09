import os
import sys


def simplifyTopo(topoSeq):
    return topoSeq.replace("x","M").replace("y","M").replace("e","M").replace("l","M").replace("J","I").replace("a","M").replace("b","M")

xml_file = sys.argv[1]
outFile = sys.argv[2]
mapFile = sys.argv[3] + "map_header.txt"

dict_map = {}
with open(mapFile) as inFile:
    for line in inFile:
        line_array = line.split(":")
        dict_map[line_array[0]] = line_array[1].strip()

with open(outFile, "w") as outFile:
    with open(xml_file) as inFile:
        seq_name = ""
        topo_seq = ""
        for line in inFile:
            if line.find("pure_seq_name_a") != -1:
                if seq_name != "":
                    outFile.write(">" + dict_map[seq_name] + "\n" + simplifyTopo(topo_seq) + "\n")
                    seq_name = ""
                    topo_seq = ""
                seq_name = line.split(">")[1].split("<")[0]
            if line.find("<label>") != -1:
                topo_seq += line.split(">")[1].split("<")[0]

        outFile.write(">" + dict_map[seq_name] + "\n" + simplifyTopo(topo_seq) + "\n")

        
