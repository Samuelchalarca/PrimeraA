from tkinter import *
from tkinter import messagebox

lista = []

def anadir():
    t = titulo.get()
    a = autor.get()
    e = editorial.get()
    np = NdePaginas.get()
    fl = fechalimite.get()
    lista.append(t + "$" + a + "$" + e + "$" + str(np) + "$" + fl)
    escribir_libro()
    messagebox.showinfo("Guardado", "El libro que tiene que leer ha sido guardado")
    titulo.set("")
    autor.set("")
    editorial.set("")
    NdePaginas.set("")
    fechalimite.set("")
    consultar()

def escribir_libro():
    archivo = open("biblioteca.txt", "w")
    lista.sort()
    for elementos in lista:
        archivo.write(elementos + "\n")
    archivo.close()

def eliminar_libro():
    eliminado = eliminarlibro.get()
    removido = False
    for elemento in lista:
        arreglo = elemento.split("$")
        if eliminarlibro.get() == arreglo[0]:
            respuesta = messagebox.askyesno("Eliminar libro", f"Desea eliminar el libro con el título:\n{eliminado}")
            if respuesta:
                lista.remove(elemento)
                removido = True
                escribir_libro()
                consultar()
                respuesta = ""
    if removido:
        messagebox.showinfo("Eliminar", f"Se ha eliminado el título:\n{eliminado}")

def salir():
    sa = messagebox.askyesno("Salir", "¿Deseas finalizar?")
    if sa:
        quit()

def iniciar_archivo():
    archivo = open("biblioteca.txt", "a")
    archivo.close()

def cargar():
    archivo = open("biblioteca.txt", "r")
    linea = archivo.readline()
    if linea:
        while linea:
            if linea[-1] == '\n':
                linea = linea[:-1]
            lista.append(linea)
            linea = archivo.readline()
        archivo.close()

def consultar():
    r = Text(ventana, width=80, height=15)
    lista.sort()
    valores = []

    r.insert(INSERT, "\tTitulo del libro\n")
    r.insert(INSERT, "---\n")

    for elemento in lista:
        arreglo = elemento.split("$")
        valores.append(arreglo[0])
        r.insert(INSERT, f"\t{arreglo[0]}\n Autor: {arreglo[1]}\tEditorial: {arreglo[2]}\tN° de páginas: {arreglo[3]}\tFecha límite: {arreglo[4]}\n")
        r.insert(INSERT, "---\n")

    spinTitulo = Spinbox(ventana, values=(valores), textvariable=eliminarlibro, width=70)
    spinTitulo.place(x=110, y=450)

    r.place(x=30, y=195)

    if not lista:
        spinTitulo = Spinbox(ventana, values=(valores), width=70)
        spinTitulo.place(x=110, y=450)

    r.config(state=DISABLED)

ventana = Tk()

titulo = StringVar()
autor = StringVar()
editorial = StringVar()
NdePaginas = IntVar()
fechalimite = StringVar()
eliminarlibro = StringVar()

colorFondo = "#006"
colorLetra = "#FFF"

iniciar_archivo()
cargar()
consultar()

ventana.title("Relación de libros que tengo que leer")
ventana.geometry("700x500")
ventana.configure(background=colorFondo)

etiquetaTitulo = Label(ventana, text="Relación de libros que tengo que leer", bg=colorFondo, fg=colorLetra)
etiquetaTitulo.place(x=250, y=10)

eTitulo = Label(ventana, text="Título: ", bg=colorFondo, fg=colorLetra)
eTitulo.place(x=30, y=40)
cTitulo = Entry(ventana, textvariable=titulo, width=70)
cTitulo.place(x=120, y=40)

eAutor = Label(ventana, text="Autor: ", bg=colorFondo, fg=colorLetra)
eAutor.place(x=30, y=70)
cAutor = Entry(ventana, textvariable=autor)
cAutor.place(x=120, y=70)

eEditorial = Label(ventana, text="Editorial:", bg=colorFondo, fg=colorLetra)
eEditorial.place(x=30, y=100)
cEditorial = Entry(ventana, textvariable=editorial)
cEditorial.place(x=120, y=100)

eNpaginas = Label(ventana, text="N° de páginas: ", bg=colorFondo, fg=colorLetra)
eNpaginas.place(x=30, y=130)
cNpaginas = Entry(ventana, textvariable=NdePaginas)
cNpaginas.place(x=120, y=130)

eFechaLimite = Label(ventana, text="Fecha límite: ", bg=colorFondo, fg=colorLetra)
eFechaLimite.place(x=30, y=160)
cFechaLimite = Entry(ventana, textvariable=fechalimite)
cFechaLimite.place(x=120, y=160)

botonAnadir = Button(ventana, text="Añadir libro", command=anadir, bg="#009", fg="white")
botonAnadir.place(x=550, y=38)

spinTitulo = Label(ventana, text="Título leído:", bg=colorFondo, fg=colorLetra)
spinTitulo.place(x=30, y=450)

botonLeido = Button(ventana, text="Libro ya leído", command=eliminar_libro, bg="#009", fg="white")
botonLeido.place(x=550, y=448)

# Assuming you have defined an image variable (imgbtn) for the button
# imgbtn = PhotoImage(file="salir.png")
salirButton = Button(ventana, command=salir)
salirButton.place(x=300, y=60)

mainloop()
