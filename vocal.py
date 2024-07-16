#Es vocal#
vocal = input("Ingrese una vocal: ")
if len(vocal) == 1 and vocal:
    if vocal in 'aeiou':
        print("Es vocal")
    else:
        print("No es vocal")
else:
     print("Solo debe ingresar una vocal")