import random

class HangmanGame:
    def __init__(self):
        self.stages = ['''
          +---+
          |   |
          O   |
         /|\\  |
         / \\  |
              |
        =========
        ''', '''
          +---+
          |   |
          O   |
         /|\\  |
         /    |
              |
        =========
        ''', '''
          +---+
          |   |
          O   |
         /|\\  |
              |
              |
        =========
        ''', '''
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========
        ''', '''
          +---+
          |   |
          O   |
           |   |
              |
              |
        =========
        ''', '''
          +---+
          |   |
          O   |
              |
              |
              |
        =========
        ''', '''
          +---+
          |   |
              |
              |
              |
              |
        =========
        ''']
        self.lives = 6
        self.word_list = ["aardvark", "baboon", "camel"]
        self.chosen_word = random.choice(self.word_list)
        self.size = len(self.chosen_word)
        self.display = ["_"] * self.size
        self.rough = ""

    def display_current_state(self):
        print(" ".join(self.display))
        print(f"Lives remaining: {self.lives}")

    def get_guess(self):
        return input("Guess a letter present in the word\n").lower()

    def update_display(self, guess):
        for i, letter in enumerate(self.chosen_word):
            if letter == guess:
                self.display[i] = guess
        self.rough = "".join(self.display)

    def process_guess(self, guess):
        if guess in self.chosen_word:
            print(f"You guessed {guess} correctly.")
            self.update_display(guess)
        else:
            print("Your guess was wrong.")
            self.lives -= 1

    def print_stage(self):
        print(self.stages[self.lives])

    def play(self):
        print(" ".join(self.display))

        while self.rough != self.chosen_word:
            guess = self.get_guess()
            self.process_guess(guess)
            self.display_current_state()
            self.print_stage()

            if self.lives == 0:
                print("Pierson dies ,You lost the game.")
                break

            if "_" not in self.display:
                print("Congratulations, you saved Pearson ")
                break

