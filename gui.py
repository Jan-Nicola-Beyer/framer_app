
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import *


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

print(ASSETS_PATH)



def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1280x720")
window.configure(bg = "#FFFFFF")






def Close():
    window.destroy()






canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    640.0,
    720.0,
    fill="#5B83D2",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    955.5,
    277.5,
    image=entry_image_1
)
entry_1 = Text(
    fg="white",
    bd=0,
    bg="#5B83D2",
    highlightthickness=0
)
Font_tuple = ("Comic Sans MS", 20, "bold")
entry_1.configure(font = Font_tuple)




entry_1.place(
    x=676.0,
    y=132.0,
    width=559.0,
    height=289.0
)

def show_text():
    entry_1.insert(INSERT, "Hello.....")
    entry_1.insert(END, "Bye Bye.....")
    entry_1.place(
        x=676.0,
        y=132.0,
        width=559.0,
        height=289.0
    )



button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=show_text,
    relief="flat"
)
button_1.place(
    x=76.0,
    y=483.0,
    width=455.0,
    height=103.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=76.0,
    y=388.0,
    width=454.0,
    height=91.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=78.0,
    y=284.0,
    width=437.0,
    height=98.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=83.0,
    y=184.0,
    width=447.0,
    height=96.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=83.0,
    y=72.0,
    width=448.0,
    height=111.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=1065.0,
    y=434.0,
    width=185.0,
    height=86.0
)

button_image_exit = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_exit = Button(
    image=button_image_exit,
    borderwidth=0,
    highlightthickness=0,
    command=Close,
    relief="flat"
)
button_exit.place(
    x=863.0,
    y=434.0,
    width=185.0,
    height=86.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=660.0,
    y=434.0,
    width=185.0,
    height=86.0
)
window.resizable(False, False)
window.mainloop()