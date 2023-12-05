from tkinter import *
ventana = Tk()
ventana.title("esta es mi primera ventana")
''
boton = Button(ventana, text="minimizar", command=ventana.iconify)
boton.pack()
etiqueta = Label(ventana,text="hola mundo en python")
etiqueta.pack()
etiqueta.mainloop()