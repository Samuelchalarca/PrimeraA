from tkinter import *
ventana = Tk()
c = Canvas(ventana, width=200, height=200)
ventana.geometry("500x500")
#rgb nivel rojo, nivel verde, nivel azul
#color = "#009"
#c.create_oval(10,10,100,100,fill=color)
c.create_oval(10,10,100,100,fill="blue")
c.create_oval(20,20,80,80,fill="yellow")
c.place(x=0,y=0)

ventana.mainloop()