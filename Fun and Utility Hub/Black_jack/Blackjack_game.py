import random

class BlackjackGame:
    def __init__(self):
        self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.user_cards = []
        self.computer_cards = []
        self.logo = """
        .------.            _     _            _    _            _    
        |A_  _ |.          | |   | |          | |  (_)          | |   
        |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
        | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
        |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
        `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
              |  \/ K|                            _/ |                
              `------'                           |__/           
        """

    def start_game(self):
        choice = input("Do you want to play a game of Blackjack? 'y' or 'n': ")
        if choice == 'y':
            print(self.logo)
            self.user_cards.append(random.choice(self.cards))
            self.user_cards.append(random.choice(self.cards))
            print("Your cards: " + str(self.user_cards))
            print("Your current score: " + str(sum(self.user_cards)))
            self.computer_cards.append(random.choice(self.cards))
            print("Computer's first card: " + str(self.computer_cards[0]))
            self.user_turn()
            self.computer_turn()
            self.compare()

    def user_turn(self):
        while True:
            choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if choice == 'y':
                self.user_cards.append(random.choice(self.cards))
                print("Your cards: " + str(self.user_cards))
                print("Your current score: " + str(sum(self.user_cards)))
                if sum(self.user_cards) > 21:
                    print("Your final hand: " + str(self.user_cards))
                    print("Your final score: " + str(sum(self.user_cards)))
                    print("You went over. You lost the game.")
                    return
            else:
                break

    def computer_turn(self):
        while sum(self.computer_cards) < 17:
            self.computer_cards.append(random.choice(self.cards))
            if sum(self.computer_cards) > 21:
                self.computer_cards.pop()
        print("The cards selected by computer are: " + str(self.computer_cards))
        print("The score of the computer is: " + str(sum(self.computer_cards)))

    def compare(self):
        user_score = sum(self.user_cards)
        computer_score = sum(self.computer_cards)
        if user_score > 21:
            print("You went over. You lost the game.")
        elif computer_score > 21 or user_score > computer_score:
            print("The user has won the game.")
        elif user_score < computer_score:
            print("The computer has won the game.")
        else:
            print("It's a draw.")
