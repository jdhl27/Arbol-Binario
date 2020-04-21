## 1. Escriba un programa para determinar sí un número entero A es divisible por otro B.

nA = 0
nB = 0
print("____________________________________________________________")
print("| DETERMINAR SI UN NÚMERO A ES DIVISIBLE POR  OTRO NÚMERO B |")
print("|___________________________________________________________|")
print("|                     A       |____B____                    |")
print("|                    Residuo  | Cociente                    |")
print("|                             |                             |")
print("|___________________________________________________________|")
print("")
while nA == 0:
    nA = int(input("Ingrese número entero A(Diferente de cero): "))

while nB == 0:
    nB = int(input("Ingrese número entero B(Diferente de cero): "))

cociente = int(nA / nB)
residuo = int(nA % nB)

if residuo == 0:
    print("A Y B SON DIVISIBLES: ")
    print(str(nA) + "  |__" + str(nB) + "__")
    print(" " + str(residuo) + "  | " + str(cociente))

    print("----------------------------------------------------------------------")
    print("RAZÓN: Para que sean divisibles el residuo tiene que ser igual a cero.")
    print("----------------------------------------------------------------------")

else:
    print("A Y B NO SON DIVISIBLES: ")
    print(str(nA) + "   |__" + str(nB) + "__")
    print(" " + str(residuo) + "  | " + str(cociente))
    print("----------------------------------------------------------------------")
    print("RAZÓN: Para que sean divisibles el residuo tiene que ser igual a cero.")
    print("----------------------------------------------------------------------")
