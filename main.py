# Created By Team SumShakti

# importing libraries
import tkinter as tk
from tkinter import ttk

# Class App
class App(tk.Tk):

    # __init__ function for class App
    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # Title and Layout size of App
        self.title('Latency Estimator')
        self.geometry('700x500')

        # Creating a container
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=False)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting of the different page layouts
        page_layout = (startPage, Bullet)
        for F in page_layout:
            frame = F(container, self)

            # initializing frame of that object from startPage, Bullet respectively with for loop
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(startPage)

    # to display the current frame passed as parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

# first window frame startPage
class startPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        button1 = ttk.Button(self, text="Bullet", command=lambda: controller.show_frame(Bullet))
        button1.grid(row=1, column=5, ipadx=10, ipady=20, padx=110, pady=40)

        button2 = ttk.Button(self, text="button2")
        button2.grid(row=1, column=7, ipadx=10, ipady=20, padx=40, pady=40)

        button3 = ttk.Button(self, text="button3")
        button3.grid(row=2, column=5, ipadx=10, ipady=20, padx=110, pady=40)

        button4 = ttk.Button(self, text="button4")
        button4.grid(row=2, column=7, ipadx=10, ipady=20, padx=40, pady=40)


class Bullet(tk.Frame):
    def calculate(self):
        time = int(self.e1.get()) / (int(self.e2.get()) - int(self.e3.get()))
        self.myText.set(time)

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.myText = tk.StringVar()
        tk.Label(self, text="Distance").grid(row=0, sticky=tk.W)
        tk.Label(self, text="Velocity of Bullet").grid(row=1, sticky=tk.W)
        tk.Label(self, text="Velocity of Target").grid(row=2, sticky=tk.W)
        tk.Label(self, text="Result:").grid(row=4, sticky=tk.W)
        tk.Label(self, text="", textvariable=self.myText).grid(row=4, column=1, sticky=tk.W)

        self.e1 = tk.Entry(self)
        self.e2 = tk.Entry(self)
        self.e3 = tk.Entry(self)

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        self.e3.grid(row=2, column=1)

        b = tk.Button(self, text="Calculate", command=lambda: self.calculate())
        b.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=tk.W + tk.E + tk.N + tk.S, padx=5, pady=5)


app = App()
app.mainloop()
