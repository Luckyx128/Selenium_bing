from doctest import master

import customtkinter
import threading
from main import main as flux

def button_callback():
    #TODO: ober a informação digitada nos entry email e senha
    rotina = threading.Thread(target=flux)
    rotina.start()

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title('Ferramenta de busca automatizada!')
        self.geometry("400x500")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0,1,2), weight=1)

        self.FTop = FTop(master=self)
        self.FTop.grid(row=0,column=0,padx=20, pady=20, sticky="nsew")
        self.Fmid = FMid(master=self)
        self.Fmid.grid(row=1, column=0, padx=20, pady=20, sticky="nsew")
        self.FFooter = FFooter(master=self)
        self.FFooter.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

class FTop(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.email = customtkinter.CTkEntry(self, placeholder_text="Seu email aqui")
        self.email.grid(row=0, column=0, sticky="nsew")

        self.senha = customtkinter.CTkEntry(self, placeholder_text="Sua senha aqui")
        self.senha.grid(row=1,column=0,sticky="nsew")

    def get(self,entry:str) -> str:
        match entry:
            case 'senha':
                return  self.senha.get()
            case 'email':
                return  self.email.get()
class FMid(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.button = customtkinter.CTkButton(self, text="Iniciar pesquisas", command=button_callback)
        self.button.pack(padx=20, pady=20)

class FFooter(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # add widgets onto the frame, for example:
        self.textbox = customtkinter.CTkTextbox(master=self, width=400, corner_radius=0)
        self.textbox.grid(row=0, column=0, sticky="nsew")
        self.textbox.insert("0.0", "Some example text!\n")

if __name__ == '__main__':
    app = App()
    app.mainloop()