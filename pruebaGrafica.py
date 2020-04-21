from tkinter import *
from arbolBinario import *

objArbol = arbolBinario()

vecDerecha = []
vecIzquierda = []

def onEnter(event):
    insertarNodo()


def insertarNodo():
    dato = txtNodo.get()

    if dato.isnumeric():

        xiDatoD = 400
        yiDatoD = 10
        xfDatoD = 450
        yfDatoD = 60
        xTextD = 425
        yTextD = 30

        xiDatoL = 400
        yiDatoL = 10
        xfDatoL = 450
        yfDatoL = 60
        xTextL = 425
        yTextL = 30

        dato = int(dato)
        listDatos.insert(END, dato)
        vec = objArbol.agregarNodo(dato)

        if len(vec) == 0:
            ## RAIZ
            c.create_oval(400, 10, 450, 60, fill=colorNodo)
            c.create_text(425, 30, text=dato, font=("Bahnschrift Light Condensed", 18), fill=colorTexto)
            ##c.create_line(425, 60, 425, 100, fill="white")
        else:
            ## DERECHA
            if vec[0] == 1:
                for i in range(len(vec)):
                    if vec[i] == 1:
                        xiDatoD += 50
                        yiDatoD += 50
                        xfDatoD += 50
                        yfDatoD += 50
                        xTextD += 50
                        yTextD += 50
                    else:
                        xiDatoD -= 50
                        yiDatoD += 50
                        xfDatoD -= 50
                        yfDatoD += 50
                        xTextD -= 50
                        yTextD += 50



                nodoDerecha = c.create_oval(xiDatoD, yiDatoD, xfDatoD, yfDatoD, fill=colorNodo)
                nodoDerechaT = c.create_text(xTextD, yTextD, text=dato, font=("Bahnschrift Light Condensed", 18), fill=colorTexto)
                ##c.create_line(xiDatoD, yiDatoD, xfDatoD, yfDatoD, fill="white")

                vecDerecha.append((nodoDerecha,nodoDerechaT))

                for i in range(len(vecDerecha)):
                    c.move(vecDerecha[i], 25, 0)

            ## IZQUIERDA
            else:
                for i in range(len(vec)):
                    if vec[i] == 0:
                        xiDatoL -= 50
                        yiDatoL += 50
                        xfDatoL -= 50
                        yfDatoL += 50
                        xTextL -= 50
                        yTextL += 50
                    else:
                        xiDatoL += 50
                        yiDatoL += 50
                        xfDatoL += 50
                        yfDatoL += 50
                        xTextL += 50
                        yTextL += 50



                nodoIzquierda = c.create_oval(xiDatoL, yiDatoL, xfDatoL, yfDatoL, fill=colorNodo)
                nodoIzquierdaT = c.create_text(xTextL, yTextL, text=dato, font=("Bahnschrift Light Condensed", 18), fill=colorTexto)
                ##c.create_line(xiDatoL, yiDatoL, xfDatoL, yfDatoL, fill="white")

                vecIzquierda.append((nodoIzquierda, nodoIzquierdaT))

                for i in range(len(vecIzquierda)):
                    c.move(vecIzquierda[i], 25, 0)

        txtNodo.delete(0, 'end')
        lblMensaje.config(text="El " + str(dato) + " ha sido insertado")
        txtNodo.focus()

    else:
        txtNodo.focus()
        lblMensaje.config(text="Dato incorrecto")
        txtNodo.delete(0, 'end')


colorVentana = "#fefce6"
colorNodo = "#0B2239"
colorTexto = "orange"

ventana = Tk()
ventana.tk.call('wm', 'resizable', ventana._w, False, False)
ventana.iconbitmap('codificacion.ico')
ventana.title(" Arbol Binario")
ventana.configure(background=colorVentana)
ventana.geometry('1100x590+150+60')

imageArbol = PhotoImage(file=("arbol.png"))
imageNube = PhotoImage(file=("nube.png"))
imageSol = PhotoImage(file=("sol.png"))

lblImageArbol = Label(ventana, bg=colorVentana, image=imageArbol)
lblImageArbol.place(x=-50, y=70)

lblImageNube = Label(ventana, bg=colorVentana, image=imageNube)
lblImageNube.place(x=400, y=0)

lblImageSol = Label(ventana, bg=colorVentana, image=imageSol)
lblImageSol.place(x=860, y=5)
lblNodo = Label(ventana, text="", font=("Bahnschrift Light Condensed", 18), fg="orange", bg=colorVentana,
                anchor="center")
lblNodo.grid(row=0, column=0)

lblNodo = Label(ventana, text=" DATO:     ", font=("Bahnschrift Light Condensed", 18), fg="orange", bg=colorVentana,
                anchor="center")
lblNodo.grid(row=1, column=0)

txtNodo = Entry(ventana, width=25, bg="#0b2239", borderwidth=2, fg="white", font=("Bahnschrift Light Condensed", 13))
txtNodo.grid(row=1, column=1)
txtNodo.focus()
txtNodo.bind('<Return>', onEnter)

lblTitulo = Label(ventana, text="ARBOL BINARIO", font=("Freestyle Script", 30), fg="#23827d", bg=colorVentana,
                  anchor="center")
lblTitulo.grid(row=1, column=2, rowspan=2, columnspan=2)

btnRegistrar = Button(ventana, text="INSERTAR", activebackground=colorVentana, bg="black", fg="white", cursor="hand2",
                      relief=GROOVE, command=insertarNodo)
btnRegistrar.grid(row=2, column=1)

lblMensaje = Label(ventana, text="", font=("Bahnschrift Light Condensed", 18), fg=colorNodo, bg=colorVentana,
                   anchor="center")
lblMensaje.grid(row=3, column=1)

listDatos = Listbox(ventana, width=3, height=5, bg="#9a795f", fg="white", font=("Bahnschrift Light Condensed", 18))
listDatos.place(x=155, y=420)

c = Canvas(ventana, width=800, height=430, bg="#2d3742")
c.grid(row=4, column=2, columnspan=2)

## SCROLL CANVAS
scroll_x = Scrollbar(ventana, orient="horizontal", command=c.xview)
scroll_x.grid(row=5, column=2, columnspan=2, sticky="ew")

scroll_y = Scrollbar(ventana, orient="vertical", command=c.yview)
scroll_y.grid(row=4, column=4, sticky="ns")

c.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

ventana.mainloop()
