#!/usr/bin/perl -w

open(IN,$ARGV[0]) || die("Could not open file");
while($id=<IN>) {
    $seq="";
    while($row = <IN>) {
        if ($row =~ /^>/) {
	    seek IN, -1*length($row), 1;
	    last;
	}
	$seq .= $row;
    }
    $id =~ s/^>//;
    chomp($id,$seq);
    $seq =~ s/\s//g;
    print ">$id\n$seq\n";
}
