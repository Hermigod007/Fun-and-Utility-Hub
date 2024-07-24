from tkinter import *
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

class PomodoroTimer:
    def __init__(self, root):
        self.window = root
        self.window.title("Pomodoro")
        self.window.config(padx=100, pady=100, bg=YELLOW)

        self.repeats = 0
        self.timer = None

        # UI Setup
        self.canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
        self.tomato_photo = PhotoImage(file="tomato.png")
        self.canvas.create_image(100, 112, image=self.tomato_photo)
        self.counter = self.canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 32, "bold"))
        self.canvas.grid(column=2, row=2)

        self.label1 = Label(text="Timer")
        self.label1.config(font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
        self.label1.grid(column=2, row=1)

        self.button1 = Button(text="Start", command=self.start_timer)
        self.button1.config(font=(FONT_NAME, 15, "bold"), bg="white", highlightthickness=0)
        self.button1.grid(column=1, row=3)

        self.button2 = Button(text="Reset", command=self.reset_timer)
        self.button2.config(font=(FONT_NAME, 15, "bold"), bg="white", highlightthickness=0)
        self.button2.grid(column=3, row=3)

        self.checkmark = Label()
        self.checkmark.config(font=(FONT_NAME, 20), bg=YELLOW, fg=GREEN)
        self.checkmark.grid(column=2, row=4)

    def reset_timer(self):
        self.window.after_cancel(self.timer)
        self.canvas.itemconfig(self.counter, text="00:00")
        self.label1.config(text="Timer")
        self.checkmark.config(text="")
        self.repeats = 0

    def start_timer(self):
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60
        self.repeats += 1

        if self.repeats == 1 or self.repeats == 3 or self.repeats == 5 or self.repeats == 7:
            self.label1.config(text="Work", fg=RED)
            self.count_down(work_sec)
        elif self.repeats == 8:
            self.label1.config(text="Long Break", fg=GREEN)
            self.count_down(long_break_sec)
        else:
            if self.repeats == 2:
                check = "✔"
                self.checkmark.config(text=check)
            elif self.repeats == 4:
                check = "✔✔"
                self.checkmark.config(text=check)
            else:
                check = "✔✔✔"
                self.checkmark.config(text=check)

            self.label1.config(text="Short Break", fg=PINK)
            self.count_down(short_break_sec)

    def count_down(self, count):
        minutes = math.floor(count / 60)
        seconds = count % 60
        if seconds == 0:
            seconds = "0"
        if int(seconds) < 10:
            seconds = f"0" + str(seconds)
        if count >= 0:
            self.timer = self.window.after(1000, self.count_down, count - 1)
            self.canvas.itemconfig(self.counter, text=f"{minutes}:{seconds}")
        else:
            self.start_timer()

