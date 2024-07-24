from tkinter import *
from Black_jack.Blackjack_game import BlackjackGame
from Ping_pong_game.Pingpong import PingPongGame
from Turtle_Crossing.turtle_race import TurtleRace
from Snake_Game.snake_game import SnakeGame
from Quiz_game.Quiz_main import QuizGame
from Hangman.Hangman_game import HangmanGame
from Language_learn import FlashcardApp
from Focus_Hours.main import PomodoroTimer
from Password_Manager.main import PasswordManager


def main():

    print("................Welcome to Gamers Hub, Play various games here and Enjoy your time ....................")

    while True:
        try:
            game = int(input(
                "1) BlackJack Game \n2) PingPong Game \n3) Turtle Crossing Game \n4) HungrySnake Game \n5) Hangman Game \n6) Quizzler Quest \n7) FluentFlock \n8) Focus hours\n9) PassWordManager \n10) Document Manager \nPlease choose which game you wish to play (1-10): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 8.")
            continue

        if game == 1:
            game_selected = BlackjackGame()
            game_selected.start_game()
            print("\n")

        elif game == 2:
            game_selected = PingPongGame()
            game_selected.play()
            print("\n")

        elif game == 3:
            game_selected = TurtleRace()
            game_selected.run()
            print("\n")

        elif game == 4:
            game_selected = SnakeGame()
            game_selected.run_game()
            print("\n")

        elif game == 5:
            game_selected = HangmanGame()
            game_selected.play()
            print("\n")

        elif game == 6:
            game_selected = QuizGame()
            game_selected.start()
            print("\n")

        elif game == 7:
            root = Tk()
            app = FlashcardApp(root)
            root.mainloop()
            print("\n")

        elif game == 8:
            root = Tk()
            app = PomodoroTimer(root)
            root.mainloop()
            print("\n")

        elif game == 9:
            PasswordManager()
            print("\n")

        elif game == 10:

            if len(sys.argv) > 1:
                cli_main()
            else:

                print("To run the following functions in command line use this commands")
                print(" Command to count total number of words in text file : -w\n",
                      "Command to count total number of characters in text file : -c \n",
                      "Command to count total number of lines in text file : -l \n",
                      "Command to sort the lines in alphabetical order in text file : -s \n",
                      "Command to remove duplicate words from the text file : -d \n",
                      "Command to replace the words in text file : -r \n",
                      "Command to compress the text file to zip file : -z \n",
                      "Command to decompress the zip file : -x \n",
                      "Command to create a PDF file from Word or .docx file : -p \n\n",)
                interactive_main()

        else:
            print("Please Select a valid input from above ")


if __name__ == "__main__":
    main()
