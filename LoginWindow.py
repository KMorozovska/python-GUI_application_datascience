from WelcomeWindow import *
from Constants import PASSWORD

class LoginWindow(ttk.Frame):

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

        l2 = ttk.Label(self, text="Login:", style="txt.TLabel")
        l2.place(x=140, y=200)

        page1 = IntVar()
        page1.set("")
        self.login_entry = Entry(self)
        self.login_entry.place(x=200, y=200, width=150)

        l3 = ttk.Label(self, text="Hasło:", style="txt.TLabel")
        l3.place(x=140, y=240)

        page2 = IntVar()
        page2.set("")
        self.pass_entry = Entry(self,show="*")
        self.pass_entry.place(x=200, y=240, width=150)

        b2 = ttk.Button(self,text="Zaloguj się",command=lambda : self.open_product_window())
        b2.place(x=210, y=320)


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

        print("login: " + str(self.login_entry.get()) + "hasło: " + str(self.pass_entry.get()))

        if not self.login_entry.get() and not self.pass_entry.get():
            showinfo("Error", "Proszę wpisać login i hasło")

        else:
            if str(self.pass_entry.get()) != PASSWORD:
                showinfo("Error", "Hasło jest nieprawidłowe")
            else:
                for widget in self.master.winfo_children():
                    widget.destroy()

                WelcomeWindow(self.master)



