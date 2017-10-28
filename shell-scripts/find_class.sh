#!/bin/sh

# Usage : search particular class in all jars

#  Command to run : 
#  ./find_class.sh <source_folder> <class name to search>

find "$1" -name "*.jar" -exec sh -c 'jar -tf {}|grep -H --label {} '$2'' \;
