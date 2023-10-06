import customtkinter
customtkinter.set_appearance_mode("System")
# def functions
def mathsolver():


# main frame details
frame = customtkinter.CTk()
frame.geometry("400x300")
frame.title("This Works")

# user input
entry = customtkinter.CTkEntry(frame, placeholder_text="Enter a value", justify="center")
entry.grid(anchor="NE")

# buttons
plus = customtkinter.CTkButton(frame, text="+") #command=buttonclick)
plus.grid(row=1, column=0, padx=10, pady=10)

minus = customtkinter.CTkButton(frame, text="-") #command=buttonclick)
minus.grid(row=1, column=1, padx=10, pady=10)

mul = customtkinter.CTkButton(frame, text="*") #command=buttonclick)
mul.grid(row=2, column=0, padx=10, pady=10)

div = customtkinter.CTkButton(frame, text="/") #command=buttonclick)
div.grid(row=2, column=1, padx=10, pady=10)

equal = customtkinter.CTkButton(frame, text="=") #command=buttonclick)
equal.grid(row=3, column=0, padx=10, pady=10)

# main program loop
frame.mainloop()
