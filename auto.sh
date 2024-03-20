#!/usr/bin/env bash
set -e
set -x
here="$(realpath "$(dirname "$0")")"
cd "$here"

last_line="$(tail -1 out.csv)"
n_line=$(grep -n "$last_line" out.csv | cut -d':' -f1)
((n_line+=1))
./export.sh
tail +"$n_line" out.csv > autotail.csv
[[ ! -s autotail.csv ]] && echo "no new members" && exit 2
./converter.py autotail.csv
cp all_contacts.vcf ~

