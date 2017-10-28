#!/bin/sh

# Usage : List all the jars which has the particual class file

#  Command to run : 
#  ./find_class.sh <source_folder> <class name>

find "$1" -name "*.jar" -exec sh -c 'jar -tf {}|grep -H --label {} '$2'' \;
