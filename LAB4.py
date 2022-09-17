from tkinter import *
import random
from tkinter import messagebox, Label


def clicked():
    code=''
    c=random.randint(0,3)
    numbers=[0,1,2,3,4,5,6,7,8,9]
    letters=['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    for j in range(4):
        for i in range(4):
            if i==c:
                code+=str(numbers[random.randint(0,9)])
            else:
                code+=letters[random.randint(0, 25)]
        if j!=3:
            code+='-'
    messagebox.showinfo(title=None, message=code)

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('662x532')
window.image=PhotoImage(file='Brawl_Stars.png')
bg_logo: Label=Label(window,image=window.image)
bg_logo.grid(row=0,column=0)
txt = Entry(window, width=10)
txt.grid(column=1, row=0)
txt.place(relx=.5, rely=.1, anchor="c")
btn = Button(window, text="создать ключ!", command=clicked)
btn.grid(column=2, row=0)
btn.place(relx=.5, rely=.5, anchor="c")
window.mainloop()