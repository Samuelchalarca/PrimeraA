from tkinter import *

ventana = Tk()
c = Canvas(ventana, width=200, height=200)
ventana.geometry("500x500")

for i in range (0, 10):
    if i % 2 == 0 :   
        c.create_oval(i * 10, i * 10, 200 - (i * 10), 200 - (i * 10), fill="red")
    else:
        c.create_oval(i * 10, i * 10, 200 - (i * 10), 200 - (i * 10), fill="white")

c.place(x=0,y=0)
ventana.mainloop()