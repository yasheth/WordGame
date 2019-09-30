import stringDatabase
import game


class Guess:
    """
             @author: Yash Sheth 40092777
             Created : May 13, 2019
             Modified : May 19, 2019
             This class is the main class which gives proper functionality to play the game. It displays option
             to the user and calls method according to user selection. Also uses Game and StringDatabase objects.
    """
    current_word = "----"
    uncovered_letters = []
    dictionary = []
    instances = []
    frequency = {'a':8.17,'b':1.49,'c':2.78,'d':4.25,'e':12.70,'f':2.23,'g':2.02,'h':6.09,'i':6.97,
                   'j':0.15,'k':0.77,'l':4.03,'m':2.41,'n':6.75,'o':7.51,'p':1.93,'q':0.10,'r':5.99,
                   's':6.33,'t':9.06,'u':2.76,'v':0.98,'w':2.36,'x':0.15,'y':1.97,'z':0.07}

    def print_message(self):
        """
            This method prints the current guess and options to the user.
        """
        # print("Word : " + game_instance.get_word())
        print("\nCurrent guess : "+self.current_word)
        print("\ng:guess, t:tell me, l:letter guess, q:quit")

    def guess_letter(self):
        """
            This method takes the letter input from the user and checks if the word has that letter or not.
            It changes the current guess word accordingly.
        """
        letter = input("# Enter a Letter :")
        if not letter:
            print("Please Enter a Valid Value")
        else:
            result = game_instance.check_letter(letter)

            if result == "NOT FOUND":
                print("WRONG. No corresponding letters found in the word. Try Again!")
            else:
                temp = list(self.current_word)
                count=0;
                for x in result:
                    count+=1
                    temp[x] = letter
                self.current_word = "".join(temp)
                print("Good Job. You Found "+str(count)+" Letters.")

    def get_value(self):
        """
            This method takes and returns user input on the console to the method caller.
            :return: String user input
        """
        return input("Enter your choice :")

    def create_new_game(self):
        """
            This method creates new game instance and gets new word for the game from the database.
        """
        global game_instance
        game_instance = game.Game()
        game_instance.set_word(db.get_random_word())
        print("\n---------NEW GAME---------")
        self.current_word = "----"

    def guess_word(self):
        """
            This method allows user to guess the word. If word is correct it calculates the score for the game
            and stores the game instance.
        """
        guess = input("# Guess the Word :")
        if not guess:
            print("Please enter a valid word.")
        else:
            if game_instance.check_word(guess):
                print("Correct! You did it Champ!")
                game_instance.calculate_score(self.frequency)
                self.instances.append(game_instance)
                obj.create_new_game()
            else:
                print("Wrong Guess. Try Again!")

    def final_result(self):
        """
            This method prints the final scorecard with score of all the games played before.
        """
        print(" Game \t\t Word \t\t Result \t\t Bad Guess \t\t Missed Letters \t\t Score ")
        print(" ---- \t\t ---- \t\t ------ \t\t --------- \t\t -------------- \t\t ----- ")
        count = 0
        final_score = 0
        for x in self.instances:
            count += 1
            print(" "+str(count)+"    \t\t "+str(x.get_word())+" \t\t "+str(x.get_result())+" \t\t "+str(x.get_wrong_guess())+" \t\t\t  "+str(x.get_wrong_letter())+" \t\t\t      "+str(round(x.get_score(),3)))
            final_score += x.get_score()

        print("\nFinal Score : "+str(round(final_score,3)))


print("***YASH'S GREAT GUESSING GAME***")
obj = Guess()
db = stringDatabase.StringDatabase()
game_instance = game.Game()
db.read_file()
game_instance.set_word(db.get_random_word())

while True:
    obj.print_message()
    option = obj.get_value()
    if option == "g":
        obj.guess_word()

    elif option == "t":
        game_instance.calculate_give_up_score(obj.frequency)
        obj.instances.append(game_instance)
        print("Don't Give Up Easy. The word is "+game_instance.get_word())
        obj.create_new_game()

    elif option == "l":
        obj.guess_letter()

    elif option == "q":
        obj.final_result()
        print("Thank You For Playing. Bye Bye.")
        break

    else:
        print("Choose properly!")
