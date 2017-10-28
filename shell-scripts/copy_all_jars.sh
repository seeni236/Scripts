#!/bin/sh

# Usage : copy all jar files to one location

#  Command to run : 
#  ./cp_all_jars.sh <source_folder> <destination_folder>

find "$1" -name "*.jar" -type file -exec cp {} "$2" \;

