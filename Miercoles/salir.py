from tkinter import *

def imprime():
    print("Acabas de presionar el boton Imprimir")

ventana = Tk()
ventana.title("segunda ventana")
botons = Button (ventana, text = "salir",fg= "red", command = ventana.quit)
botons.pack(side=LEFT)
boton = Button (ventana, text="Imprimir",fg= "blue", command = imprime)
boton.pack(side=RIGHT)
ventana.mainloop()