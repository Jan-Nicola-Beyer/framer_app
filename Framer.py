#### new line #####
from pathlib import Path
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import *
import tkinter as tk
import pandas as pd

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path("./assets")

        self.geometry("1280x720")
        self.resizable(0,0)
        self.title('Framing Intelligence Center')
        self.configure(bg="#FFFFFF")
        self.img = PhotoImage(file='favicon.png')

        self.tk.call('wm', 'iconphoto', self._w, self.img)

        ##### data
        self.data = pd.read_excel("testx.xlsx")
        # self.data["code"]=np.nan
        print(self.data.head(3))
        # Text field

        # inital number
        self.initial = tk.IntVar()
        if self.data.code.last_valid_index() == None:
            self.initial.set(0)
        else:
            point = self.data.code.last_valid_index()
            self.initial.set(point+1)



        self.canvas = Canvas(
            self,
            bg="#FFFFFF",
            height=720,
            width=1280,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.canvas.create_rectangle(
            0.0,
            0.0,
            640.0,
            720.0,
            fill="#5B83D2",
            outline="")

       # self.canvas.create_text(950,80,fill="darkblue",font="Calibri 20  bold",
                        #text=str(f"{self.initial.get() + 1} of {len(self.data)} "))

        ##### label for how far you are
        self.label_entry = Label(self, text=str(f"{self.initial.get() + 1} of {len(self.data)} "), anchor=W, bg="#FFFFFF")
        self.button1_window = self.canvas.create_window(1200, 10, anchor=NW, window=self.label_entry)


        if str(self.data.code.values[self.initial.get()]) == "nan":
            self.label_frame = Label(self, text="Not picked",
                                     anchor=W, bg="#FFFFFF")
            self.label_frame_window = self.canvas.create_window(1200, 40, anchor=NW, window=self.label_frame)
        else:
            self.label_frame = Label(self, text=f"Frame {str(int(self.data.code.values[self.initial.get()]))}",
                                     anchor=W, bg="#FFFFFF")
            self.label_frame_window = self.canvas.create_window(1200, 40, anchor=NW, window=self.label_frame)


        self.entry_image_1 = PhotoImage(
            file="assets/entry_1.png")
        self.entry_bg_1 = self.canvas.create_image(
            955.5,
            277.5,
            image=self.entry_image_1
        )
        self.entry_1 = Text(
            fg="white",
            bd=0,
            bg="#5B83D2",
            highlightthickness=0
        )
        self.Font_tuple = ("Calibri", 16)
        self.entry_1.configure(font=self.Font_tuple)

    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)








class Functionality(App):
    def __init__(self):
        App.__init__(self)
        #### backward button
        self.button_image_backward = PhotoImage(
            file="assets/button_8.png")
        self.button_backward = Button(
            image=self.button_image_backward,
            borderwidth=0,
            highlightthickness=0,
            command=self.backward,
            relief="flat"
        )
        self.button_backward.place(
            x=660.0,
            y=434.0,
            width=185.0,
            height=86.0
        )

        self.button_image_exit = PhotoImage(
            file="assets/button_7.png")
        self.button_exit = Button(
            image=self.button_image_exit,
            borderwidth=0,
            highlightthickness=0,
            command=self.Close,
            relief="flat"
        )
        self.button_exit.place(
            x=863.0,
            y=434.0,
            width=185.0,
            height=86.0
        )


        #### forward button
        self.button_image_forward = PhotoImage(
            file="assets/button_6.png")
        self.button_forward = Button(
            image=self.button_image_forward,
            borderwidth=0,
            highlightthickness=0,
            command=self.forward,
            relief="flat"
        )
        self.button_forward.place(
            x=1065.0,
            y=434.0,
            width=185.0,
            height=86.0
        )


        #### Button Frame 1
        self.button_image_Frame1 = PhotoImage(
            file="assets/button_5.png")
        self.button_frame1 = Button(
            image=self.button_image_Frame1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.frame_pick(1),
            relief="flat"
        )
        self.button_frame1.place(
            x=83.0,
            y=72.0,
            width=448.0,
            height=111.0
        )
        #### Button Frame 2
        self.button_image_Frame2 = PhotoImage(
            file="assets/button_4.png")
        self.button_frame2 = Button(
            image=self.button_image_Frame2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.frame_pick(2),
            relief="flat"
        )
        self.button_frame2.place(
            x=83.0,
            y=184.0,
            width=447.0,
            height=96.0
        )



        ####button frame 3

        self.button_image_frame3 = PhotoImage(
            file="assets/button_3.png")
        self.button_frame3 = Button(
            image=self.button_image_frame3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.frame_pick(3),
            relief="flat"
        )
        self.button_frame3.place(
            x=78.0,
            y=284.0,
            width=437.0,
            height=98.0
        )




    #### button frame 4
        self.button_image_frame4 = PhotoImage(
            file="assets/button_2.png")
        self.button_frame4 = Button(
            image=self.button_image_frame4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.frame_pick(4),
            relief="flat"
        )
        self.button_frame4.place(
            x=76.0,
            y=388.0,
            width=454.0,
            height=91.0
        )







        #### button frame 5

        self.button_image_Frame5 = PhotoImage(
            file="assets/button_1.png")
        self.button_frame_5 = Button(
            image=self.button_image_Frame5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.frame_pick(5),
            relief="flat"
        )
        self.button_frame_5.place(
            x=76.0,
            y=483.0,
            width=455.0,
            height=103.0
        )

        self.text=self.data.summary.values[self.initial.get()]
        self.entry_1.insert(INSERT, self.text)
        #self.entry_1.insert(END, "Bye Bye.....")
        self.entry_1.place(
            x=676.0,
            y=132.0,
            width=559.0,
            height=289.0
            )

    def forward(self):

        self.initial.set(self.initial.get()+1)
        self.entry_1.delete("1.0", "end")
        self.text = self.data.summary.values[self.initial.get()]
        self.entry_1.insert(INSERT, self.text)
        # self.entry_1.insert(END, "Bye Bye.....")
        self.entry_1.place(
            x=676.0,
            y=132.0,
            width=559.0,
            height=289.0
        )
        self.label_entry = Label(self, text=str(f"{self.initial.get() + 1} of {len(self.data)} "), anchor=W, bg="#FFFFFF")
        self.button1_window = self.canvas.create_window(1200, 10, anchor=NW, window=self.label_entry)

        if str(self.data.code.values[self.initial.get()]) == "nan":
            self.label_frame = Label(self, text="Not picked",
                                     anchor=W, bg="#FFFFFF")
            self.label_frame_window = self.canvas.create_window(1200, 40, anchor=NW, window=self.label_frame)
        else:
            self.label_frame = Label(self, text=f"Frame {str(int(self.data.code.values[self.initial.get()]))}",
                                     anchor=W,bg="#FFFFFF")
            self.label_frame_window = self.canvas.create_window(1200, 40, anchor=NW, window=self.label_frame)



    def backward(self):
        if self.initial.get() >= 1:
            self.initial.set(self.initial.get()-1)
            self.entry_1.delete("1.0", "end")
            self.text = self.data.summary.values[self.initial.get()]
            self.entry_1.insert(INSERT, self.text)
            # self.entry_1.insert(END, "Bye Bye.....")
            self.entry_1.place(
                x=676.0,
                y=132.0,
                width=559.0,
                height=289.0
            )
            self.label_entry = Label(self, text=str(f"{self.initial.get() + 1} of {len(self.data)} "), anchor=W, bg="#FFFFFF")
            self.button1_window = self.canvas.create_window(1200, 10, anchor=NW, window=self.label_entry)


            if str(self.data.code.values[self.initial.get()]) == "nan":
                self.label_frame.destroy()
                self.label_frame = Label(self, text="Not picked",
                                         anchor=W, bg="#FFFFFF")
                self.label_frame_window = self.canvas.create_window(1200, 40, anchor=NW, window=self.label_frame)
            else:
                self.label_frame = Label(self, text=f"Frame {str(int(self.data.code.values[self.initial.get()]))}",
                                     anchor=W, bg="#FFFFFF")
                self.label_frame_window = self.canvas.create_window(1200, 40, anchor=NW, window=self.label_frame)

        else:
            pass

    def Close(self):
        self.destroy()



    def frame_pick (self, number):
        self.data.at[self.initial.get(),"code"]=number
        self.label_frame.destroy()
        self.label_frame = Label(self, text=f"Frame {str(int(self.data.code.values[self.initial.get()]))}", anchor=W, bg="#FFFFFF")
        self.label_frame_window = self.canvas.create_window(1200, 40, anchor=NW, window=self.label_frame)
        self.data.to_excel("testx.xlsx")

if __name__ == "__main__":
    app = Functionality()
    app.mainloop()