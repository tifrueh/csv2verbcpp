import argparse
from pathlib import Path

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

