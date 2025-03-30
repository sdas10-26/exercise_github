import re

def get_words(s):
    """ Extract a list of words from string s.

    Args:
        s (str): a string containing one or more words.

    Returns:
        list of str: a list of words from s converted to lower-case.
    """
    words = list()
    s = re.sub(r"--+", " ", s)
    for word in re.findall(r"[\w'-]+", s):
        word = word.strip("'-_")
        if len(word) > 0:
            words.append(word.lower())
    return words

class UniqueWords:
    """
    This is a class to track/manage unique words within files.

    Attributes:
        all_words (set): Set that keeps track of every word you encounter in the files you read in.
        unique_words (set): Set that contains words that show up in a single file.
        words_by_file (dict): Dictionary that keeps track of the words that occur in a single file.
    """
    def __init__(self):
        """
        Initializes attributes to track unique words.
        """
        self.all_words.set()
        self.unique_words.set()
        self.words_by_file = {}

    def add_file(self, filename, key):
        """
        Reads the file and processes words along with updating the tracking attributes.

        Args:
            filename (str): Path for the file to be read.
            key (str): Nickname for the file.
        """
        with open(filename, 'r', encoding = 'uft-8') as file:
            file_content = file.read()
        words_by_file = set(get_words(file_content))
        self.words_by_file[key] = words_by_file
        self.words_by_file -= words_by_file
        new_words = words_by_file - self.all_words
        self.unique_words.update(new_words)
        self.all_words.update(new_words)

    def unique(self, key):
        """
        Returns the unique set of words from the specified file.

        Args:
            key (str): Nickname for the file that is being used to get the unique words.
        
        Returns:
            set: Set of words that is unique to the file specified.
        """
        if key in self.words_by_file:
            return self.words_by_file[key] - (self.all_words - self.words_by_file[key])
        return set()
