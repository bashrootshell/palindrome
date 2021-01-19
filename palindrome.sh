#!/usr/bin/env bash

# Palindrome finder - simple implementation in bash

counter=0

if [ -z "$1" ];
  then
    echo "Plese provide a file name."
    exit
fi

for string in $(< $1)
  do
    string_size=${#string}
    string_reversed=$(echo "$string" | rev)
    if [ "$string_reversed" == "$string" ] && [ "$string_size" -ge 10 ];
      then
        let counter++
    fi
  done

echo "There are $counter palindromes in file $1."
