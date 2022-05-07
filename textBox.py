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


vnta.geometry("300x300")
caja = Entry(vnta, textvariable= info, width=10, bg="#B7F1F7", fg="black", font=("Arial",18, "bold")).place(x=80, y=80)

palabra = Label(vnta, textvariable=palabrita, font=("Arial", 22, "bold")).place(x=20, y=20)

boton = Button(vnta, text="Mostrar", font=("Arial", 16), command=mostrar).place(x=20, y=130)

botonI = Button(vnta, text="Nueva Partida", font=("Arial", 16), command=lambda: nuevaPartida()).place(x=120, y=130)



vnta.mainloop()