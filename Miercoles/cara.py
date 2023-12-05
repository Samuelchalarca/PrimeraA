from tkinter import *

ventana = Tk()
c = Canvas(ventana,width=500, height=500)
ventana.geometry("500x500")
c.place(x=0,y=0)
c.create_rectangle(0,0,500,500, fill="#4682B4")
c.create_oval(180,180,320,320,fill="#FFEBCD")
c.create_polygon(160,210,340,210,250,150, fill="yellow")
c.create_line(210,240,240,240, width=3.0)
c.create_line(260,240,290,240, width=3.0)
c.create_line(230,270,270,270, width=3.0)
ventana.mainloop()