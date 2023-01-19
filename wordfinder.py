"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    def __init__(self, file_path):
        """Reads the file and prints out the number of words found"""
        file = open(file_path)
        self.word = self.parse_file(file)
        print(f"{len(self.words)} words found")

    def parse_file(self, file):
        """ Parses the file into a list """
        return [word.strip() for word in file]

    def random_word(self):
        """Returns a random word"""
        return random.choice(self.words)


