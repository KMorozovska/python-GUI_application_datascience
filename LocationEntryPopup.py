from tkinter import *
from tkinter.messagebox import showinfo


class LocationEntryPopup(Frame):
    def __init__(self, master=None):
        super().__init__(master)

        self.top = Toplevel(master)
        self.label = Label(self.top, text="Wpisz kod lokalizacji")
        self.label.pack()
        self.entry = Entry(self.top)
        self.entry.pack()
        self.button = Button(self.top, text='Ok', command=self.closing_popup)
        self.button.pack()

    def closing_popup(self):
        self.value = self.entry.get()
        if not self.value:
            showinfo("Error", "Proszę uzupełnić lokalizację, przykładowy format: LOK_6883")
        else:
            self.top.destroy()