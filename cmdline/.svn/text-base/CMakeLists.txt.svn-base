cmake_minimum_required(VERSION 2.6)


INCLUDE(CPack)


SET(CPACK_PACKAGE_VERSION_MAJOR "1")
SET(CPACK_PACKAGE_VERSION_MINOR "1")
SET(CPACK_PACKAGE_VERSION_PATCH "0")
set(PACKAGE_VERSION ${CPACK_PACKAGE_VERSION_MAJOR}.${CPACK_PACKAGE_VERSION_MINOR}.${CPACK_PACKAGE_VERSION_PATCH})
SET(CPACK_DEBIAN_PACKAGE_DEPENDS "libxml2 (>= 2.6.16 )")


SET(CPACK_SOURCE_GENERATOR TGZ;ZIP)
# SET(CPACK_RPM_PACKAGE_ARCHITECTURE "i386")
SET(CPACK_PACKAGE_CONTACT "erik.sjolund@sbc.su.se") 
SET(CPACK_PACKAGE_DESCRIPTION_SUMMARY "This is a set of programs  (OCTOPUS, SCAMPI, PRODIV, SPOCTOPUS and TOPCONS) is a set of software for TM predictions using modhmm)")
SET(CPACK_PACKAGE_VENDOR "Hakan Viklund, Erik Sjölund")
#SET(CPACK_PACKAGE_DESCRIPTION_FILE "${CMAKE_CURRENT_SOURCE_DIR}/README")
#SET(CPACK_RESOURCE_FILE_LICENSE "${CMAKE_CURRENT_SOURCE_DIR}/COPYING")
SET(CPACK_PACKAGE_INSTALL_DIRECTORY "${CMAKE_PROJECT_NAME}-${PACKAGE_VERSION}")
SET(CPACK_RPM_PACKAGE_LICENSE "GPL")
SET(CPACK_RPM_PACKAGE_RELEASE "1")


SET(CPACK_SOURCE_PACKAGE_FILE_NAME "${CMAKE_PROJECT_NAME}-${PACKAGE_VERSION}")

macro(my_find_program progname)
  find_program(${progname}_EXECUTABLE ${progname})
  IF(NOT ${progname}_EXECUTABLE)
    message(FATAL_ERROR  "${progname} not found" )
  ENDIF(NOT ${progname}_EXECUTABLE)
endmacro(my_find_program)

my_find_program(echo)
my_find_program(wc)
my_find_program(cp)
my_find_program(mktemp)
my_find_program(mkdir)
my_find_program(sort)
my_find_program(awk)
my_find_program(ipcrm)
my_find_program(pwd)
my_find_program(head)
my_find_program(cat)
my_find_program(nohup)
my_find_program(chmod)
my_find_program(ls)
my_find_program(find)
my_find_program(rm)
my_find_program(xargs)
my_find_program(grep)
my_find_program(sed)
my_find_program(ps)
my_find_program(date)
my_find_program(basename)
my_find_program(mv)


IF(NOT TARGETS)
  SET( TARGETS scampi spoctopus topcons prodiv_tmhmm topcons_single zpred scampi-msa)
ENDIF(NOT TARGETS)

my_find_program(modhmmxml2res)
my_find_program(modhmmxml2top)
my_find_program(modhmmt)
my_find_program(modhmms)




include(FindPerl)
IF(NOT PERL_FOUND)
  message(FATAL_ERROR  "perl not found" )
ENDIF(NOT PERL_FOUND)


# include(FindImageMagick)
# IF(NOT ImageMagick_convert_FOUND)
#   message(FATAL_ERROR  "convert ( a part of Imagemagick ) were not found" )
# ENDIF(NOT ImageMagick_convert_FOUND)

execute_process( COMMAND date "+%F"
COMMAND tr -d "\n"
OUTPUT_VARIABLE date
)

SET(PERMS OWNER_WRITE OWNER_READ OWNER_EXECUTE GROUP_READ GROUP_EXECUTE  WORLD_READ WORLD_EXECUTE )
SET(GENEROUSPERMS OWNER_WRITE OWNER_READ OWNER_EXECUTE GROUP_READ GROUP_WRITE GROUP_EXECUTE  WORLD_READ WORLD_WRITE WORLD_EXECUTE )

IF(NOT CMAKE_INSTALL_PREFIX)
 SET ( CMAKE_INSTALL_PREFIX "/usr/local")
ENDIF(NOT CMAKE_INSTALL_PREFIX)

IF(NOT tmpdir)
 SET ( tmpdir "/tmp" )
ENDIF(NOT tmpdir)

macro(instmacro target)
  set ( ${target}dir ${CMAKE_INSTALL_PREFIX}/${target} )
  install(DIRECTORY DESTINATION ${CMAKE_INSTALL_PREFIX}/${target} DIRECTORY_PERMISSIONS ${PERMS} )
  file(GLOB_RECURSE conffiles RELATIVE @CMAKE_CURRENT_SOURCE_DIR@ @CMAKE_CURRENT_SOURCE_DIR@/src/${target}-configure-files/*  PATTERN "*/.svn" EXCLUDE  PATTERN "*/.svn/*" EXCLUDE )
  foreach(i ${conffiles})
    configure_file(${CMAKE_CURRENT_SOURCE_DIR}/${i} ${CMAKE_CURRENT_BINARY_DIR}/${i} @ONLY)
  endforeach(i)
  install(DIRECTORY @CMAKE_CURRENT_SOURCE_DIR@/src/${target}/ DESTINATION ${CMAKE_INSTALL_PREFIX}/${target} FILE_PERMISSIONS ${PERMS}  DIRECTORY_PERMISSIONS ${PERMS} PATTERN ".svn" EXCLUDE PATTERN "*~" EXCLUDE )
  install(DIRECTORY @CMAKE_CURRENT_BINARY_DIR@/src/${target}-configure-files/ DESTINATION ${CMAKE_INSTALL_PREFIX}/${target} FILE_PERMISSIONS ${PERMS}  DIRECTORY_PERMISSIONS ${PERMS} PATTERN ".svn" EXCLUDE PATTERN "*~" EXCLUDE )
endmacro(instmacro)



list(FIND TARGETS spoctopus findvar)
if( ${findvar}  GREATER -1 )
  list(APPEND modhmmtargets octopus spoctopus)
  add_subdirectory (src/spoctopus/score_nn)
endif( ${findvar}  GREATER -1 )

list(FIND TARGETS topcons findvar)
if( ${findvar}  GREATER -1 )
  list(APPEND modhmmtargets general)
endif( ${findvar}  GREATER -1 )

list(FIND TARGETS scampi findvar)
if( ${findvar}  GREATER -1 )
  list(APPEND modhmmtargets scampi)
endif( ${findvar}  GREATER -1 )

list(FIND TARGETS prodiv_tmhmm findvar)
if( ${findvar}  GREATER -1 )
  list(APPEND modhmmtargets general)
endif( ${findvar}  GREATER -1 )

list(FIND TARGETS zpred findvar)
if( ${findvar}  GREATER -1 )
    list(APPEND modhmmtargets general)
    my_find_program(dmesg)
endif( ${findvar}  GREATER -1 )

list(FIND TARGETS topcons_single findvar)
if( ${findvar}  GREATER -1 )
    list(APPEND modhmmtargets general)
    my_find_program(modhmmxml2top)
    my_find_program(toppred)
    my_find_program(memsat)
    my_find_program(hmmtop)
endif( ${findvar}  GREATER -1 )

list(FIND TARGETS scampi-msa findvar)
if( ${findvar}  GREATER -1 )
  my_find_program(modhmmxml2top)
  list(APPEND modhmmtargets scampi)
endif( ${findvar}  GREATER -1 )

list(REMOVE_DUPLICATES modhmmtargets)


foreach(i ${modhmmtargets})
  set(suffix "_${i}")
  if(${i} STREQUAL general)
   set(suffix "")
  endif(${i} STREQUAL general)
  my_find_program(modhmms${suffix})
  my_find_program(modhmmt${suffix})
  my_find_program(modseqalign${suffix})
  my_find_program(add_alphabet${suffix})
endforeach(i)

foreach(i ${TARGETS})
  instmacro(${i})
endforeach(i)
