from tkinter import *

# ----------------------- CONSTANTS --------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ----------------------- TIMER RESET --------------------- #

# ----------------------- TIMER MECHANISM --------------------- #

# ----------------------- COUNTDOWN MECHANISM --------------------- #


# ----------------------- UI SETUP --------------------- #
# create a window with Tkinter
window = Tk()
# create a title for window
window.title("Pomodoro")
# set padding for window on x,y and set a background color
window.config(padx=100, pady=50, bg=YELLOW)

# create canvas, set a background color and remove white border with highlightthickness
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# create a Photoimage with file path and save it to a variable
tomato_img = PhotoImage(file="tomato.png")
# use that in create_image method on canvas with pos x,y
canvas.create_image(100, 112, image=tomato_img)
# create text with pos x,y , text, fill color and font
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

# show canvas in window
canvas.pack()

window.mainloop()
