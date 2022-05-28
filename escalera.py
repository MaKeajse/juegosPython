from tkinter import *

vnta = Tk()
vnta.geometry("800x580")
vnta.title("Paz y bien Jugadores...")
#vnta.config(bg="#D0DDCE")
vnta.maxsize(width=800, height=580)

turno = 0
player1 = ""
player2 = ""
botones = []

boton0 = Button(vnta, text="Meta",width=8, height=4,font=("Arial",12,"bold"))
boton0.place(x=10, y=80)

botones.append(boton0)

boton1 = Button(vnta, text="30",width=8, height=4,font=("Arial",12,"bold"))
boton1.place(x=100, y=80)

botones.append(boton1)

boton2 = Button(vnta, text="29",width=8, height=4,font=("Arial",12,"bold"))
boton2.place(x=190, y=80)

botones.append(boton2)

boton3 = Button(vnta, text="28",width=8, height=4,font=("Arial",12,"bold"))
boton3.place(x=280, y=80)

botones.append(boton3)

boton4 = Button(vnta, text="27",width=8, height=4,font=("Arial",12,"bold"))
boton4.place(x=370, y=80)

botones.append(boton4)

boton5 = Button(vnta, text="26",width=8, height=4,font=("Arial",12,"bold"))
boton5.place(x=460, y=80)

botones.append(boton5)

boton6 = Button(vnta, text="25",width=8, height=4,font=("Arial",12,"bold"))
boton6.place(x=550, y=80)

botones.append(boton6)

boton7 = Button(vnta, text="24",width=8, height=4,font=("Arial",12,"bold"))
boton7.place(x=640, y=80)

botones.append(boton7)

# Segunda línea
boton8 = Button(vnta, text="16",width=8, height=4,font=("Arial",12,"bold"))
boton8.place(x=10, y=170)

botones.append(boton8)

boton9 = Button(vnta, text="17",width=8, height=4,font=("Arial",12,"bold"))
boton9.place(x=100, y=170)

botones.append(boton9)

boton10 = Button(vnta, text="18",width=8, height=4,font=("Arial",12,"bold"))
boton10.place(x=190, y=170)

botones.append(boton10)

boton11 = Button(vnta, text="19",width=8, height=4,font=("Arial",12,"bold"))
boton11.place(x=280, y=170)

botones.append(boton11)

boton12 = Button(vnta, text="20",width=8, height=4,font=("Arial",12,"bold"))
boton12.place(x=370, y=170)

botones.append(boton12)

boton13 = Button(vnta, text="21",width=8, height=4,font=("Arial",12,"bold"))
boton13.place(x=460, y=170)

botones.append(boton13)

boton14 = Button(vnta, text="22",width=8, height=4,font=("Arial",12,"bold"))
boton14.place(x=550, y=170)

botones.append(boton14)

boton15 = Button(vnta, text="23",width=8, height=4,font=("Arial",12,"bold"))
boton15.place(x=640, y=170)

botones.append(boton15)

#Tercera línea
boton16 = Button(vnta, text="15",width=8, height=4,font=("Arial",12,"bold"))
boton16.place(x=10, y=260)

botones.append(boton16)

boton17 = Button(vnta, text="14",width=8, height=4,font=("Arial",12,"bold"))
boton17.place(x=100, y=260)

botones.append(boton17)

boton18 = Button(vnta, text="13",width=8, height=4,font=("Arial",12,"bold"))
boton18.place(x=190, y=260)

botones.append(boton18)

boton19 = Button(vnta, text="12",width=8, height=4,font=("Arial",12,"bold"))
boton19.place(x=280, y=260)

botones.append(boton19)

boton20 = Button(vnta, text="11",width=8, height=4,font=("Arial",12,"bold"))
boton20.place(x=370, y=260)

botones.append(boton20)

boton21 = Button(vnta, text="10",width=8, height=4,font=("Arial",12,"bold"))
boton21.place(x=460, y=260)

botones.append(boton21)

boton22 = Button(vnta, text="9",width=8, height=4,font=("Arial",12,"bold"))
boton22.place(x=550, y=260)

botones.append(boton22)

boton23 = Button(vnta, text="8",width=8, height=4,font=("Arial",12,"bold"))
boton23.place(x=640, y=260)

botones.append(boton23)

#Cuarta línea
boton24 = Button(vnta, text="Inicio",width=8, height=4,font=("Arial",12,"bold"))
boton24.place(x=10, y=350)

botones.append(boton24)

boton25 = Button(vnta, text="1",width=8, height=4,font=("Arial",12,"bold"))
boton25.place(x=100, y=350)

botones.append(boton25)

boton26 = Button(vnta, text="2",width=8, height=4,font=("Arial",12,"bold"))
boton26.place(x=190, y=350)

botones.append(boton26)

boton27 = Button(vnta, text="3",width=8, height=4,font=("Arial",12,"bold"))
boton27.place(x=280, y=350)

botones.append(boton27)

boton28 = Button(vnta, text="4",width=8, height=4,font=("Arial",12,"bold"))
boton28.place(x=370, y=350)

botones.append(boton28)

boton29 = Button(vnta, text="5",width=8, height=4,font=("Arial",12,"bold"))
boton29.place(x=460, y=350)

botones.append(boton29)

boton30 = Button(vnta, text="6",width=8, height=4,font=("Arial",12,"bold"))
boton30.place(x=550, y=350)

botones.append(boton30)

boton31 = Button(vnta, text="7",width=8, height=4,font=("Arial",12,"bold"))
boton31.place(x=640, y=350)

botones.append(boton31)


vnta.mainloop()