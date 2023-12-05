from tkinter import *
ventana = Tk()
ventana.title("posicionamiento")
ventana.geometry("400x200")
boton = Button(ventana, text="posicionamiento diferente").place(x=10, y=10)
etiqueta = Label(ventana, text="posicionamiento diferente").place(x=200, y=10)
etiqueta2 = Label(ventana, text="posicionamiento diferente 2").place(x=10, y=30)
etiqueta3 = Label(ventana, text="posicionamiento diferente 3").place(x=200, y=30)
ventana.mainloop()