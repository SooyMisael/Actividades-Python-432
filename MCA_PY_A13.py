import tkinter as tk
from tkinter import messagebox

def Suma():
    num1 = int(ent_caja.get())
    num2 = int(ent_caja1.get())
    Resultado = str(num1 + num2)
    ent_caja2["text"]=Resultado
def Resta():
    num1 = int(ent_caja.get())
    num2 = int(ent_caja1.get())
    Resultado = str(num1 - num2)
    ent_caja2["text"]=Resultado

def Multi():
    num1 = int(ent_caja.get())
    num2 = int(ent_caja1.get())
    Resultado = str(num1 * num2)
    ent_caja2["text"]=Resultado

def Division():
    num1 = int(ent_caja.get())
    num2 = int(ent_caja1.get())
    Resultado = str(num1 / num2)
    ent_caja2["text"]=Resultado

    

root=tk.Tk()
cadena = tk.StringVar()
root.title("Calculadora Basica Python")
root.geometry("516x378")
root.resizable(width=False, height=False)



lbl_msge = tk.Label(root, text="CALCULADORA BASICA", font=("Comic Sans MS",20))
lbl_msge.place(x=115,y=122)

lbl_num1 = tk.Label(root, text="Numero 1", font=("Comic Sans MS",10))
lbl_num1.place(x=145,y=191)

lbl_num2 = tk.Label(root,text="Numero 2", font=("Comic Sans MS",10))
lbl_num2.place(x=239,y=191)

lbl_resu = tk.Label(root,text="Resultado", font=("Comic Sans MS",10))
lbl_resu.place(x=336,y=191)

ent_caja = tk.Entry(root)
ent_caja.place(x=132,y=217, width="79",height="27")

ent_caja1 = tk.Entry(root)
ent_caja1.place(x=227,y=218, width="79",height="27")

ent_caja2 = tk.Label(root, background="White")
ent_caja2.place(x=324,y=219, width=79, height="27")

btn_suma = tk.Button(root,text="Suma", font=("Comic Sans MS",10), command=Suma)
btn_suma.place(x=107,y=282, width=62,height=27)

btn_resta = tk.Button(root,text="Resta", font=("Comic Sans MS",10), command=Resta)
btn_resta.place(x=185, y=282,width=64,height=27)

btn_multi = tk.Button(root, text="Multiplicacion", font=("Comic Sans MS",9), command=Multi)
btn_multi.place(x=265, y=282,width=85,height=27)

btn_div = tk.Button(root, text="Division", font=("Comic Sans MS",10), command=Division)
btn_div.place(x=367, y=282,width=61,height=27)

root.mainloop()