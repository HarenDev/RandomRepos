import customtkinter
import math

#define window settings
app = customtkinter.CTk()
app.title('Calculator')
app.geometry('315x175')

def math_solver(fun):
    entry_text = entry.get()

    if fun==1:
        entry_len = len(entry_text)
        entry.insert(entry_len,'+')
    elif fun==2:
        entry_len = len(entry_text)
        entry.insert(entry_len,'-')
    elif fun==3:
        entry_len = len(entry_text)
        entry.insert(entry_len,'*')
    elif fun==4:
        entry_len = len(entry_text)
        entry.insert(entry_len,'/')
    elif fun==5:
        entry.delete(0,customtkinter.END)
        entry.insert(0,eval(entry_text))

#buttons and things
entry = customtkinter.CTkEntry(app)
entry.grid(row=0,column=0,columnspan=2,pady=10)

plus = customtkinter.CTkButton(app,text='+',command=lambda: math_solver(1))
plus.grid(row=1,column=0,padx=10,pady=10)

minus = customtkinter.CTkButton(app,text='-',command=lambda: math_solver(2))
minus.grid(row=1,column=1)

multiply = customtkinter.CTkButton(app,text='*',command=lambda: math_solver(3))
multiply.grid(row=2,column=0)

divide = customtkinter.CTkButton(app,text='/',command=lambda: math_solver(4))
divide.grid(row=2,column=1)

equals = customtkinter.CTkButton(app,text='=',command=lambda: math_solver(5))
equals.grid(row=3,column=0,columnspan=2,pady=10)

app.mainloop()