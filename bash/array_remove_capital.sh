#! /bin/bash

i=1
while read line
do
    array[ $i ]=`echo "$line" | sed 's/^[A-Z]/./g'`
    (( i++ ))
done

printf "%s " "${array[@]}" | cut -d " " -f 1-${#array[@]}