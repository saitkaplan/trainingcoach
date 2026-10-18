from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
STEP = 0
TIMER = None

# ---------------------------- TIMER RESET ----------------------------------- #

def reset_timer():
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    global STEP
    STEP = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global STEP
    STEP += 1

    work_sec = WORK_MIN * 60
    short_brk_sec = SHORT_BREAK_MIN * 60
    long_brk_sec = LONG_BREAK_MIN * 60

    if STEP % 8 == 0:
        count_down(long_brk_sec)
        title_label.config(text="Rest", fg=PINK)
    elif STEP % 2 == 0:
        count_down(short_brk_sec)
        title_label.config(text="Rest", fg=RED)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM --------------------------- #

def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(STEP/2)
        for i in range(work_sessions):
            mark += "✓"
        check_label.config(text=mark)

# ---------------------------- UI SETUP -------------------------------------- #

window = Tk()
window.title("Training Coach")
window.config(padx=50, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")

title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "bold"), bg=YELLOW)
title_label.pack(side="top")

canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 26, "bold"))
canvas.pack()

space_label = Label(text=" ", fg=GREEN, font=(FONT_NAME, 25, "bold"), bg=YELLOW)
space_label.pack(side="top")

start_button = Button(text="Start", fg="Black", bg=YELLOW, command=start_timer)
start_button.pack(side="left")

reset_button = Button(text="Reset", fg="Black", bg=YELLOW, command=reset_timer)
reset_button.pack(side="right")

check_label = Label(fg=RED, bg=YELLOW)
check_label.pack(side="bottom")

window.mainloop()