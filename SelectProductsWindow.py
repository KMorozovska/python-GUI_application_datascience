from tkinter import *
import tkinter.ttk as ttk


class SelectProductsWindow(ttk.Frame):

    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)

        self.master = master
        self.master.maxsize(500, 500)
        self.master.minsize(500, 500)
        self.master.title("Żabka")

        self.pack(fill=BOTH, expand=True)

        self.layout()

    def layout(self):

        b1 = ttk.Button(self, text="Powrót")
        b1.place(x=10, y=20)

        title = ttk.Label(self, text="Analiza \nnajchętniej kupowanych razem \nproduktów", style="title.TLabel")
        title.place(x=0, y=60)


        l7 = ttk.Label(self, text="Przeprowadź analizę na podstawie danych:", style="txt.TLabel")
        l7.place(x=10, y=160)

        self.var = IntVar()
        self.var.set(1)
        R1 = Radiobutton(self, text="Z mojej lokalizacji", variable=self.var, value=1)
        R1.pack(anchor=W)
        R1.place(x=20, y=190)

        R2 = Radiobutton(self, text="Ze wszystkich dostępnych danych", variable=self.var, value=2)
        R2.pack(anchor=W)
        R2.place(x=20, y=210)


        #l2 = ttk.Label(self, text="Lokalizacja:", style="txt.TLabel")
        #l2.place(x=10, y=350)

        #page1 = IntVar()
        #page1.set("")
        #e2 = Entry(self, textvariable=page1, bg="#CFD8DC", fg="#455A64", font="Arial 10 bold")
        #e2.place(x=10, y=370, width=150)


        l1 = ttk.Label(self, text="Przegladaj produkty:", style="txt.TLabel")
        l1.place(x=10, y=270)

        # Create a Tkinter variable - dropdown list
        tkvar = StringVar()
        # Dictionary with options
        choices = {'Pizza', 'Lasagne', 'Fries', 'Fish', 'Potatoe'}
        tkvar.set('Pizza')  # set the default option
        popupMenu = OptionMenu(self, tkvar, *choices)
        # Label(self, text="Choose a dish").grid(row=1, column=1)
        popupMenu.grid(row=2, column=1)
        popupMenu.place(x=30, y=300)


        b2 = ttk.Button(self, text="Start")
        b2.place(x=220, y=400)

        #b3 = ttk.Button(self, text="Stop")
        #b3.place(x=120, y=415)

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

