import argparse
import csv
from pathlib import Path

# Function which returns the file contents for a specific verb
def get_out_str(verb):
    return f"""// Copyright (C) 2023-2024 Timo Früh
// The full copyright notice can be found in ../main.cpp

#include "verb.db.hpp"

const verbDB::Verb verbDB::{verb["Identifier"]} = {{

    L"{verb["Label"]}",

    verbDB::VerbType::{verb["Type"]},

    L"{verb["Infinitif"]}",
    L"{verb["Translation"]}",
    L"{verb["Participe présent"]}",

    L"{verb["Présent - je"]}",
    L"{verb["Présent - tu"]}",
    L"{verb["Présent - il"]}",
    L"{verb["Présent - elle"]}",
    L"{verb["Présent - nous"]}",
    L"{verb["Présent - vous"]}",
    L"{verb["Présent - ils"]}",
    L"{verb["Présent - elles"]}",

    L"{verb["Imparfait - je"]}",
    L"{verb["Imparfait - tu"]}",
    L"{verb["Imparfait - il"]}",
    L"{verb["Imparfait - elle"]}",
    L"{verb["Imparfait - nous"]}",
    L"{verb["Imparfait - vous"]}",
    L"{verb["Imparfait - ils"]}",
    L"{verb["Imparfait - elles"]}",

    L"{verb["Futur - je"]}",
    L"{verb["Futur - tu"]}",
    L"{verb["Futur - il"]}",
    L"{verb["Futur - elle"]}",
    L"{verb["Futur - nous"]}",
    L"{verb["Futur - vous"]}",
    L"{verb["Futur - ils"]}",
    L"{verb["Futur - elles"]}",

    L"{verb["Passé composé - je"]}",
    L"{verb["Passé composé - tu"]}",
    L"{verb["Passé composé - il"]}",
    L"{verb["Passé composé - elle"]}",
    L"{verb["Passé composé - nous"]}",
    L"{verb["Passé composé - vous"]}",
    L"{verb["Passé composé - ils"]}",
    L"{verb["Passé composé - elles"]}",

    L"{verb["Plus-que-parfait - je"]}",
    L"{verb["Plus-que-parfait - tu"]}",
    L"{verb["Plus-que-parfait - il"]}",
    L"{verb["Plus-que-parfait - elle"]}",
    L"{verb["Plus-que-parfait - nous"]}",
    L"{verb["Plus-que-parfait - vous"]}",
    L"{verb["Plus-que-parfait - ils"]}",
    L"{verb["Plus-que-parfait - elles"]}",

    L"{verb["Subjonctif - je"]}",
    L"{verb["Subjonctif - tu"]}",
    L"{verb["Subjonctif - il"]}",
    L"{verb["Subjonctif - elle"]}",
    L"{verb["Subjonctif - nous"]}",
    L"{verb["Subjonctif - vous"]}",
    L"{verb["Subjonctif - ils"]}",
    L"{verb["Subjonctif - elles"]}",

    L"{verb["Conditionnel - je"]}",
    L"{verb["Conditionnel - tu"]}",
    L"{verb["Conditionnel - il"]}",
    L"{verb["Conditionnel - elle"]}",
    L"{verb["Conditionnel - nous"]}",
    L"{verb["Conditionnel - vous"]}",
    L"{verb["Conditionnel - ils"]}",
    L"{verb["Conditionnel - elles"]}"

}};
"""

# Create a list to contain all verbs
verbs_list = []

# Create parser object
parser = argparse.ArgumentParser(
        prog="csv2verbcpp",
        description="Create .verb.cpp files from a CSV file",
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
