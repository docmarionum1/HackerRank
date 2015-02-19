#! /bin/bash

i=1
while read line
do
    array[ $i ]="$line"
    (( i++ ))
done

printf "%s " "${array[@]}" | cut -d " " -f 1-${#array[@]}