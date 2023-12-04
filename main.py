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

# Store csv and output directory in corresponding variables
path_csv = Path(args.filepath)
path_out = Path(args.directory)

# Exit if csv does not exist
if not path_csv.is_file():
    raise FileNotFoundError(str(path_csv) + " is not a file or doesn't exist")

# Exit if output directory does not exist
if not path_out.is_dir():
    raise NotADirectoryError(str(path_out) + " is not a directory or doesn't exist")

