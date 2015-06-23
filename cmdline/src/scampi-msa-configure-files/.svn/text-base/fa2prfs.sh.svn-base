#!/bin/bash

set -e

if (( $# < 2 )); then
    echo "Usage: $0 <fasta file> <blast installation directory> <database>";
    exit 1;
fi

bindir="@scampi-msadir@";
infile_path=$1;
filename=`basename $infile_path`
blastdir=$2;
db=$3;

if [[ -s ${infile_path}.prf ]]; then 
    echo "$0: Found file '${infile_path}.mtx', skipping BLAST-run";
    exit ;
else
    echo "No blast result found for ${infile_path}";
fi

$blastdir/bin/blastpgp -i ${infile_path}.fa -d $db -e 1e-3 -v 0 -b 500 -m 6 -a 4 > ${infile_path}.blast
$bindir/msa62fasta_oneround.pl ${infile_path}.blast > ${infile_path}.hits.db
$blastdir/bin/formatdb -i ${infile_path}.hits.db -l /dev/null
$blastdir/bin/blastpgp -j 2 -i ${infile_path}.fa -d ${infile_path}.hits.db -e 1000000 -v 0 -b 1000000 -a 4 -C ${infile_path}.chk -Q ${infile_path}.psi >/dev/null

$bindir/msa62mod_oneround.pl ${infile_path}.blast ${infile_path}.fa > ${infile_path}.raw.prf

@echo_EXECUTABLE@ $filename.chk > ${infile_path}.pn
@echo_EXECUTABLE@ $filename.fa > ${infile_path}.sn
$blastdir/bin/makemat -P ${infile_path}
$bindir/mtx2prf.pl ${infile_path}.mtx
#rm ${infile_path}.hits.db* ${infile_path}.blast formatdb.log error.log ${infile_path}.pn ${infile_path}.sn ${infile_path}.chk ${infile_path}.mtx ${infile_path}.mn ${infile_path}.aux
