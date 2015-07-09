#!/usr/bin/perl -w

use strict;
use File::Temp "tempdir";

if ( $#ARGV < 3 ) {
    printf "Usage: $0 <fasta file> <outfile> <BLAST installation directory> <database>\n";
    exit(1);
}

my $fastafile=$ARGV[0];
my $outfile =$ARGV[1];
my $blastdir = $ARGV[2];
my $blast_db = $ARGV[3];

my $bindir = "@scampi-msadir@";
my $tmpdir = tempdir("@tmpdir@/scampi-msa_tmpdir_XXXXXX");

$ENV{'PATH'}="/bin:/usr/bin";
system("$bindir/fix_fasta.pl $fastafile > $tmpdir/query.fa");
system("@echo_EXECUTABLE@ $bindir/DGHMM_KR_21_multi.hmg > $bindir/DGHMM_KR_21_multi.txt");

print "BLASTing...\n";
system("$bindir/fa2prfs.sh $tmpdir/query $blastdir $blast_db");
print "BLAST finished!\n";

system("@echo_EXECUTABLE@ $tmpdir/query.raw.prf > $tmpdir/query.raw.prf.snf");
system("@echo_EXECUTABLE@ query > $tmpdir/query.pnf");

if(open(IN,"$tmpdir/query.fix")) {
    my $fix_topo = <IN>;
    close(IN);
    $fix_topo =~ /^[iMo\.]+$/ || die;
    relabel_prf_file("$tmpdir/query.prf",$fix_topo);
    relabel_prf_file("$tmpdir/query.raw.prf",$fix_topo);
}

print "Running SCAMPI \n";
system("@modhmms_scampi_EXECUTABLE@ -f prf -s $tmpdir/query.raw.prf.snf -m $bindir/DGHMM_KR_21_multi.txt -r $bindir/replacement_letter_multi.rpl --nopostout --viterbi -u -L > $tmpdir/scampi_modhmmres.xml");
system("python $bindir/parse_topo_xml.py $tmpdir/scampi_modhmmres.xml $outfile");
system("@rm_EXECUTABLE@ -rf $tmpdir");

sub relabel_prf_file {
    my $prffile = shift;
    my $topology = shift;
    if($prffile eq "" || $topology eq "") {
	return;
    }
    else {
	my @topology = split //, $topology;
	
	
	open(PRFFILE, "$prffile")
	    or die "Could not open $prffile";
	
	my $intro = "";
	my @cols = ();
	my $extro = "";
	my $inintro = 1;
	my $inextro = 0;
	my $topopos = 0;
	while(<PRFFILE>) {
	    if($_ =~ "START 1") {
		$intro .= $_;
		$inintro = 0;
	    }
	    if($_ =~ "END 1") {
		$inextro = 1;
	    }
	    if($_ =~ 'ALPHABET' && $inextro <= 0) {
		$intro .= $_;
	    }
	    if($_ =~ 'COL ') {
		chomp;
		$_ =~ s/\s+/ /g;
		my @col = split /\s/, $_;
		$col[$#col - 1] = $topology[$topopos];
		push @cols, [@col];
		$topopos++;
	    }
	    if($inintro > 0) {
		$intro .= $_;
	    }
	    if($inextro > 0) {
		$extro .= $_;
	    }
	    
	}
	close PRFFILE;
	open OUTFILE, ">"."$prffile"
	    or die "Could not open $prffile for writing";
	print OUTFILE "$intro";
	for(my $i = 0; $i <= $#cols; $i++) {
	    my @col = @{$cols[$i]};
	    printf OUTFILE "COL %4d", $i+1;
	    print OUTFILE ":  ";
	    for $b (2 .. $#col ) {
		if($b >= ($#col - 1)) {
		    print OUTFILE "$col[$b]       ";
		}
		else {
		    printf OUTFILE "%5.02f   ", $col[$b];
		}
	    }
	    print OUTFILE "\n";
	}
	print OUTFILE "$extro";
	close OUTFILE;
    }
    return;
}
