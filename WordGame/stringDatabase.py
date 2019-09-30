import random


class StringDatabase(object):
    """
         @author: Yash Sheth 40092777
         Created : May 13, 2019
         Modified : May 14, 2019
         This class does IO Operation of reading text file for four lettered words and stores them in a
         list. It also generates random words using python's random module for the game.
    """

    dictionary = []
    used_words = []

    def read_file(self):
        """
        read_file() method reads the content from the four_letters.txt file and stores the words
        in a list named dictionary.
        """
        f = open("four_letters.txt", "r")
        if f.mode == 'r':
            content = f.read()
            self.dictionary = content.split()

    def get_dictionary(self):
        """
        get_dictionary() method returns the dictionary list.
        :return: list dictionary
        """
        return self.dictionary

    def get_random_word(self):
        """
        get_random_word() method returns a random word from the dictionary.
        :return: String a random word from the dictionary and removes it from the dictionary so it doesnt appear again.
        """
        word = random.choice(self.dictionary)
        self.used_words.append(word)
        self.dictionary.remove(word)
        return word
