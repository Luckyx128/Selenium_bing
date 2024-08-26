import customtkinter
import threading
from main import main as flux

def button_callback():
    rotina = threading.Thread(target=flux)
    rotina.start()

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Ferramenta de busca automatizada!')
        self.geometry("400x500")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0,1), weight=1)

        self.my_frame1 = MyFrame1(master=self)
        self.my_frame1.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        self.my_frame2 = MyFrame2(master=self)
        self.my_frame2.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")

class MyFrame1(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.button = customtkinter.CTkButton(self, text="Iniciar pesquisas", command=button_callback)
        self.button.pack(padx=20, pady=20)

class MyFrame2(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.textbox = customtkinter.CTkTextbox(master=self, width=400, corner_radius=0)
        self.textbox.grid(row=0, column=0, sticky="nsew")
        self.textbox.insert("0.0", "Some example text!\n")

if __name__ == '__main__':
    app = App()
    app.mainloop()