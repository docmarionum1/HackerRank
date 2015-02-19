#! /bin/bash

i=1
while read line
do
    array[ $i ]="$line"
    (( i++ ))
done

printf "%s " "${array[@]:4:5}" | cut -d " " -f 1-${#array[@]:4:5}