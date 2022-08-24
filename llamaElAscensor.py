from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
import random as ra
import time

class Ascensor():

    def __init__(self):
        self.pisoActual = 1

    def subir(self):
        if self.pisoActual <10:
            self.pisoActual +=1
    
    def baja(self):
        if self.pisoActual > 1:
            self.pisoActual -= 1  

    def ascensorNorte(self):
        pisoAscNorte = ra.randint(1,10)
        return pisoAscNorte

    def ascensorSur(self):
        pisoAscSur = ra.randint(1,10)
        return pisoAscSur

    def llamarAscensor(self):
        asc = simpledialog.askstring('Ascensor',"1. Norte - 2. Sur ")
        if asc == '1':
            botonesNorte[0].config(bg="violet",state="normal")
            botonesSur[0].config(bg=colorAscS, state="disable")
        elif asc == '2':
            botonesSur[0].config(bg="violet", state="normal")
            botonesNorte[0].config(bg=colorAscN, state="disable")
        else:
            messagebox.showerror("Opción no válida", "Vuelva a intentarlo")
    
    def moverAscensorNorte(self):
        global pisoNorte
        pisoActual = simpledialog.askinteger("Piso Actual", "¿En qué piso se encuentra?")

        if pisoActual < pisoNorte:
            messagebox.showinfo("Estado", "Ascensor Bajando")
        else:
            messagebox.showinfo("Estado", "Ascensor Subiendo")

        botonesNorte[pisoNorte].config(bg=coloresAscN)
        botonesNorte[pisoActual].config(bg="green")

        irA = simpledialog.askinteger("Ir a", "¿A qué piso se dirige?")

        if irA > pisoActual and irA <= 10:
            for i in range(pisoActual, irA):
                pisoActual += 1
                botonesNorte[pisoActual].config(bg="green")
                #time.sleep(0.5)
                botonesNorte[pisoActual-1].config(bg=coloresAscN)
        elif irA < pisoActual and irA >= 1:
            while pisoActual > irA:
                pisoActual -= 1
                botonesNorte[pisoActual].config(bg="green")
                botonesNorte[pisoActual+1].config(bg=coloresAscN)
                time.sleep(0.1)


        pisoNorte = pisoActual
        return pisoNorte
        

ascen = Ascensor()

botonesNorte = []
botonesSur = []

vnta = Tk()
vnta.geometry("600x800")
vnta.title("Paz y bien Jugadores...")
#vnta.config(bg="#D0DDCE")
vnta.maxsize(width=600, height=800)

colorAscN = "#C7F9F4"
colorAscS = "#86EFFB"
coloresAscN = "#F8D8F9"
coloresAscS = "#B3E6F9"

pisoNorte = ascen.ascensorNorte()
pisoSur = ascen.ascensorSur()

btnAscNorte = Button(vnta, text="Ascensor Norte",width=15, height=2,font=("Arial",12,"bold"), bg=colorAscN, command=ascen.moverAscensorNorte)
btnAscNorte.place(x=60, y=600)
btnAscNorte.config(state="disabled")

botonesNorte.append(btnAscNorte)

btnAscSur = Button(vnta, text="Ascensor Sur",width=15, height=2,font=("Arial",12,"bold"), bg=colorAscS)
btnAscSur.place(x=370, y=600)
btnAscSur.config(state="disabled")

botonesSur.append(btnAscSur)

boton0 = Button(vnta, text="INICIO",width=15, height=3,font=("Arial",12,"bold"), command = ascen.llamarAscensor)
boton0.place(x=215, y=670)

btnAscN1 = Button(vnta, text="1",width=15, height=2,font=("Arial",12,"bold"), bg=coloresAscN)
btnAscN1.place(x=60, y=500)

botonesNorte.append(btnAscN1)


btnAscN2 = Button(vnta, text="2",width=15, height=2,font=("Arial",12,"bold"), bg=coloresAscN)
btnAscN2.place(x=60, y=450)
botonesNorte.append(btnAscN2)

btnAscN3 = Button(vnta, text="3",width=15, height=2,font=("Arial",12,"bold"), bg=coloresAscN)
btnAscN3.place(x=60, y=400)
botonesNorte.append(btnAscN3)

btnAscN4 = Button(vnta, text="4",width=15, height=2,font=("Arial",12,"bold"), bg=coloresAscN)
btnAscN4.place(x=60, y=350)
botonesNorte.append(btnAscN4)

btnAscN5 = Button(vnta, text="5",width=15, height=2,font=("Arial",12,"bold"), bg=coloresAscN)
btnAscN5.place(x=60, y=300)
botonesNorte.append(btnAscN5)

btnAscN6 = Button(vnta, text="6",width=15, height=2,font=("Arial",12,"bold"), bg=coloresAscN)
btnAscN6.place(x=60, y=250)
botonesNorte.append(btnAscN6)

btnAscN7 = Button(vnta, text="7",width=15, height=2,font=("Arial",12,"bold"), bg=coloresAscN)
btnAscN7.place(x=60, y=200)
botonesNorte.append(btnAscN7)

btnAscN8 = Button(vnta, text="8",width=15, height=2,font=("Arial",12,"bold"), bg=coloresAscN)
btnAscN8.place(x=60, y=150)
botonesNorte.append(btnAscN8)

btnAscN9 = Button(vnta, text="9",width=15, height=2,font=("Arial",12,"bold"), bg=coloresAscN)
btnAscN9.place(x=60, y=100)
botonesNorte.append(btnAscN9)

btnAscN10 = Button(vnta, text="10",width=15, height=2,font=("Arial",12,"bold"), bg=coloresAscN)
btnAscN10.place(x=60, y=50)
botonesNorte.append(btnAscN10)

btnAscS1 = Button(vnta, text="1",width=15, height=2,font=("Arial",12,"bold"), bg=coloresAscS)
btnAscS1.place(x=370, y=500)
botonesSur.append(btnAscS1)

btnAscS2 = Button(vnta, text="2",width=15, height=2,font=("Arial",12,"bold"), bg=coloresAscS)
btnAscS2.place(x=370, y=450)
botonesSur.append(btnAscS2)

btnAscS3 = Button(vnta, text="3",width=15, height=2,font=("Arial",12,"bold"), bg=coloresAscS)
btnAscS3.place(x=370, y=400)
botonesSur.append(btnAscS3)

btnAscS4 = Button(vnta, text="4",width=15, height=2,font=("Arial",12,"bold"), bg=coloresAscS)
btnAscS4.place(x=370, y=350)
botonesSur.append(btnAscS4)

btnAscS5 = Button(vnta, text="5",width=15, height=2,font=("Arial",12,"bold"), bg=coloresAscS)
btnAscS5.place(x=370, y=300)
botonesSur.append(btnAscS5)

btnAscS6 = Button(vnta, text="6",width=15, height=2,font=("Arial",12,"bold"), bg=coloresAscS)
btnAscS6.place(x=370, y=250)
botonesSur.append(btnAscS6)

btnAscS7 = Button(vnta, text="7",width=15, height=2,font=("Arial",12,"bold"), bg=coloresAscS)
btnAscS7.place(x=370, y=200)
botonesSur.append(btnAscS7)

btnAscS8 = Button(vnta, text="8",width=15, height=2,font=("Arial",12,"bold"), bg=coloresAscS)
btnAscS8.place(x=370, y=150)
botonesSur.append(btnAscS8)

btnAscS9 = Button(vnta, text="9",width=15, height=2,font=("Arial",12,"bold"), bg=coloresAscS)
btnAscS9.place(x=370, y=100)
botonesSur.append(btnAscS9)

btnAscS10 = Button(vnta, text="10",width=15, height=2,font=("Arial",12,"bold"), bg=coloresAscS)
btnAscS10.place(x=370, y=50)
botonesSur.append(btnAscS10)

botonesNorte[pisoNorte].config(bg="green")
botonesSur[pisoSur].config(bg="green")

Label(vnta,text="""Realizado por Laura Juliana Serrano García - MaKeajse 2022.
Recuerda: 'Hacer de lo Ordinario, algo Extraordinario'.
""",font=("Arial",10 , "italic"), fg="black", justify="right").pack(side="bottom")

vnta.mainloop()