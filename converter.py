#!/usr/bin/env python3
import os
import sys
from member import Member
from csv2vcf import convert_to_vcard


def main() -> None:
    # Input file must be a csv file formatted in the style produced by formie
    path_input = sys.argv[1]
    path_output = "out.csv"

    if not path_input:
        print("usage: python3 converter.py <input csv file>")
        exit(1)

    if not os.path.isfile(path_input):
        print(f"File {path_input} does not exist")

    members: list[Member]
    with open(path_input, 'r') as file:
        members = [Member.parse_list(line.strip().split(','))
                   for line in file.readlines()]

    with open(path_output, 'w') as file:
        for member in members:
            file.write(str(member))

    convert_to_vcard("out.csv", single_output=True, input_file_format={"name":1, "tel":2})

    

if __name__ == "__main__":
    main()
