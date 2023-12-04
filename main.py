import argparse
import csv
from pathlib import Path

# Function which returns the file contents for a specific verb
def get_out_str(verb):
    return f"""// Copyright (C) 2023 Timo Früh
// The full copyright notice can be found in ../main.cpp

#include "verb.db.hpp"

const verbDB::Verb verbDB::{verb["Identifier"]} = {{

    verbDB::VerbType::TYPE,

    L"infinitif",
    L"participePresent",

    L"presentJe",
    L"presentTu",
    L"presentIl",
    L"presentElle",
    L"presentNous",
    L"presentVous",
    L"presentIls",
    L"presentElles",

    L"imparfaitJe",
    L"imparfaitTu",
    L"imparfaitIl",
    L"imparfaitElle",
    L"imparfaitNous",
    L"imparfaitVous",
    L"imparfaitIls",
    L"imparfaitElles",

    L"futurJe",
    L"futurTu",
    L"futurIl",
    L"futurElle",
    L"futurNous",
    L"futurVous",
    L"futurIls",
    L"futurElles",

    L"passeComposeJe",
    L"passeComposeTu",
    L"passeComposeIl",
    L"passeComposeElle",
    L"passeComposeNous",
    L"passeComposeVous",
    L"passeComposeIls",
    L"passeComposeElles",

    L"plusQueParfaitJe",
    L"plusQueParfaitTu",
    L"plusQueParfaitIl",
    L"plusQueParfaitElle",
    L"plusQueParfaitNous",
    L"plusQueParfaitVous",
    L"plusQueParfaitIls",
    L"plusQueParfaitElles",

    L"subjonctifJe",
    L"subjonctifTu",
    L"subjonctifIl",
    L"subjonctifElle",
    L"subjonctifNous",
    L"subjonctifVous",
    L"subjonctifIls",
    L"subjonctifElles",

    L"conditionnelJe",
    L"conditionnelTu",
    L"conditionnelIl",
    L"conditionnelElle",
    L"conditionnelNous",
    L"conditionnelVous",
    L"conditionnelIls",
    L"conditionnelElles"
}};
"""

# Create a list to contain all verbs
verbs_list = []

# Create parser object
parser = argparse.ArgumentParser(
        prog="csv2verbcpp",
        description="Convert a csv to .verb.cpp files for Conjugateur",
)

# Add parser arguments
parser.add_argument("filepath", 
                    help="Path to the csv file"
)

parser.add_argument("-d", "--directory", 
                    help="Directory to put the .verb.cpp files in [default: .]"
)

# Parse the arguments
args = parser.parse_args()

# Store csv and output directory in corresponding variables
path_csv = Path(args.filepath)
path_out = Path(args.directory)

# Exit if csv does not exist
if not path_csv.is_file():
    raise FileNotFoundError(str(path_csv) + " is not a file or doesn't exist")

# Exit if output directory does not exist
if not path_out.is_dir():
    raise NotADirectoryError(str(path_out) + " is not a directory or doesn't exist")

# Open csvfile and extract verbs
with open(path_csv, newline="") as csvfile:
    verbreader = csv.DictReader(csvfile)
    for verb in verbreader:
        verbs_list.append(verb)

# Create and populate all verb files
for verb in verbs_list:
    out_str = ""
    with open(path_out / f"{verb['Identifier']}.verb.cpp", "x") as outfile:
        outfile.write(get_out_str(verb))
