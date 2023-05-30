import tkinter
import random
#Camila Pérez 20221107043
#Angela Malagon 20221107081

def encriptado_con_intercepto():
    n = int(entrada_1.get())
    ejes = []
    clave = []

    for _ in range(n):
        ejes.append(random.randint(1, 2))
    for _ in range(n):
        clave.append(random.randint(0, 1))

    ejes_letras = ['x' if i == 2 else 'y' for i in ejes]

    clave_interceptada = [random.randint(0, 1) for _ in range(n)]

    ventana_resultado = tkinter.Toplevel()
    ventana_resultado.title("Encriptado cuántico con intercepto")

    label1 = tkinter.Label(ventana_resultado, text="La longitud del mensaje es: " + str(n))
    label1.pack()
    label2 = tkinter.Label(ventana_resultado, text="La clave original es:")
    label2.pack()
    label3 = tkinter.Label(ventana_resultado, text=clave)
    label3.pack()
    label4 = tkinter.Label(ventana_resultado, text="La clave interceptada es:")
    label4.pack()
    label5 = tkinter.Label(ventana_resultado, text=clave_interceptada)
    label5.pack()

def encriptado_sin_intercepto():
    n = int(entrada_1.get())
    ejes = []
    clave = []

    for _ in range(n):
        ejes.append(random.randint(1, 2))
    for _ in range(n):
        clave.append(random.randint(0, 1))

    ejes_letras = ['x' if i == 2 else 'y' for i in ejes]
    #ejes_letras = []
    #for i in ejes:
        #if i == 2:
            #'x'
        #else:
            #'y'
       
    clave_1 = [random.randint(0, 1) if ejes_letras[i] != ejes[i] else clave[i] for i in range(n)]
    clave_final = clave
    ventana_resultado = tkinter.Toplevel()
    ventana_resultado.title("Encriptado cuántico sin intercepto")


    clave_final_2 = [clave_final[i] for i in range(n) if ejes_letras[i] == ejes[i]]
    datos_desechados = [clave_1[i] for i in range(n) if ejes_letras[i] != ejes[i]]

    label1 = tkinter.Label(ventana_resultado, text="La longitud del mensaje es: " + str(n))
    label1.pack()
    label2 = tkinter.Label(ventana_resultado, text="Los ejes en los que se enviaron los datos fueron:")
    label2.pack()
    label3 = tkinter.Label(ventana_resultado, text=ejes_letras)
    label3.pack()
    label4 = tkinter.Label(ventana_resultado, text="La clave original es:")
    label4.pack()
    label5 = tkinter.Label(ventana_resultado, text=clave)
    label5.pack()
    label6 = tkinter.Label(ventana_resultado, text="Tus ejes de medición fueron:")
    label6.pack()
    label7 = tkinter.Label(ventana_resultado, text=ejes_letras)
    label7.pack()
    label8 = tkinter.Label(ventana_resultado, text="Y tus datos medidos fueron:")
    label8.pack()
    label9 = tkinter.Label(ventana_resultado, text=clave_1)
    label9.pack()
    label10 = tkinter.Label(ventana_resultado, text="Valores de los ejes en letras y números:")
    label10.pack()
    label11 = tkinter.Label(ventana_resultado, text=ejes_letras)
    label11.pack()
    label12 = tkinter.Label(ventana_resultado, text=ejes)
    label12.pack()
    label13 = tkinter.Label(ventana_resultado, text="La clave final es:")
    label13.pack()
    label14 = tkinter.Label(ventana_resultado, text=clave_final)
    label14.pack()
    label15 = tkinter.Label(ventana_resultado, text="Los datos desechados son:")
    label15.pack()
    label16 = tkinter.Label(ventana_resultado, text=datos_desechados)
    label16.pack()


ventana = tkinter.Tk()
ventana.title("Encriptado cuántico")

label_entrada1 = tkinter.Label(ventana, text="Longitud del mensaje:")
label_entrada1.pack()

entrada_1 = tkinter.Entry(ventana)
entrada_1.pack()

btn_con_intercepto = tkinter.Button(ventana, text="Encriptado con intercepto", command=encriptado_con_intercepto)
btn_con_intercepto.pack()

btn_sin_intercepto = tkinter.Button(ventana, text="Encriptado sin intercepto", command=encriptado_sin_intercepto)
btn_sin_intercepto.pack()

ventana.mainloop()
