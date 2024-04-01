#!/usr/bin/env python3
from tkinter import *  

def clicked():
    name=txt.get()[::-1]
    lbname.configure(text=name) 
  
window = Tk()  
window.title("Добро пожаловать в приложение")  
window.geometry('400x250')  
lbl = Label(window, text="Введите свою Максимова_Матюшина")  
lbl.grid(column=0, row=0)  
lbname = Label(window, text='', height=3, font='Arial 30')
lbname.grid(column=2, row=2)  
txt = Entry(window,width=10)  
txt.grid(column=1, row=0)  
btn = Button(window, text="Нажмите!", command=clicked)  
btn.grid(column=2, row=0)  
window.mainloop()