import customtkinter

customtkinter.set_appearance_mode("System")


# def functions
def mathsolver():
    print()


# main frame details


root = customtkinter.CTk()
root.maxsize(400,300)
root.title("This Works")


# base frames
frame_1 = customtkinter.CTkFrame(frame,)

# user input
entry = customtkinter.CTkEntry(frame, placeholder_text="Enter a value", justify="center")
entry.pack(padx=20, pady=20)

# result
result = customtkinter.CTkEntry(frame, placeholder_text="Result", justify="center")
result.pack(fill='x')

# buttons
plus = customtkinter.CTkButton(frame, text="+")  # command=buttonclick)
plus.pack(padx=10, pady=10)

minus = customtkinter.CTkButton(frame, text="-")  # command=buttonclick)
minus.pack(padx=10, pady=10)

mul = customtkinter.CTkButton(frame, text="*")  # command=buttonclick)
mul.pack(padx=10, pady=10)

div = customtkinter.CTkButton(frame, text="/")  # command=buttonclick)
div.pack(padx=10, pady=10)

equal = customtkinter.CTkButton(frame, text="=")  # command=buttonclick)
equal.pack(padx=10, pady=10)

# main program loop
frame.mainloop()
