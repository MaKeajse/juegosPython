from cProfile import label
from tkinter import *
from tkinter import font
from tkinter import messagebox as msg
from tkinter import simpledialog
import random as r

vnta = Tk()

def mostrar():
    variable = info.get()
    #nueva = nueva
    #msg.showinfo("Mensaje", variable)
    if variable.upper() == nueva:
        msg.showinfo("Mensaje", "Correcto")
        #palabrita.set("")
        variable = info.set("")      

        try:
            continuar = simpledialog.askstring("CONTINUAR","Desea continuar ingrese (s): ").upper()
            if continuar == "S":
                nuevaPartida()
            else:
                msg.showinfo("Mensaje", "El juego ha terminado")
                vnta.destroy()
        except Exception as ex:
            msg.showinfo("Mensaje", "El juego ha terminado")
            vnta.destroy()
            
    else:
        msg.showinfo("Mensaje", "Palabra Equivocada")
        variable = info.set("")

def nuevaPartida():    
    #msg.showinfo("Mensaje", "Prueba")
    global nueva
    listaPalabras = ("SANTIDAD","CAMINO","DIOS","UNIDAD")
    nueva=listaPalabras[r.randint(0,len(listaPalabras)-1)]
    desorden = r.sample(nueva,len(nueva))
    palabrita.set(desorden)
    return nueva
    



#Crear variable a utilizar en la caja (Declaración de variable)
info = StringVar()
palabrita = StringVar()
#texto = "SANTIDAD"
#listaPalabras = ("SANTIDAD","CAMINO","DIOS","UNIDAD")
#nueva=listaPalabras[r.randint(0,len(listaPalabras)-1)]
#desorden = r.sample(nueva,len(nueva))


vnta.geometry("400x240")
vnta.config(bg="#C7F9F4")
vnta.title("Adivina la Palabra")
vnta.maxsize(width=400, height=240)

espacio = Label(vnta,bg="#C7F9F4").pack()
palabra = Label(vnta, textvariable=palabrita, font=("Arial", 22, "bold"), bg="#86EFFB").pack(fill="x")

caja = Entry(vnta, textvariable= info, width=22, fg="black", font=("Arial",20, "bold")).place(x=30, y=85)

boton = Button(vnta, text="Mostrar", font=("Arial", 16), command=mostrar).place(x=80, y=150)

botonI = Button(vnta, text="Nueva Partida", font=("Arial", 16), command=lambda: nuevaPartida()).place(x=180, y=150)

realizado = Label(vnta, text="Realizado por Laura Juliana Serrano García - Makeajse", bg="#C7F9F4").pack(side="bottom")

vnta.mainloop()