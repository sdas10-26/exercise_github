""" Find cities near a specified location. """


from argparse import ArgumentParser
import sys

from haversine import haversine


class Cities:
    """
    Class that reads in geographic information about cities and finds the nearest cities to a specified latitude and longitude.
    """
    def __init__(self, filename):
        """
        Reads city data from the file.

        Args: 
            filename (str): Path to a file containing city data as specified
        
        Attributes:
            cities (dict): Dictionary that maps (area, city) tuples to (latitude, longitude) tuples.
        """
        self.cities = {}
        with open(filename, 'r', encoding = 'utf-8') as file:
            for line in file:
                data_files = line.strip().split(',')
                if len(data_files) >= 4:
                    area = data_files[0].strip()
                    city = data_files[1].strip()
                    latitude = float(data_files[2].strip())
                    longitude = float(data_files[3].strip())
                    self.cities[(area, city)] = (latitude, longitude)
    
    def nearest(self, point):
        """
        Finds the five closest cities to the specified point

        Args:
            point (tuple): Tuple that contains the floats of latitude and longitude.

        Returns:
            list: A sorted list that has the five closest cities to the specified point. 
        """
        return sorted(self.cities.keys(), key  = lambda city: haversine(point, self.cities[city]))[:5]
                    


def main(filename, arg1, arg2):
    """ Read city data from a file and find the closest cities to a
    specified location (either an area and city from filename or a
    latitude and longitude which may or may not be in the file).
    
    Args:
        filename (str): path to a file containing city data. Each line
            in the file should consist of four values, separated by
            commas: area (e.g., state or country), city, latitude in
            decimal degrees, longitude in decimal degrees.
        arg1 (str): either the name of an area in the file, or a string
            representation of a latitude.
        arg2 (str): either the name of a city in the file, or a string
            representation of a longitude.
    
    Side effects:
        Writes to stdout.
    """
    cities = Cities(filename)
    try:
        lat = float(arg1)
        lon = float(arg2)
        point = (lat, lon)
    except ValueError:
        try:
            point = cities.cities[arg1, arg2]
        except KeyError:
            sys.exit(f"Error: could not look up {arg1}, {arg2}")
    print(f"For {arg1}, {arg2}, the nearest cities from the file are")
    for result in cities.nearest(point):
        print("    " + ", ".join(result))


def parse_args(arglist):
    """ Process command-line arguments and return the parsed values as a
    namespace. """
    parser = ArgumentParser()
    parser.add_argument("filename", help="file containing city data")
    parser.add_argument("arg1",
                        help="a latitude expressed in decimal degrees"
                             " or an area (state, country) from the"
                             " file")
    parser.add_argument("arg2",
                        help="a longitude expressed in decimal degrees"
                             " or a city name from the file")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filename, args.arg1, args.arg2)
