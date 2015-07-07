#!@PERL_EXECUTABLE@ -w

$scampi_dir="@scampidir@";

($infile_withpath=$ARGV[0]) || die("Syntax: SCAMPI_run.pl <fasta_file> <output file>\n");
($outfile_withpath=$ARGV[1]) || die("Syntax: SCAMPI_run.pl <fasta_file> <output file>\n");

$infile=$infile_withpath;
$infile=~ s/.*\///;

$tmpdir=`@mktemp_EXECUTABLE@ -d @tmpdir@/SCAMPI_XXXXXXXXXX`;
chomp($tmpdir);
mkdir("$tmpdir/sequences");
system("@cp_EXECUTABLE@ $infile_withpath $tmpdir");
system("python $scampi_dir/fasta_split.py $tmpdir/$infile $tmpdir/sequences fasta 0 \"|\"");
system("@ls_EXECUTABLE@ -1 $tmpdir/sequences/|@awk_EXECUTABLE@ '{print \"$tmpdir/sequences/\" \$1}' > $tmpdir/snf");
# No -g flag (globular protein filter); corresponds to what's used in paper
system("@modhmms_scampi_EXECUTABLE@ -f fa -s $tmpdir/snf -m $scampi_dir/DGHMM_KR_21.txt -o $tmpdir -r $scampi_dir/replacement_letter_multi.rpl --nopostout --nolabels --viterbi -u -L > $tmpdir/outfile.xml");
system("@cat_EXECUTABLE@ $tmpdir/outfile.xml | @modhmmxml2top_EXECUTABLE@ > $outfile_withpath");
system("python $scampi_dir/simplify_topology.py $outfile_withpath");
system("@rm_EXECUTABLE@ -rf $tmpdir");

