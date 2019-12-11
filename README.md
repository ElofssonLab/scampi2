# scampi2

## Setup

### Requirements
1. Python 2.7+
2. CMake

### Easy installation 

    git clone https://github.com/ElofssonLab/scampi2
    cd scampi2
    ./install.sh

After that, scampi2 will be installed in the folder `bin`

### Separated installation
 1. Clone the github repository 
 2. Install modhmm
  * mkdir /tmp/build
  * cd /tmp/build
  * cmake -D CMAKE_INSTALL_PREFIX=/my/install/dir  /this/source/dir
  * make
  * make install

 3. Install cmdline
  * mkdir /tmp/build
  * cd /tmp/build
  * cmake -D TARGETS="scampi;scampi-msa" -D CMAKE_PREFIX_PATH=/path/to/modhmm -D CMAKE_INSTALL_PREFIX=/my/install/dir   /this/source/dir
  * make
  * make install

----
## Usage

### Scampi-Single: 

        ./SCAMPI_run.pl \<input_fasta\> \<output_file\>

* \<input_fasta\> can contain one or more fasta entries

For example:

    bin/scampi/SCAMPI_run.pl test/4seq.fasta test/4seq.out

### Scampi-MSA:

        ./run_SCAMPI_multi.pl \<input_fasta\> \<output_file\> \<blast_dir\> \<blast_db\>

* \<input_fasta\> can contain only one (!) fasta entry

For example (suppose you have `blastpgp` installed at `/usr/bin` and blast
database at `/data/blastdb/uniref90.fasta`):

    bin/scampi-msa/run_SCAMPI_multi.pl test/1seq.fasta test/1seq.scampi-msa.out /usr /data/blastdb/uniref90.fasta

    
