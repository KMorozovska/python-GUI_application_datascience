from EvaluateWindow import *
from LocationEntryPopup import *
from ProduceData import *


class SelectProductsWindow(ttk.Frame):

    def __init__(self, master=None):
        ttk.Frame.__init__(self, master)

        self.master = master
        self.master.maxsize(500, 500)
        self.master.minsize(500, 500)
        self.master.title("Żabka")

        self.pack(fill=BOTH, expand=True)
        self.product_list = []
        self.layout()

    def layout(self):

        b1 = ttk.Button(self, text="Powrót",command=lambda : self.back_to_mainwindow())
        b1.place(x=10, y=20)

        title = ttk.Label(self, text="Analiza \nnajchętniej kupowanych razem \nproduktów", style="title.TLabel")
        title.place(x=0, y=60)


        l7 = ttk.Label(self, text="Przeprowadź analizę na podstawie danych:", style="txt.TLabel")
        l7.place(x=20, y=180)

        self.choose_datasource_buttons = IntVar()
        self.choose_datasource_buttons.set(1)
        self.R1 = Radiobutton(self, text="Z mojej lokalizacji", variable=self.choose_datasource_buttons, value=1,command=selected(self))
        self.R1.pack(anchor=W)
        self.R1.place(x=30, y=210)

        self.R2 = Radiobutton(self, text="Ze wszystkich dostępnych danych", variable=self.choose_datasource_buttons, value=2,command=selected(self))
        self.R2.pack(anchor=W)
        self.R2.place(x=30, y=230)

        b2 = ttk.Button(self, text="Ok", command=lambda: self.ok_button_clicked())
        b2.place(x=300, y=227)

        l2 = ttk.Label(self, text="Wpisz produkt, który Cię interesuje:", style="txt.TLabel")
        l2.place(x=20, y=285)

        page1 = IntVar()
        page1.set("")
        self.product_entry = Entry(self,state='disabled')
        self.product_entry.place(x=30, y=320, width=150)


        self.startButton = ttk.Button(self, text="Start",state='disabled',command=lambda : self.start_button_clicked())
        self.startButton.place(x=220, y=400)

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

    def back_to_mainwindow(self):
        for widget in self.master.winfo_children():
            widget.destroy()




    def ok_button_clicked(self):

        print("Chosen option is: " + str(self.choose_datasource_buttons.get()))
        self.R1.configure(state=DISABLED)
        self.R2.configure(state=DISABLED)

        if self.choose_datasource_buttons.get() == 2:
            self.chosen_datasource = "all"
            self.load_data()

        else:
            popup = LocationEntryPopup(self.master)
            self.master.wait_window(popup.top)
            print('wpisana wartosc lokalizacji: ' + popup.value)

            # przykladowo : LOK_6883

            self.chosen_datasource = popup.value
            self.load_data()

        self.product_entry = AutocompleteEntry(self.product_list, self, state='normal')
        self.product_entry.place(x=30, y=320, width=150)
        self.startButton.configure(state='normal')

    def start_button_clicked(self):
        if not self.product_entry.var.get():
            showinfo("Error", "Proszę wybrać produkt")
        else:
            for widget in self.master.winfo_children():
                widget.destroy()

            self.evaluation_list = self.produced_data.analyse_corelated_products(self.chosen_datasource, self.product_entry.var.get())
            app = EvaluateWindow(self.product_entry.var.get(), self.evaluation_list,self.master)

    def load_data(self):
        self.produced_data = ProduceData()
        self.product_list = self.produced_data.list_of_products(self.chosen_datasource)


def selected(self):
    print(self.choose_datasource_buttons.get())

