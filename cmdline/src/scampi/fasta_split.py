#!/usr/bin/python

import sys,re,os;
import tempfile;

def generateFasta(strFasta, tmpdir = '/tmp') :
    foo, tmpfilepath = tempfile.mkstemp(dir = tmpdir, suffix = '.fa', prefix = 'fasta_split_tmp_', text = True);
    flh = file(tmpfilepath, 'w');
    print >>flh, strFasta;
    flh.close();
    for strTitle, strSeq in generateFastaFromFile(tmpfilepath) :
        yield strTitle, strSeq;
    os.remove(tmpfilepath);

def generateFastaFromFile(strFastaFile):
    print "generateFastaFromFile"
    strTitle = "";
    strSeq = "";

    flhFasta = file(strFastaFile);
    for strLine in flhFasta :
        # Handle case where we have 'ACDA>sp|NextTitle|Foo' (yes it happens)
        intGtIndex = strLine.find('>');
        if intGtIndex != -1 :
            # Found a '>': Store 'ACDA' to previous sequence, '>sp|NextTitle|Foo' to current line
            strSeq += strLine[:intGtIndex];
            strLine = strLine[intGtIndex:];
            # If not the first time; yield previous record to caller
            if strTitle != "" :
                yield strTitle, strSeq;
            # Start construction of current record
            strTitle = strLine.strip().lstrip('>');
            strSeq = "";
        elif re.match('[A-Za-z.-]+', strLine) :
            strSeq += strLine.strip();
    # Yield trailing last record
    yield strTitle, strSeq;
    flhFasta.close();

def saveFile(title, seq, outdir, iCounter, seqtype="fasta", intNameColumn = 1):#splitchar = '|') :
    strFilename = "";
    #if seqtype == "fasta" :
    #    strFilename = title.split(splitchar)[intNameColumn].split()[0] + '.fa';
    #elif seqtype == 'top' :
    #    strFilename = title.split(splitchar)[intNameColumn].split()[0] + '.top';
    #else :
    #    raise Exception("Unrecognised filetype ('%s')" % seqtype);
    
    flhOut = file(os.path.join(outdir, "seq_" +str(iCounter)), 'w');
    print >>flhOut, ">%s\n%s" % (title, seq);
    flhOut.close();

def splitToSmaller(fasta_file_path, outdir, seqs_per_outfile = 10, seqtype="fasta", name_column = 1, split_char = '|') :
    print "splitToSmaller"
    strFilenameBase = "fasta_%dseqs_" % seqs_per_outfile;

    intCounter = 0;
    strToSave = '';
    for title, seq in generateFastaFromFile(fasta_file_path) :
        # Define filename after first sequence
        if intCounter == 0 :
            if seqtype == "fasta" :
                strFilename = strFilenameBase + title.split(split_char)[name_column].split()[0] + '.fa';
            elif seqtype == 'top' :
                strFilename = strFilenameBase + title.split(split_char)[name_column].split()[0] + '.top';
            else :
                raise Exception("Unrecognised filetype ('%s')" % seqtype);
        # Add to string to save
        strToSave += ">%s\n%s\n" % ( title, seq );

        intCounter += 1;
        
        # Print to file if enough seqs stored
        if intCounter == seqs_per_outfile :
            # print
            flhOut = file(os.path.join(outdir, strFilename), 'w');
            flhOut.write(strToSave);
            flhOut.close();
            # reset
            intCounter = 0;
            strToSave = '';
    # Save trailing sequences
    flhOut = file(os.path.join(outdir, strFilename), 'w');
    flhOut.write(strToSave);
    flhOut.close();
        
    

if __name__ == '__main__' :
    # Check, parse $argv
    strUsage = "Usage: %s <fasta/top file> <outdir> <fasta/top> [filename column number] [field separator]";
    if ( len(sys.argv) < len(strUsage.split('<')) ) :
        print >>sys.stderr, strUsage % os.path.basename(sys.argv[0]);
        sys.exit(1);

    strFastafile = sys.argv[1];
    strOutdir = sys.argv[2];
    strSeqtype = sys.argv[3];
    
    intColumn = None;
    if len(sys.argv) > 4 :
        intColumn = int(sys.argv[4]);

    strSplitchar = None;
    if len(sys.argv) > 5 :
        strSplitchar = sys.argv[5];
    
    flhFasta = file(strFastafile);
    fasta = flhFasta.read();
    flhFasta.close();
    iCounter = 0
    with open(strOutdir.replace("sequences","map_header.txt"),"w") as outFile:
        for t, s in generateFasta(fasta) :
            saveFile(t,s,strOutdir,iCounter,strSeqtype, intColumn)
            outFile.write("seq_" + str(iCounter) + ":" + t + "\n")
            iCounter += 1
