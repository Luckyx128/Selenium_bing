import customtkinter
import threading
from main import main as flux
def button_callback():
    main = threading.Thread(target=flux)
    main.start()
app = customtkinter.CTk()
app.geometry("400x150")

button = customtkinter.CTkButton(app, text="my button", command=button_callback)
button.pack(padx=20, pady=20)

app.mainloop()