import tkinter

ventana =tkinter.Tk() #contenedor de graficos
ventana.geometry("400x400")

etiqueta = tkinter.Label(ventana, text="Hola Mundo",bg="green")
etiqueta.pack(fill=tkinter.X) # Colocar el label en pantalla

cajaNumero1 = tkinter.Entry(ventana, font="Helveltica 20")
cajaNumero1.pack()
cajaNumero2 = tkinter.Entry(ventana, font="Helveltica 20")
cajaNumero2.pack()

def numerosDeLaCaja():
    numero1 = int(cajaNumero1.get())
    numero2 = int(cajaNumero2.get())
    resultMultiplicacion = numero1*numero2
    etiquetaResult["text"]="El resultado de la multiplicacion es :",resultMultiplicacion
#def saludo(num1,num2):
 #   print("Hola Programadores")
  #  print(num1*num2)

boton = tkinter.Button(ventana,text="Multiplicar", command= numerosDeLaCaja)
boton.pack()

etiquetaResult = tkinter.Label(ventana,text="",bg="blue",font="Helveltica 20")
etiquetaResult.pack(fill=tkinter.X)

ventana.mainloop()