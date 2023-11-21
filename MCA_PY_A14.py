#Importaciones
import tkinter as tk
import math

#Creacion de ventana
root = tk.Tk()

#Configuracion de la ventana
root.title("Calculadora de Escritorio")
root.geometry("362x471")

i = 0
#Entrada
ent_caja1 = tk.Entry(root,font=("Comic Sans MS",10))
ent_caja1.place(x=30,y=76, width="304",height="29")

#funciones
def click(valor):
    global i
    ent_caja1.insert(i, valor)
    i += 1

def MC():
    ent_caja1.delete("0","end")
    i=0

def Igual():
    ecuacion = ent_caja1.get()
    resultado = eval(ecuacion)
    ent_caja1.delete("0","end")
    ent_caja1.insert(0,resultado)
    i=0

def Raiz():
    resultado = math.sqrt(float(ent_caja1.get()))
    ent_caja1.insert(0,resultado)
    i=0

def UnoEntre():
    entrada = float(ent_caja1.get())
    ecuacion = (1/(entrada))
    ent_caja1.delete("0", "end")
    ent_caja1.insert(0,ecuacion)
    i=0

def EmeMas():
    acumulador = 0
    entrada = float(ent_caja1.get())
    acumulador = float(acumulador + entrada)
    ent_caja1.delete("0","end")
    ent_caja1.insert(0,acumulador)

#botones Especiales
botonMC = tk.Button(root,text="MC",font=("Comic Sans MS",10),command=lambda:MC())
botonMC.place(x=10,y=127,width="61",height="50")

botonMR = tk.Button(root,text="MR",font=("Comic Sans MS",10))
botonMR.place(x=79,y=127,width="61",height="50")

botonMS = tk.Button(root,text="MS",font=("Comic Sans MS",10))
botonMS.place(x=150,y=127,width="61",height="50")

botonM = tk.Button(root,text="M+",font=("Comic Sans MS",10), command=lambda:EmeMas())
botonM.place(x=219,y=127,width="61",height="50")

botonSQR = tk.Button(root,text="SQRT",font=("Comic Sans MS",10),command=lambda:Raiz())
botonSQR.place(x=288,y=127,width="61",height="50")

#Botones de operadores
boton_div = tk.Button(root,text="/",font=("Comic Sans MS",10), command=lambda:click("/"))
boton_div.place(x=219,y=186,width="61",height="50")

boton_sum = tk.Button(root,text="+", font=("Comic Sans MS",10), command=lambda:click("+"))
boton_sum.place(x=219,y=363,width="61",height="50")

boton_res = tk.Button(root,text="-",font=("Comic Sans MS",10), command=lambda:click("-"))
boton_res.place(x=219,y=304,width="61",height="50")

boton_multi = tk.Button(root,text="*",font=("Comic Sans MS",10), command=lambda:click("*"))
boton_multi.place(x=219,y=245,width="61",height="50")

boton_porc = tk.Button(root,text="%",font=("Comic Sans MS",10), command=lambda:click("%"))
boton_porc.place(x=288,y=186,width="61",height="50")

boton_uno = tk.Button(root,text="1/X",font=("Comic Sans MS",10), command=lambda:UnoEntre())
boton_uno.place(x=288,y=245,width="61",height="50")

boton_igual = tk.Button(root,text="=",font=("Comic Sans MS",10), command=lambda:Igual())
boton_igual.place(x=288,y=304,width="61",height="108")

boton_punto = tk.Button(root,text=".",font=("Comic Sans MS",10), command=lambda:click("."))
boton_punto.place(x=151,y=363,width="61",height="50")

#Botones numericos
boton_1 = tk.Button(root,text="1",font=("Comic Sans MS",10),command=lambda:click(1))
boton_1.place(x=11,y=304,width="61",height="50")

boton_2 = tk.Button(root,text="2",font=("Comic Sans MS",10),command=lambda:click(2))
boton_2.place(x=80,y=304,width="61",height="50")

boton_3 = tk.Button(root,text="3",font=("Comic Sans MS",10),command=lambda:click(3))
boton_3.place(x=151,y=304,width="61",height="50")

boton_4 = tk.Button(root,text="4",font=("Comic Sans MS",10),command=lambda:click(4))
boton_4.place(x=11,y=245,width="61",height="50")

boton_5 = tk.Button(root,text="5",font=("Comic Sans MS",10),command=lambda:click(5))
boton_5.place(x=80,y=245,width="61",height="50")

boton_6 = tk.Button(root,text="6",font=("Comic Sans MS",10),command=lambda:click(6))
boton_6.place(x=151,y=245,width="61",height="50")

boton_7 = tk.Button(root,text="7",font=("Comic Sans MS",10),command=lambda:click(7))
boton_7.place(x=11,y=186,width="61",height="50")

boton_8 = tk.Button(root,text="8",font=("Comic Sans MS",10),command=lambda:click(8))
boton_8.place(x=80,y=186,width="61",height="50")

boton_9 = tk.Button(root,text="9",font=("Comic Sans MS",10),command=lambda:click(9))
boton_9.place(x=151,y=186,width="61",height="50")

boton_0 = tk.Button(root,text="0",font=("Comic Sans MS",10),command=lambda:click(0))
boton_0.place(x=11,y=363,width="130",height="50")

lblfirma = tk.Label(root, text="Creado por Misael Antonio, 2023",font=("Comic Sans MS",10))
lblfirma.place(x=153,y=450)



#Bucle del programa
root.mainloop()