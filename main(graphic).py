import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
app.geometry("500x350")

def login():
    frame = customtkinter.CTkFrame(master=app)
    frame.grid(row=0, column=0, pady=20, padx=60)

    label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Roboto", 24))
    label.grid(row=0, column=0, pady=30, padx=10)

    entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
    entry1.grid(row=1, column=0, pady=12, padx=10)

    entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show = "*")
    entry2.grid(row=2, column=0, pady=12, padx=10)

    button = customtkinter.CTkButton(master=frame, text="Login", command=screen1)
    button.grid(row=3, column=0, pady=12, padx=10)

    checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
    checkbox.grid(row=4, column=0, pady=12, padx=10)

def screen1():
    frame2 = customtkinter.CTkFrame(master=app, width=500, height=350)
    frame2.grid(row=0, column=0, pady=20, padx=60)
    frame2.grid_propagate(False)
    frame2.grid_rowconfigure(0, weight=1)
    frame2.grid_columnconfigure(0, weight=1)

    def return_login():
        login()
        frame2.destroy()

    button2 = customtkinter.CTkButton(master=frame2, text="Back to login", command=return_login)
    button2.grid(row=3, column=0, pady=12, padx=10)

login()

app.mainloop()