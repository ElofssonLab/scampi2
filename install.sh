#!/bin/bash

rundir=`dirname $0`
rundir=`realpath $rundir`

cd $rundir

# 1 install modhmm

tmpdir=$(mktemp -d $rundir/tmpdir.install.XXXXXXXXX) || { echo "Failed to create temp dir" >&2; exit 1; }

cd $tmpdir

cmake -D CMAKE_INSTALL_PREFIX=$rundir/bin $rundir/modhmm
make
make install

rm -rf $tmpdir

tmpdir=$(mktemp -d $rundir/tmpdir.install.XXXXXXXXX) || { echo "Failed to create temp dir" >&2; exit 1; }

cd $tmpdir

# 2 install scampi
cmake -D TARGETS="scampi;scampi-msa" -D CMAKE_PREFIX_PATH=$rundir/bin/modhmm -D CMAKE_INSTALL_PREFIX=$rundir/bin/ $rundir/cmdline
make
make install

rm -rf $tmpdir


