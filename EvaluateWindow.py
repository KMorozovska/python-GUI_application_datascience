import tkinter.ttk as ttk
from ProduceData import *
from AutocompleteEntry import *
from tkinter.messagebox import showinfo


class EvaluateWindow(ttk.Frame):

    def __init__(self, chosen_item,chosen_datasource, master=None):
        ttk.Frame.__init__(self, master)

        self.master = master
        self.master.maxsize(500, 500)
        self.master.minsize(500, 500)
        self.master.title("Żabka")

        self.chosen_item = chosen_item
        self.chosen_datasource = chosen_datasource

        self.pack(fill=BOTH, expand=True)
        self.layout()

    def layout(self):

        title = ttk.Label(self, text="Produkty \n najczęściej kupowane razem \n z:"+ str(self.chosen_item), style="title.TLabel")
        title.place(x=0, y=60)


        l7 = ttk.Label(self, text="Wybierz ilość wyświetlanych produktów: ", style="txt.TLabel")
        l7.place(x=20, y=180)

        tkvar = StringVar()

        choices = {1,2,3,4,5}
        tkvar.set(3)  # set the default option

        popupMenu = OptionMenu(self, tkvar, *choices)
        popupMenu.grid(row=2, column=1)
        popupMenu.place(x=30, y=300)

        b2 = ttk.Button(self, text="Ok", command=lambda: self.ok_button_clicked())
        b2.place(x=300, y=227)


        # ----------- STYLES ------------

        style = ttk.Style()

        style.configure("TFrame",
                        background="#607D8B"
                        )
        style.configure("title.TLabel",
                        background="#455A64",
                        foreground="#42A5F5",
                        font="Arial 16 bold",
                        width=500,
                        padding=10
                        )
        style.configure("txt.TLabel",
                        background="#607D8B",
                        foreground="#B0BEC5",
                        font="Arial 12",
                        )
        style.configure("TButton",
                        background="#607D8B",
                        foreground="#455A64",
                        font="Arial 9 bold"
                        )
        style.configure("TCheckbutton",
                        background="#607D8B",
                        foreground="#B0BEC5",
                        font="Arial 12"
                        )
        style.configure("warning.TLabel",
                        background="#607D8B",
                        foreground="#B0BEC5",
                        font="Arial 10 bold",
                        )
        style.configure("status.TLabel",
                        background="#607D8B",
                        foreground="#B0BEC5",
                        font="Arial 12",
                        )
