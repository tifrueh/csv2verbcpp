import argparse
from pathlib import Path

parser = argparse.ArgumentParser(
        prog="csv2verbcpp",
        description="Convert a csv to .verb.cpp files for Conjugateur",
)

parser.add_argument("filepath", 
                    help="Path to the csv file"
)

parser.add_argument("-d", "--directory", 
                    help="Directory to put the .verb.cpp files in [default: .]"
)

args = parser.parse_args()
