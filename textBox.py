from tkinter import *
from tkinter import font
from tkinter import messagebox as msg
import random as r



def mostrar():
    variable = info.get()
    #msg.showinfo("Mensaje", variable)
    if variable.upper() == nueva.upper():
        msg.showinfo("Mensaje", "Correcto")
       
    else:
        msg.showinfo("Mensaje", "Palabra Equivocada")

def nuevaPartida():    
    msg.showinfo("Mensaje", "Prueba")
    

vnta = Tk()

#Crear variable a utilizar en la caja (Declaración de variable)
info = StringVar()
#texto = "SANTIDAD"
listaPalabras = ("SANTIDAD","CAMINO","DIOS","UNIDAD")
nueva=listaPalabras[r.randint(0,len(listaPalabras)-1)]
desorden = r.sample(nueva,len(nueva))


vnta.geometry("300x300")
caja = Entry(vnta, textvariable= info, width=10, bg="#B7F1F7", fg="black", font=("Arial",18, "bold")).place(x=80, y=80)

palabra = Label(vnta, text=desorden, font=("Arial", 22, "bold")).place(x=20, y=20)

boton = Button(vnta, text="Mostrar", font=("Arial", 16), command=mostrar).place(x=20, y=130)

botonI = Button(vnta, text="Nueva Partida", font=("Arial", 16), command=nuevaPartida).place(x=120, y=130)



vnta.mainloop()