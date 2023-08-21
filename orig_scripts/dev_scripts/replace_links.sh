#!/bin/bash

input_file="calender_generators/sofprep/sof365.py"
link_file="calender_generators/sofprep/links.txt"

links=()

while read -r line; do
    if [[ "$line" == *"https://"* ]]; then
        links+=("$line")
    fi
done < "$link_file"

for link in "${links[@]}"; do
    echo $link
    sed -i -e "1 s#(link)#${link}#; t" -e "1,// s#(link)#${link}#" $input_file
    sed -i -e "2 s#(link)#${link}#; t" -e "2,// s#(link)#${link}#" $input_file
done