import re


class Game(object):
    """
        @author: Yash Sheth 40092777
        Created : May 13, 2019
        Modified : May 19, 2019
        This class holds all the information about the game. Score, word, Wrong guess, Missed Letter and other
        important details.
    """
    selected_word = ""
    wrong_guess = 0
    wrong_letter = 0
    result = ""
    score = 0
    letters = []
    letter_request = 0

    def set_result(self, result):
        """
            Sets result value.
            :param result: sets result
            :return:
        """
        self.result = result

    def get_result(self):
        """
            Returns result value
            :return: result value.
        """
        return self.result

    def set_word(self, word):
        """
            Sets word value
            :param word: word of the game
            :return:
        """
        self.selected_word = word
        self.letters = list(word)

    def get_word(self):
        """
            Returns the word of the game.
            :return: word
        """
        return self.selected_word

    def check_word(self, word):
        """
            Check if the word is correct or not
            :param word: the word from the user
            :return: True or False according to the result
        """
        if self.selected_word == word:
            self.result = "SUCCESS"
            return True
        else:
            self.wrong_guess = self.wrong_guess+1
            return False

    def check_letter(self, letter):
        """
            Check if the letter exists in the word or not.
            :param letter: the letter from the user.
            :return:
        """
        self.letter_request += 1
        if self.selected_word.find(letter) == -1:
            self.wrong_letter += 1
            return "NOT FOUND"
        else:
            i = 0
            length = len(self.letters)
            while i < length:
                if self.letters[i] == letter:
                    self.letters.remove(self.letters[i])
                    length = length - 1
                    continue
                i = i + 1
            occurrence = [m.start() for m in re.finditer(letter, self.selected_word)]
            return occurrence

    def get_wrong_guess(self):
        """
            Returns the wrong guess count.
            :return: count of wrong guess.
        """
        return self.wrong_guess

    def get_wrong_letter(self):
        """
            Returns the missed letter count
            :return: count of missed letters
        """
        return self.wrong_letter

    def get_score(self):
        """
            Return the score of the game
            :return: score of game
        """
        return self.score

    def calculate_score(self, frequency):
        """
            Calculates score
            :param frequency: key value dictionary for calculating score
        """
        for x in self.letters:
            self.score = self.score + frequency.get(x)
        if self.letter_request > 0:
            self.score = self.score / self.letter_request
        if self.wrong_guess > 0:
            self.score = self.score * (self.wrong_guess * 0.10)

    def calculate_give_up_score(self, frequency):
        """
            Calculates score if user gives up.
            :param frequency: key value dictionary for calculating score
        """
        self.result = "GAVE UP"
        for x in self.letters:
            self.score = self.score-frequency.get(x)

    def set_score(self, score):
        """
            Sets score of the game
            :param score: value of score
        """
        self.score = score
