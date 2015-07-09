# scampi2

## Setup
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

 4. Running
  * Scampi-Single: 
    * Command: ./SCAMPI_run.pl <input_fasta> <output_file>
    * <input_fasta> can contain one or more fasta entries
