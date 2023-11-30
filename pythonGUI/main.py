import customtkinter
import math

root = customtkinter.CTk()

#Functions

def math_solver():
    print('not yet done')

#Window Logic
root.title("Calc")
root.geometry("175x375")
root.resizable(False, False)

#Frames Logic
entry= customtkinter.CTkEntry(root)
entry.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
button_plus = customtkinter.CTkButton(root, text="+",command=math_solver)
button_plus.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=2,)
button_sub = customtkinter.CTkButton(root, text="-")
button_sub.grid(row=2, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
button_mul = customtkinter.CTkButton(root, text="*")
button_mul.grid(row=3, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
button_div = customtkinter.CTkButton(root, text="/")
button_div.grid(row=4, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

#Runs the Program
root.mainloop()
