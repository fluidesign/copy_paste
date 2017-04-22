#! python

## Many thanks to sentdex youtube channel
## https://www.youtube.com/channel/UCfzlCWGWYyIQ0aLC5w48gBQ

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import Listbox

LARGE_FONT = ("Verdana", 12)


class AppGui(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand = True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        ## add any newly created pages here to load them
        for page in (MainPage, SettingsPage):

            frame = page(container, self)

            self.frames[page] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


def exit_gui(self):
    if messagebox.askyesno("Exit", "Do you want to quit the application?"):
        self.master.destroy()



class MainPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="main page", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        closebutton = ttk.Button(self, text="Close",command=lambda:exit_gui(self))
        closebutton.pack()

        listBox = Listbox(self)
        listBox.insert(1, "list object number 1")
        listBox.pack()


class SettingsPage(ttk.Frame):

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="settings page", font="LARGE_FONT")
        label.pack(pady=10, padx=10)

        closeButton = ttk.Button(self, text="Close",command=lambda:exit_gui(self))
        closeButton.pack()


