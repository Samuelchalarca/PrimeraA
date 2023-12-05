from tkinter import *

ventana = Tk()
c = Canvas(ventana,width=500, height=500)
ventana.geometry("500x500")
c.place(x=0,y=0)
c.create_rectangle(0,0,200,200, fill="blue")
c.create_rectangle(200,0,400,200,fill="yellow")
c.create_line(50,250,80,250,width=4.0) #por defecto 1.0
c.create_polygon(100,0,150,200,50,200,fill="green")
ventana.mainloop()