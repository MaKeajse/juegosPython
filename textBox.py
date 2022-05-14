from cProfile import label
from email import message
from re import A
from tkinter import *
from tkinter import font
from tkinter import messagebox as msg
from tkinter import simpledialog
import random as r
from tkinter.messagebox import askyesno

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
            #continuar = simpledialog.askstring("CONTINUAR","Desea continuar ingrese (s): ").upper()
            answer = askyesno(title='confirmation',
                    message='Desea Continuar?')

            if answer:
                nuevaPartida()

            else:
                msg.showinfo("Mensaje", "El juego ha terminado")
                vnta.destroy()
            """if continuar == "S":
                nuevaPartida()
            else:
                msg.showinfo("Mensaje", "El juego ha terminado")
                vnta.destroy()"""
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

def reorganiza():
    desorden = r.sample(nueva,len(nueva))
    if desorden == nueva:
        desorden = r.sample(nueva,len(nueva))
    palabrita.set(desorden)
    



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

boton = Button(vnta, text="Mostrar", font=("Arial", 14), command=mostrar).place(x=20, y=150)

botonI = Button(vnta, text="Nueva Partida", font=("Arial", 14), command=lambda: nuevaPartida()).place(x=115, y=150)

botonR = Button(vnta, text="Reorganizar", font=("Arial", 14), command=lambda: reorganiza()).place(x=260, y=150)

realizado = Label(vnta, text="Realizado por Laura Juliana Serrano García - Makeajse", bg="#C7F9F4").pack(side="bottom")

vnta.mainloop()