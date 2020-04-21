class Nodo:
    def __init__(self, dato, izquierda, derecha):
        self.dato = dato
        self.izquierda = izquierda
        self.derecha = derecha


class arbolBinario:
    def __init__(self):
        self.cabeza = None

    def returnCabeza(self):
        return self.cabeza

    def agregarNodo(self, dato):
        vec = []
        if self.cabeza == None:
            self.cabeza = Nodo(dato, None, None)
        else:
            aux = self.cabeza
            padre = None
            while aux != None:
                padre = aux
                if dato >= aux.dato:
                    aux = aux.derecha
                    vec.append(1)
                else:
                    aux = aux.izquierda
                    vec.append(0)
            if dato >= padre.dato:
                padre.derecha = Nodo(dato, None, None)
            else:
                padre.izquierda = Nodo(dato, None, None)

        return vec


    def preOrden(self, cabeza):
        if cabeza != None:
            print(cabeza.dato)
            self.preOrden(cabeza.izquierda)
            self.preOrden(cabeza.derecha)

    def inOrden(self, cabeza):
        if cabeza != None:
            self.inOrden(cabeza.izquierda)
            print(cabeza.dato)
            self.inOrden(cabeza.derecha)

    def postOrden(self, cabeza):
        if cabeza != None:
            self.postOrden(cabeza.izquierda)
            self.postOrden(cabeza.derecha)
            print(cabeza.dato)



"""
objArbol = arbolBinario()

objArbol.agregarNodo(5)
objArbol.agregarNodo(9)
objArbol.agregarNodo(3)
objArbol.agregarNodo(10)
objArbol.agregarNodo(4)
objArbol.agregarNodo(0)
objArbol.agregarNodo(1)
objArbol.agregarNodo(6)
objArbol.agregarNodo(12)

cabeza = objArbol.returnCabeza()
print("Imprimiendo por In orden")
objArbol.inOrden(cabeza)

print("Imprimiendo por Pre orden")
objArbol.preOrden(cabeza)

print("Imprimiendo por Post orden")
objArbol.postOrden(cabeza)

vec = objArbol.agregarNodo(2)

for i in range(len(vec)):
    if vec[i] == 1:
        print("Derecha")
    else:
        print("Izquierda")

"""