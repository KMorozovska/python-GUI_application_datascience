from SelectProductsWindow import *


class WelcomeWindow(ttk.Frame):

    def __init__(self, master):
        ttk.Frame.__init__(self, master)

        self.master = master
        self.master.maxsize(500, 500)
        self.master.minsize(500, 500)
        self.master.title("Żabka")

        self.pack(fill=BOTH, expand=True)

        self.layout()

    def layout(self):
        title = ttk.Label(self, text="Analiza sprzedaży produktów", style="title.TLabel")
        title.place(x=0, y=30)


        b2 = ttk.Button(self,text="Zbadaj korelacje pomiędzy produktami",command=lambda : self.open_product_window())
        b2.place(x=115, y=200)

        b3 = ttk.Button(self, text="Sprawdź historię popytu")
        b3.place(x=165, y=250)

        # ----------- STYLES ------------

        style = ttk.Style()

        style.configure("TFrame",
                        background="#607D8B"
                        )
        style.configure("title.TLabel",
                        background="#455A64",
                        foreground="#42A5F5",
                        font="Arial 20 bold",
                        width=500,
                        padding=10
                        )

        style.configure("txt.TLabel",
                        background="#607D8B",
                        foreground="#B0BEC5",
                        font="Arial 12",
                        )


    def open_product_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

        SelectProductsWindow(self.master)
