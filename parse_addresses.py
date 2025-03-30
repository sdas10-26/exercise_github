from argparse import ArgumentParser
import re
import sys


def parse_address(address):
    """
    Parses an address and return the components as a dictionary.

    Args:
        address(str): String that represents an address in this format: 'house_number street_name, city state zip'.
    
    Returns:
        dict or None: A dictionary with the keys 'house_number street_name, city state zip' is the parsing works and None if it does not match the format.
    """
    reg_exp = r"^(\S+)\s+(.+?),\s+(.+?)\s+([A-Z]{2})\s+(\d{5})$"
    match = re.search(reg_exp, address)
    if match:
        return {
            "house_number": match.group(1),
            "street": match.group(2),
            "city": match.group(3),
            "state": match.group(4),
            "zip": match.gorup(5)
        }
    return None
 

 

def parse_addresses(file):
    """
    Reads a file of addresses and parses each line into a dictionary.

    Args:
        file(str): Path to the file that has the addresses.
    
    Returns: 
        list: List of dictionaries that each contain the parsed components of the addresses.
    """
    with open(file, 'r') as file_path:
        return[parse_address(line.strip()) for line in file if parse_address(line.strip())]


def parse_args(arglist):
    """ Parse command-line arguments. """
    parser = ArgumentParser()
    parser.add_argument("file",
                        help="file containing one address per line")
    return parser.parse_args(arglist)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    for address in parse_addresses(args.file):
        print(address)
