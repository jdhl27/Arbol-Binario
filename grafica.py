from tkinter import *
from arbolBinario import  *

objArbol = arbolBinario()

def onEnter(event):
    insertarNodo()


def insertarNodo():
    dato = txtNodo.get()

    if dato.isnumeric():

        xi = 400
        yi = 10
        xf = 450
        yf = 60
        xText = 425
        yText = 30

        xiLineaD = 445
        yiLineaD = 50
        xfLineaD = 470
        yfLineaD = 80

        xiLineaI = 405
        yiLineaI = 50
        xfLineaI = 370
        yfLineaI = 80

        dato = int(dato)
        listDatos.insert(END, dato)
        vec = objArbol.agregarNodo(dato)

        if len(vec) == 0:
            ## CABEZA
            c.create_oval(400, 10, 450, 60, fill=colorNodo)
            c.create_text(425, 30, text=dato, font=("Bahnschrift Light Condensed", 18), fill=colorTexto)

        else:
            if len(vec) == 1:
                if vec[0] == 1:
                    ## DERECHA
                    derechaLinea = c.create_line(445, 50, 470, 80, fill="white")
                    derecha = c.create_oval(450, 60, 500, 110, fill=colorNodo)
                    derechaText = c.create_text(475, 80, text=dato, font=("Bahnschrift Light Condensed", 18), fill=colorTexto)
                else:
                    ## IZQUIERDA
                    izquierdaLinea = c.create_line(405, 50, 370, 80, fill="white")
                    izquierda = c.create_oval(350, 60, 400, 110, fill=colorNodo)
                    izquierda = c.create_text(375, 80, text=dato, font=("Bahnschrift Light Condensed", 18), fill=colorTexto)
            else:
                for j in range(len(vec)):
                    if vec[j] == 1:
                        xi = xi + 50
                        yi = yi + 50
                        xf = xf + 50
                        yf = yf + 50
                        xText = xText + 50
                        yText = yText + 50
                        if j > 0:
                            xiLineaD = xiLineaD + 50
                            yiLineaD = yiLineaD + 50
                            xfLineaD = xfLineaD + 50
                            yfLineaD = yfLineaD + 50

                    else:
                        xi = xi - 50
                        yi = yi + 50
                        xf = xf - 50
                        yf = yf + 50
                        xText = xText - 50
                        yText = yText + 50

                        if j > 0:
                            xiLineaI = xiLineaI - 50
                            yiLineaI = yiLineaI + 50
                            xfLineaI = xfLineaI - 50
                            yfLineaI = yfLineaI + 50

                if vec[len(vec) - 1] == 1:
                    derechaLinea = c.create_line(xiLineaD, yiLineaD, xfLineaD, yfLineaD, fill="white")
                    derecha = c.create_oval(xi, yi, xf, yf, fill=colorNodo)
                    derechaText = c.create_text(xText, yText, text=dato, font=("Bahnschrift Light Condensed", 18),fill=colorTexto)
##                  c.move(derecha, 50, 0)
##                  c.move(derechaText, 50, 0)

                else:
                    izquierdaLinea = c.create_line(xiLineaI, yiLineaI, xfLineaI, yfLineaI, fill="white")
                    izquierda = c.create_oval(xi, yi, xf, yf, fill=colorNodo)
                    izquierdaText = c.create_text(xText, yText, text=dato, font=("Bahnschrift Light Condensed", 18),fill=colorTexto)
##                  c.move(izquierda, -50, 0)
##                  c.move(izquierdaText, -50, 0)

        txtNodo.delete(0,'end')
        lblMensaje.config(text="El " + str(dato) + " ha sido insertado")
        txtNodo.focus()

    else:
        txtNodo.focus()
        lblMensaje.config(text="Dato incorrecto")
        txtNodo.delete(0,'end')



colorVentana = "#fefce6"
colorNodo="#0B2239"
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
lblNodo = Label(ventana, text="", font=("Bahnschrift Light Condensed", 18), fg="orange", bg=colorVentana, anchor="center")
lblNodo.grid(row=0, column=0)

lblNodo = Label(ventana, text=" DATO:     ", font=("Bahnschrift Light Condensed", 18), fg="orange", bg=colorVentana, anchor="center")
lblNodo.grid(row=1, column=0)

txtNodo = Entry(ventana,width=25,bg="#0b2239",borderwidth = 2,fg="white", font=("Bahnschrift Light Condensed", 13))
txtNodo.grid(row=1, column=1)
txtNodo.focus()
txtNodo.bind('<Return>', onEnter)

lblTitulo = Label(ventana, text="ARBOL BINARIO", font=("Freestyle Script", 30), fg="#23827d", bg=colorVentana, anchor="center")
lblTitulo.grid(row=1, column=2, rowspan=2, columnspan=2)

btnRegistrar = Button(ventana, text="INSERTAR", activebackground=colorVentana, bg="black", fg="white", cursor="hand2", relief=GROOVE, command=insertarNodo)
btnRegistrar.grid(row=2, column=1)

lblMensaje= Label(ventana, text="", font=("Bahnschrift Light Condensed", 18), fg=colorNodo, bg=colorVentana, anchor="center")
lblMensaje.grid(row=3, column=1)

listDatos = Listbox(ventana, width=3,height= 5, bg="#9a795f", fg="white", font=("Bahnschrift Light Condensed", 18))
listDatos.place(x=155, y=420)

c = Canvas(ventana, width =800, height=430, bg="#2d3742")
c.grid(row=4, column=2, columnspan=2)

## SCROLL CANVAS
scroll_x = Scrollbar(ventana, orient="horizontal", command=c.xview)
scroll_x.grid(row=5, column=2, columnspan=2, sticky="ew")

scroll_y = Scrollbar(ventana, orient="vertical", command=c.yview)
scroll_y.grid(row=4, column=4, sticky="ns")

c.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

ventana.mainloop()