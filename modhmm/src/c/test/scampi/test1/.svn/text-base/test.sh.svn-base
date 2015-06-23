#!/bin/sh

set -e
@modhmms_scampi_exe@  -f fa -s @CMAKE_CURRENT_BINARY_DIR@/snf.1 -m @CMAKE_CURRENT_BINARY_DIR@/hmg.list -o @CMAKE_CURRENT_BINARY_DIR@ -r @CMAKE_CURRENT_SOURCE_DIR@/replacement_letter_multi.rpl --nopostout --nolabels --viterbi -u -L -g | @xsltproc_EXECUTABLE@ @CMAKE_SOURCE_DIR@/src/xslt/xml2res.xsl - > @CMAKE_CURRENT_BINARY_DIR@/DGHMM_KR_21_single.1.hmg.res

diff --brief @CMAKE_CURRENT_BINARY_DIR@/DGHMM_KR_21_single.1.hmg.res @CMAKE_CURRENT_SOURCE_DIR@/DGHMM_KR_21_single.1.hmg.res
