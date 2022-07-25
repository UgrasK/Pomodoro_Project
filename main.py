from tkinter import *
import math

# ----------------------- CONSTANTS --------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ----------------------- TIMER RESET --------------------- #

# ----------------------- TIMER MECHANISM --------------------- #
# create a timer function to use when start button is clicked
def start_timer():
    global reps
    reps += 1

    work_seconds = WORK_MIN * 60
    short_break_seconds = SHORT_BREAK_MIN * 60
    long_break_seconds = LONG_BREAK_MIN * 60

    # long break countdown if 8th/16th/24th/32th... reps
    if reps % 8 == 0:
        count_down(long_break_seconds)
        title_label.config(text="BREAK", fg=RED)
    # short break countdown if 2nd/4th/6th/10th/... reps
    elif reps % 2 == 0:
        count_down(short_break_seconds)
        title_label.config(text="BREAK", fg=PINK)
    # work countdown if 1st/3rd/5th/7th... reps
    else:
        count_down(work_seconds)
        title_label.config(text="WORK", fg=GREEN)

# ----------------------- COUNTDOWN MECHANISM --------------------- #
# create a countdown function to change timer_text
def count_down(count):
    count_minute = math.floor(count / 60)
    count_seconds = count % 60
    if count_minute < 10:
        count_minute = f"0{count_minute}"
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    # start countdown with rep 1
    if count > 0:
        window.after(1000, count_down, count - 1)
    # start countdown with rep +1 when countdown reaches 00:00
    else:
        start_timer()


# ----------------------- UI SETUP --------------------- #
# create a window with Tkinter
window = Tk()
# create a title for window
window.title("Pomodoro")
# set padding for window on x,y and set a background color
window.config(padx=100, pady=50, bg=YELLOW)


# create a label as Timer and set its position on grid
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

# create canvas, set a background color and remove white border with highlightthickness
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# create a Photoimage with file path and save it in a variable
tomato_img = PhotoImage(file="tomato.png")
# use that in create_image method on canvas with pos x,y
canvas.create_image(100, 112, image=tomato_img)
# create text with pos x,y , text, fill color, font and save it in a variable
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# set canvas position on grid
canvas.grid(column=1, row=1)

# create a start button, set its position on grid and use start_timer() function on its command
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
# create a reset button and set its position on grid
reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

# create checkmark and set its position on grid
check_marks = Label(text="✔", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
