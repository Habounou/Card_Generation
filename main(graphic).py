import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
app.after(0, lambda:app.state('zoomed'))

def login():
    frame = customtkinter.CTkFrame(master=app, width=250, height=350)
    frame.grid(row=0, column=0, pady=20, padx=60)
    frame.grid_propagate(False)
    frame.grid_columnconfigure(0, weight=1)
    frame.grid_rowconfigure(5, weight=1)

    frame2 = customtkinter.CTkFrame(master=frame, width=250, height=26, corner_radius=0, fg_color="#1167B1")
    frame2.grid(row=0, column=0, sticky="ne")
    frame2.grid_propagate(False)
    frame2.grid_columnconfigure(0, weight=1)

    exit_button = customtkinter.CTkButton(master=frame2, text="⨉", fg_color="transparent", hover_color="#C21A09",
                                          corner_radius=0, width=40, height=24, command=lambda: exit())
    exit_button.grid(row=0, column=0, sticky="ne", padx=2)

    label = customtkinter.CTkLabel(master=frame, text="Welcome", font=("Roboto", 24))
    label.grid(row=1, column=0, pady=30, padx=10)

    entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
    entry1.grid(row=2, column=0, pady=12, padx=10)

    entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show = "*")
    entry2.grid(row=3, column=0, pady=12, padx=10)

    login_button = customtkinter.CTkButton(master=frame, text="Login", command=screen1)
    login_button.grid(row=4, column=0, pady=12, padx=10)

    checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
    checkbox.grid(row=5, column=0, pady=12, padx=10)

def screen1():
    frame3 = customtkinter.CTkFrame(master=app, width=1400, height=800)
    frame3.grid(row=0, column=0, pady=20, padx=60)
    frame3.grid_propagate(False)
    frame3.grid_columnconfigure(0, weight=1)
    frame3.grid_rowconfigure(0, weight=1)

    def return_login():
        login()
        frame3.destroy()

    frame4 = customtkinter.CTkFrame(master=frame3, width=1400, height=30, corner_radius=0, fg_color="#1167B1")
    frame4.grid(row=0, column=0, sticky="ne")
    frame4.grid_propagate(False)
    frame4.grid_columnconfigure(0, weight=1)

    return_button = customtkinter.CTkButton(master=frame4, text="↩", font=("Roboto", 28), fg_color="transparent",
                                            hover_color="#C21A09", corner_radius=0, width=50, height=28,
                                            command=return_login)
    return_button.grid(row=0, column=0, sticky="ne")
    return_button.grid_propagate(False)

    frame5 = customtkinter.CTkFrame(master=frame3, width=400, height=700)
    frame5.grid(row=0, column=0, sticky="nw", pady=50, padx=20)
    frame5.grid_propagate(False)
    frame5.grid_columnconfigure(0, weight=1)

    label = customtkinter.CTkLabel(master=frame5, text="Digital Duel Card Creator", font=("Roboto", 32))
    label.grid(row=0, column=0, sticky="n", pady=12)

login()

app.mainloop()