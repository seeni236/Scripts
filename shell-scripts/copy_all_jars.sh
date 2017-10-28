#!/bin/sh

#copy all jar files to one location

find "$1" -name "*.jar" -type file -exec cp {} "$2" \;

""" Command to run : 
 ./cp_all_jars.sh <source_folder> <destination_folder> """