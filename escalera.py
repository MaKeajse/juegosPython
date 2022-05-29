import colorsys
from tkinter import *
import tkinter
from tkinter import messagebox
from tkinter import simpledialog
import random as ra
from turtle import pos


def iniciarP():
    global player1, player2, turno

    reiniciarJuego()

    try:
        player1 = simpledialog.askstring("Jugador 1","Escriba el nombre del jugador 1: ").upper()
        if player1 == "":
            player1 = "JUGADOR 1"
        
        player2 = simpledialog.askstring("Jugador 2","Escriba el nombre del jugador 2: ").upper()
        if player2 =="":
            player2 = "JUGADOR 2"
        
    except Exception as ex:
        messagebox.showinfo("FIN", "FIN DEL JUEGO")   
    
    shiftPlayer.set(player1)
    turno = 0
    botones[0].config(bg="#B06CE8", text="""INICIO
    😁😼""")

def tirarDados():
    #messagebox.showinfo("Paz y bien...", player1)

    global player1, player2, turno, posicionFinJug1, posicionFinJug2, posibleJug1,posibleJug2
    global colorSube, colorBaja, turnoJug1, turnoJug2, empate, base, inicio, meta
    
    if turno==0:
        #messagebox.showinfo("Posicion", posicionFinJug1)

        if posicionFinJug1 == 3 or posicionFinJug1 == 9 or posicionFinJug1 == 14 or posicionFinJug1 == 18 or posicionFinJug1 == 19:
            botones[posicionFinJug1].config(bg=colorSube, text=f"{posicionFinJug1} 🪜")
        elif posicionFinJug1 == 11 or posicionFinJug1 == 16 or posicionFinJug1 == 23 or posicionFinJug1 == 27 or posicionFinJug1 == 30:
            botones[posicionFinJug1].config(bg=colorBaja, text=f"{posicionFinJug1} 📏")
        elif posicionFinJug1 == 0:
            botones[posicionFinJug1].config(bg=inicio, text="INICIO 😼")            
        else:
            botones[posicionFinJug1].config(bg=base, text=f"{posicionFinJug1}")
        
        if posicionFinJug2 == 0:
            botones[posicionFinJug2].config(bg=inicio, text="INICIO 😼")            
        else:
            botones[posicionFinJug2].config(bg=turnoJug2, text=f"{posicionFinJug2} 😼")
        

        dados1 = ra.randint(1,6)
        messagebox.showinfo("Dados", dados1)
        posibleJug1 = posicionFinJug1 + dados1
        

        if posibleJug1 > 31:
            posicionFinJug1 = posicionFinJug1
            messagebox.showinfo("CONTINUA", posicionFinJug1)
            botones[posicionFinJug1].config(bg=turnoJug1, text=f"{posicionFinJug1} 😁")
        else:
            posicionFinJug1 = posicionFinJug1 + dados1

            if posicionFinJug1  == 3:
                posicionFinJug1 = 11
                messagebox.showinfo("SUBE!", posicionFinJug1)
            elif posicionFinJug1 == 9:
                posicionFinJug1 = 23
                messagebox.showinfo("SUBE!", posicionFinJug1)
            elif posicionFinJug1 == 14:
                posicionFinJug1 = 16
                messagebox.showinfo("SUBE!", posicionFinJug1)
            elif posicionFinJug1 == 18:
                posicionFinJug1 = 30
                messagebox.showinfo("SUBE!", posicionFinJug1)
            elif posicionFinJug1 == 19:
                posicionFinJug1 = 27
                messagebox.showinfo("SUBE!", posicionFinJug1)

            elif posicionFinJug1 == 11:
                posicionFinJug1 = 3
                messagebox.showinfo("BAJA!", posicionFinJug1)
            elif posicionFinJug1 == 23:
                posicionFinJug1 = 9
                messagebox.showinfo("BAJA!", posicionFinJug1)
            elif posicionFinJug1 == 16:
                posicionFinJug1 = 14
                messagebox.showinfo("BAJA!", posicionFinJug1)
            elif posicionFinJug1 == 30:
                posicionFinJug1 = 18
                messagebox.showinfo("BAJA!", posicionFinJug1)
            elif posicionFinJug1 == 27:
                posicionFinJug1 = 19
                messagebox.showinfo("BAJA!", posicionFinJug1)
            else:
                posicionFinJug1    

            if posicionFinJug1 == posicionFinJug2:
                botones[posicionFinJug1].config(bg=empate, text=f"{posicionFinJug1} 😁😼")
            else:
                botones[posicionFinJug1].config(bg=turnoJug1, text=f"{posicionFinJug1} 😁")


        if posicionFinJug1 == 31:
            messagebox.showinfo("GANADOR","¡¡¡FELICITACIONES " + player1 + " HAS GANADOR")
            bloquearTirarDados()

        
        turno = 1
        shiftPlayer.set(player2)
    
    elif turno==1:
        #messagebox.showinfo("Posicion", posicionFinJug2)

        if posicionFinJug2 == 3 or posicionFinJug2 == 9 or posicionFinJug2 == 14 or posicionFinJug2 == 18 or posicionFinJug2 == 19:
            botones[posicionFinJug2].config(bg=colorSube, text=f"{posicionFinJug2} 🪜")
        elif posicionFinJug2 == 11 or posicionFinJug2 == 16 or posicionFinJug2 == 23 or posicionFinJug2 == 27 or posicionFinJug2 == 30:
            botones[posicionFinJug2].config(bg=colorBaja, text=f"{posicionFinJug2} 📏")
        elif posicionFinJug2 == 0:
            botones[posicionFinJug2].config(bg=inicio, text="INICIO")            
        else:
            botones[posicionFinJug2].config(bg=base, text=f"{posicionFinJug2}")

        if posicionFinJug1 == 0:
            botones[posicionFinJug1].config(bg=inicio, text="INICIO 😁")            
        else:
            botones[posicionFinJug1].config(bg=turnoJug1, text=f"{posicionFinJug1} 😁")
        


        dados2 = ra.randint(1,6)
        messagebox.showinfo("Dados", dados2)
        posibleJug2 = posicionFinJug2 + dados2

        if posibleJug2 > 31:
            posicionFinJug2 = posicionFinJug2
            messagebox.showinfo("CONTINUA", posicionFinJug2)
            botones[posicionFinJug2].config(bg=turnoJug2, text=f"{posicionFinJug2} 😼")
        else:
            posicionFinJug2 = posicionFinJug2 + dados2

            if posicionFinJug2  == 3:
                posicionFinJug2 = 11
                messagebox.showinfo("SUBE!", posicionFinJug2)
            elif posicionFinJug2 == 9:
                posicionFinJug2 = 23
                messagebox.showinfo("SUBE!", posicionFinJug2)
            elif posicionFinJug2 == 14:
                posicionFinJug2 = 16
                messagebox.showinfo("SUBE!", posicionFinJug2)
            elif posicionFinJug2 == 18:
                posicionFinJug2 = 30
                messagebox.showinfo("SUBE!", posicionFinJug2)
            elif posicionFinJug2 == 19:
                posicionFinJug2 = 27
                messagebox.showinfo("SUBE!", posicionFinJug2)

            elif posicionFinJug2 == 11:
                posicionFinJug2 = 3
                messagebox.showinfo("BAJA!", posicionFinJug2)
            elif posicionFinJug2 == 23:
                posicionFinJug1 = 9
                messagebox.showinfo("BAJA!", posicionFinJug2)
            elif posicionFinJug2 == 16:
                posicionFinJug2 = 14
                messagebox.showinfo("BAJA!", posicionFinJug2)
            elif posicionFinJug2 == 30:
                posicionFinJug2 = 18
                messagebox.showinfo("BAJA!", posicionFinJug2)
            elif posicionFinJug2 == 27:
                posicionFinJug2 = 19
                messagebox.showinfo("BAJA!", posicionFinJug2)
            else:
                posicionFinJug2

            if posicionFinJug2 == posicionFinJug1:
                botones[posicionFinJug2].config(bg=empate, text=f"{posicionFinJug2} 😁😼")
            else:
                botones[posicionFinJug2].config(bg=turnoJug2, text=f"{posicionFinJug2} 😼")

        if posicionFinJug2 == 31:
            messagebox.showinfo("GANADOR","¡¡¡FELICITACIONES " + player2 + " HAS GANADOR")
            bloquearTirarDados()
        
        turno = 0
        shiftPlayer.set(player1)

    return posicionFinJug2, posicionFinJug1


def bloquearTirarDados():
    continuar.config(state="disable")

def reiniciarJuego():
    for i in range(0,32):
        if i == 3 or i == 9 or i == 14 or i == 18 or i == 19:
            botones[i].config(bg=colorSube, text=f"{i} 🪜")
        elif i == 11 or i == 16 or i == 23 or i == 27 or i == 30:
            botones[i].config(bg=colorBaja, text=f"{i} 📏")
        elif i == 0:
            botones[i].config(bg=inicio, text="INICIO")
        elif i == 31:
            botones[i].config(bg=meta, text=" 🥅 META 🥅")            
        else:
            botones[i].config(bg=base, text=f"{i}")
    
    
vnta = Tk()
vnta.geometry("800x600")
vnta.title("Paz y bien Jugadores...")
#vnta.config(bg="#D0DDCE")
vnta.maxsize(width=800, height=600)



player1 = ""
player2 = ""
botones = []
posicionFinJug2 = 0
posicionFinJug1 = 0
posibleJug2 = 0
posicionJug1 = 0

colorSube= "#7EF770"
colorBaja= "#F84274"
turnoJug1 = "#42C1F8"
turnoJug2 = "#D180F5"
empate = "#6CE8AC"
base = "#B5F3EF"
inicio = "#B06CE8"
meta = "#2E9CF3"

shiftPlayer = StringVar()
varBtn1 = StringVar()

turno = Label(vnta, text="TURNO: ", font=("Arial", 14)).place(x=400, y=30)

turnoTxt = Label(vnta, textvariable=shiftPlayer, font=("Arial",14,"bold"), bg="#D0DDCE").place(x=480, y=30)

imag = tkinter.PhotoImage(file="./img/meta.png")
titulo = Label(vnta, text="JUEGO DE LA ESCALERA", font=("Arial", 14, "bold"), fg="red").place(x=15, y=30)

boton0 = Button(vnta, text="INICIO",width=8, height=4,font=("Arial",12,"bold"), bg=inicio)
boton0.place(x=40, y=350)

botones.append(boton0)

boton1 = Button(vnta, text="1",width=8, height=4,font=("Arial",12,"bold"), bg=base)
boton1.place(x=130, y=350)

botones.append(boton1)

boton2 = Button(vnta, text="2",width=8, height=4,font=("Arial",12,"bold"), bg=base)
boton2.place(x=220, y=350)

botones.append(boton2)

boton3 = Button(vnta, text="3 🪜",width=8, height=4,font=("Arial",12,"bold"), bg=colorSube)
boton3.place(x=310, y=350)

botones.append(boton3)

boton4 = Button(vnta, text="4",width=8, height=4,font=("Arial",12,"bold"), bg=base)
boton4.place(x=400, y=350)

botones.append(boton4)

boton5 = Button(vnta, text="5",width=8, height=4,font=("Arial",12,"bold"), bg=base)
boton5.place(x=490, y=350)

botones.append(boton5)

boton6= Button(vnta, text="6",width=8, height=4,font=("Arial",12,"bold"), bg=base)
boton6.place(x=580, y=350)

botones.append(boton6)

boton7 = Button(vnta, text="7",width=8, height=4,font=("Arial",12,"bold"), bg=base)
boton7.place(x=670, y=350)

botones.append(boton7)



# Segunda línea
boton8 = Button(vnta, text="8",width=8, height=4,font=("Arial",12,"bold"), bg=base)
boton8.place(x=670, y=260)
botones.append(boton8)

boton9 = Button(vnta, text="9 🪜",width=8, height=4,font=("Arial",12,"bold"), bg=colorSube)
boton9.place(x=580, y=260)
botones.append(boton9)

boton10 = Button(vnta, text="10",width=8, height=4,font=("Arial",12,"bold"), bg=base)
boton10.place(x=490, y=260)
botones.append(boton10)

boton11 = Button(vnta, text="11 📏",width=8, height=4,font=("Arial",12,"bold"), bg=colorBaja)
boton11.place(x=400, y=260)
botones.append(boton11)

boton12 = Button(vnta, text="12",width=8, height=4,font=("Arial",12,"bold"), bg=base)
boton12.place(x=310, y=260)
botones.append(boton12)

boton13 = Button(vnta, text="13",width=8, height=4,font=("Arial",12,"bold"), bg=base)
boton13.place(x=220, y=260)
botones.append(boton13)

boton14 = Button(vnta, text="14 🪜",width=8, height=4,font=("Arial",12,"bold"), bg=colorSube)
boton14.place(x=130, y=260)
botones.append(boton14)

boton15 = Button(vnta, text="15",width=8, height=4,font=("Arial",12,"bold"), bg=base)
boton15.place(x=40, y=260)
botones.append(boton15)


#Tercera línea
boton16 = Button(vnta, text="16 📏",width=8, height=4,font=("Arial",12,"bold"), bg=colorBaja)
boton16.place(x=40, y=170)

botones.append(boton16)

boton17 = Button(vnta, text="17",width=8, height=4,font=("Arial",12,"bold"), bg=base)
boton17.place(x=130, y=170)

botones.append(boton17)

boton18 = Button(vnta, text="18 🪜",width=8, height=4,font=("Arial",12,"bold"), bg=colorSube)
boton18.place(x=220, y=170)

botones.append(boton18)

boton19 = Button(vnta, text="19 🪜",width=8, height=4,font=("Arial",12,"bold"), bg=colorSube)
boton19.place(x=310, y=170)

botones.append(boton19)

boton20 = Button(vnta, text="20",width=8, height=4,font=("Arial",12,"bold"), bg=base)
boton20.place(x=400, y=170)

botones.append(boton20)

boton21 = Button(vnta, text="21",width=8, height=4,font=("Arial",12,"bold"), bg=base)
boton21.place(x=490, y=170)

botones.append(boton21)

boton22 = Button(vnta, text="22",width=8, height=4,font=("Arial",12,"bold"), bg=base)
boton22.place(x=580, y=170)

botones.append(boton22)

boton23 = Button(vnta, text="23 📏",width=8, height=4,font=("Arial",12,"bold"), bg=colorBaja)
boton23.place(x=670, y=170)

botones.append(boton23)

#Cuarta línea
boton24 = Button(vnta, text="24",width=8, height=4,font=("Arial",12,"bold"), bg=base)
boton24.place(x=670, y=80)
botones.append(boton24)

boton25 = Button(vnta, text="25",width=8, height=4,font=("Arial",12,"bold"), bg=base)
boton25.place(x=580, y=80)
botones.append(boton25)

boton26 = Button(vnta, text="26",width=8, height=4,font=("Arial",12,"bold"), bg=base)
boton26.place(x=490, y=80)
botones.append(boton26)

boton27 = Button(vnta, text="27 📏",width=8, height=4,font=("Arial",12,"bold"), bg=colorBaja)
boton27.place(x=400, y=80)
botones.append(boton27)

boton28 = Button(vnta, text="28",width=8, height=4,font=("Arial",12,"bold"), bg=base)
boton28.place(x=310, y=80)
botones.append(boton28)

boton29 = Button(vnta, text="29",width=8, height=4,font=("Arial",12,"bold"), bg=base)
boton29.place(x=220, y=80)
botones.append(boton29)

boton30 = Button(vnta, text="30 📏",width=8, height=4,font=("Arial",12,"bold"), bg=colorBaja)
boton30.place(x=130, y=80)
botones.append(boton30)

boton31 = Button(vnta, text=" 🥅 META 🥅",width=8, height=4,font=("Arial",12,"bold"), bg=meta)
boton31.place(x=40, y=80)
botones.append(boton31)

iniciar = Button(vnta, text="Iniciar juego",width=10, height=2,font=("Arial",12,"bold"), command= iniciarP)
iniciar.config(bg="#F9614C", fg="white")
iniciar.place(x=250,y=460)

continuar = Button(vnta, text="Tirar los dados 🎲",width=20, height=2,font=("Arial",12,"bold"), command=tirarDados)
continuar.config(bg="#F94C95", fg="white")
continuar.place(x=380,y=460)


Label(vnta,text="""Realizado por Laura Juliana Serrano García - MaKeajse 2022.
Recuerda: 'Hacer de lo Ordinario, algo Extraordinario'.
""",font=("Arial",10 , "italic"), fg="black", justify="right").pack(side="bottom")


vnta.mainloop()