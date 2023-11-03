import customtkinter
import math

root = customtkinter.CTk()

#Functions

#Frames Logic
button_plus = customtkinter.CTkButton(root, text="+")
button_plus.grid(row=0,column=0,padx=20,pady=20,sticky="ew",columnspan=2)
button_sub = customtkinter.CTkButton(root, text="-")
button_sub.grid(row=1,column=0,padx=20,pady=20,sticky="ew",columnspan=2)
button_mul = customtkinter.CTkButton(root, text="*")
button_mul.grid(row=2,column=0,padx=20,pady=20,sticky="ew",columnspan=2)
button_div = customtkinter.CTkButton(root, text="/")
button_div.grid(row=3,column=0,padx=20,pady=20,sticky="ew",columnspan=2)

#Window Logic
root.title("Calc")
root.geometry("200-40x400")
root.resizable(False,False)
root.mainloop()
