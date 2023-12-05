from tkinter import *

def saludo():
    print("hola a todos")

def minimizar():
    ventana.iconify()

ventana = Tk()
ventana.title("Ejercicio numero 1")
ventana.geometry("400x200")
etiqueta1 = Label (ventana, text="desde aqui saludamos").place(x=30, y=50)
etiqueta2 = Label (ventana, text="desde aqui minimizamos").place(x=30, y=100)
boton1 = Button(ventana, text="dame click para saludar", command=saludo).place(x=200, y=50)
boton2 = Button(ventana, text="dame click para minimizar", command=minimizar).place(x=200, y=100)
ventana.mainloop()

