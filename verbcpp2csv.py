#!/usr/bin/env python3

import argparse
import csv
from pathlib import Path

fieldnames = [
        "Identifier",
        "Translation",
        "Infinitif",
        "Participe Présent",
        "Présent - je",
        "Présent - tu",
        "Présent - il",
        "Présent - elle",
        "Présent - nous",
        "Présent - vous",
        "Présent - ils",
        "Présent - elles",
        "Imparfait - je",
        "Imparfait - tu",
        "Imparfait - il",
        "Imparfait - elle",
        "Imparfait - nous",
        "Imparfait - vous",
        "Imparfait - ils",
        "Imparfait - elles",
        "Futur - je",
        "Futur - tu",
        "Futur - il",
        "Futur - elle",
        "Futur - nous",
        "Futur - vous",
        "Futur - ils",
        "Futur - elles",
        "Passé composé - je",
        "Passé composé - tu",
        "Passé composé - il",
        "Passé composé - elle",
        "Passé composé - nous",
        "Passé composé - vous",
        "Passé composé - ils",
        "Passé composé - elles",
        "Plus-que-parfait - je",
        "Plus-que-parfait - tu",
        "Plus-que-parfait - il",
        "Plus-que-parfait - elle",
        "Plus-que-parfait - nous",
        "Plus-que-parfait - vous",
        "Plus-que-parfait - ils",
        "Plus-que-parfait - elles",
        "Subjonctif - je",
        "Subjonctif - tu",
        "Subjonctif - il",
        "Subjonctif - elle",
        "Subjonctif - nous",
        "Subjonctif - vous",
        "Subjonctif - ils",
        "Subjonctif - elles",
        "Conditionnel - je",
        "Conditionnel - tu",
        "Conditionnel - il",
        "Conditionnel - elle",
        "Conditionnel - nous",
        "Conditionnel - vous",
        "Conditionnel - ils",
        "Conditionnel - elles"
]

def get_row(file_str):
    start = 0
    end = len(file_str)
    row_dict = {}
    for i in range(0, len(fieldnames)):
        start = file_str.index("L\"", start, end) + 2
        end = file_str.index("\"", start, end)
        row_dict[fieldnames[i]] = file_str[start:end]
        start = end
        end = len(file_str)
    return row_dict

# Create parser object.
parser = argparse.ArgumentParser(
        prog="verbcpp2csv",
        description="Create a CSV file from a directory of .verb.cpp files",
)

# Add parser arguments.
parser.add_argument("directory",
                    help="Path to directory containin the .verb.cpp files"
)

parser.add_argument("-o", "--output",
                    help="Filepath to the desired output file [default: out.csv]",
                    default="out.csv"
)

# Parse the arguments.
args = parser.parse_args()

# Store paths.
path_dir = Path(args.directory)
path_out = Path(args.output)

# Exit if directory doesn't exist.
if not path_dir.is_dir():
    raise FileNotFoundError(str(path_csv) + " is not a directory or doesn't exist")

# Iterate through all files in the directory.
with open(path_out, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames)

    writer.writeheader()
    for verb in path_dir.iterdir():
        with open(verb, "r") as file:
            file_str = file.read()
            writer.writerow(get_row(file_str))
