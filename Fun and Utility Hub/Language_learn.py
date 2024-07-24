from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

class FlashcardApp:
    def __init__(self, root):
        self.window = root
        self.window.title("Flashy")
        self.window.configure(padx=80, pady=80, bg=BACKGROUND_COLOR)

        self.flip_timer = self.window.after(1000000, func=self.flip_card)
        self.front_card = Canvas(width=800, height=562, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.front_image = PhotoImage(file="images/card_front.png")
        self.back_image = PhotoImage(file="images/card_back.png")
        self.card_background = self.front_card.create_image(400, 263, image=self.front_image)
        self.card_title = self.front_card.create_text(400, 150, text="Title", font=("Arial", 24, "italic"))
        self.card_text = self.front_card.create_text(400, 263, text="WORD", font=("Arial", 33, "bold"))
        self.front_card.grid(column=0, row=0)

        self.tick_image = PhotoImage(file="images/right.png")
        self.tick_button = Button(image=self.tick_image, highlightthickness=0, command=self.is_known)
        self.tick_button.place(x=100, y=530)

        self.cross_image = PhotoImage(file="images/wrong.png")
        self.cross_button = Button(image=self.cross_image, highlightthickness=0, command=self.next_card)
        self.cross_button.place(x=600, y=530)

        self.load_data()
        self.next_card()

    def load_data(self):
        try:
            self.data = pandas.read_csv("data/to_learn_words.csv")
        except FileNotFoundError:
            original_data = pandas.read_csv("data/french_words.csv")
            self.words = original_data.to_dict(orient="records")
        else:
            self.words = self.data.to_dict(orient="records")

    def next_card(self):
        self.window.after_cancel(self.flip_timer)
        self.current_card = random.choice(self.words)
        self.front_card.itemconfig(self.card_title, text="French", fill="black")
        self.front_card.itemconfig(self.card_text, text=f"{self.current_card['French']}", fill="black")
        self.front_card.itemconfig(self.card_background, image=self.front_image)
        self.flip_timer = self.window.after(3000, func=self.flip_card)

    def flip_card(self):
        self.front_card.itemconfig(self.card_title, text="English", fill="white")
        self.front_card.itemconfig(self.card_text, text=f"{self.current_card['English']}", fill="white")
        self.front_card.itemconfig(self.card_background, image=self.back_image)
        self.window.after_cancel(self.flip_timer)

    def is_known(self):
        self.words.remove(self.current_card)
        not_known = pandas.DataFrame(self.words)
        not_known.to_csv("data/to_learn_words.csv", index=False)
        self.next_card()
