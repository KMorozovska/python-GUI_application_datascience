import tkinter.ttk as ttk
from AutocompleteEntry import *
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure



class EvaluateWindow(ttk.Frame):

    def __init__(self, chosen_item,products_list, master=None):
        ttk.Frame.__init__(self, master)

        self.master = master
        self.master.maxsize(600, 600)
        self.master.minsize(600, 600)
        self.master.title("Żabka")

        self.chosen_item = chosen_item
        self.final_products_list = products_list

        self.fig = Figure(figsize=(1, 1), dpi=80, facecolor="#455A64")
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)  # A tk.DrawingArea

        self.pack(fill=BOTH, expand=True)
        self.layout()

    def layout(self):



        title = ttk.Label(self, text="Produkty \nnajczęściej kupowane razem \nz produktem: "+ str(self.chosen_item), style="title.TLabel")
        title.place(x=10, y=60)


        l7 = ttk.Label(self, text="Wybierz ilość wyświetlanych produktów: ", style="txt.TLabel")
        l7.place(x=20, y=180)

        self.tkvar = StringVar()
        choices = {1,2,3,4,5,6,7,8,9,10}
        self.tkvar.set(3)  # set the default option

        popupMenu = OptionMenu(self, self.tkvar, *choices)
        popupMenu.grid(row=2, column=1)
        popupMenu.place(x=350, y=170)

        b2 = ttk.Button(self, text="Ok", command=lambda : self.draw_piechart())
        b2.place(x=200, y=227)


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



    def draw_piechart(self):

        zawartosc_query = 'ID_PRODUKTU not in ("Reklamówki 1", "Reklamówki 2","Reklamówki 3", ' + "\"" + self.chosen_item + "\")"
        wyniki = self.final_products_list.reset_index(drop=True).query(zawartosc_query).head(int(self.tkvar.get()))

        # ---------- drawing actual chart

        self.a = self.fig.add_subplot(111)
        self.a.clear()
        self.a.pie(wyniki['Ilosc'], labels=wyniki['ID_PRODUKTU'])

        self.canvas.draw()
        self.canvas.get_tk_widget().pack(fill=BOTH, expand=1)
