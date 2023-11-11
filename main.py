def vet():
    def MenuN2():
        print("1- Ingresar mascota al registro")
        print("2- Ingresar estado de ultima vacunación")
        print("3- Ingresar estado de extravio")
    def Ingresarmascota():
        nch = input("Número de chip:")
        mascotas.append(nch)
        nm = input("Nombre de la mascota:")
        mascotas.append(nm)
        nt = input("Nombre del tutor:")
        mascotas.append(nt)
        uv = int(input("Fecha de ultima vacunación (año, mes y dia todo junto):"))
        mascotas.append(uv)
        estma = input("La mascota esta extraviada:")
        mascotas.append(estma)
        print(mascotas)
        return mascotas
    def Registroult():
        e = input("Ingrese numero de chip:")
        if e in mascotas:
            a = int(input("Ingrese nueva fecha de vacunación"))
            indice = mascotas.index(e)
            mascotas[indice+3] = a
            print("La ultima fecha de vacunación fue el", mascotas[indice+3])
            print(mascotas)
    while True:
        print("BIENVENIDOS A CLINICAS SIEMPREVET")
        print("")
        print("Que necesita realizar")
        print("1- Ingresar información")
        print("2- Consultar información")
        print("")
        ele = int(input("Elección:"))
        print("")
        if ele == 1:
            MenuN2()
            men2 = int(input("Elección:"))
            print("")
            if men2 == 1:
                Ingresarmascota()
                print("")
            if men2 == 2:
                Registroult()
                print("")
            if men2 == 3:
                k = input("Ingrese numero de chip:")
                if k in mascotas:
                    indice = mascotas.index(k)
                    print(mascotas[indice])
                    print("Desea colocar en extravio a", mascotas[indice + 1])
                    print("1- Si    2- No")
                    t = int(input("Elección:"))
                    if t == 1:
                        print("")
                        print("La mascota", mascotas[indice + 1], "Se encuentra extraviada")
                        elemento = "Si"
                        mascotas[indice + 4] = elemento
                        print("Estado de extravio modificado")
                        print(mascotas)
                        print("")
                    if t == 2:
                        elemento = "No"
                        mascotas[indice + 4] = elemento
                        print("Estado de extravio modificado")
                        print(mascotas)
                        print("")
        if ele == 2:
            r = input("Ingrese numero de chip:")
            p = 20221109
            if r in mascotas:
                print("")
                indice = mascotas.index(r)
                print("Número de chip:", mascotas[indice])
                print("Nombre de la mascota:", mascotas[indice + 1])
                print("Nombre del dueño:", mascotas[indice + 2])
                print("Ultima fecha de vacunación", mascotas[indice + 3])
                print("Estado de la mascota esta extraviada:", mascotas[indice + 4])
                print("")
                if mascotas[indice + 3] < p:
                    print("09-11-2022")
                    print("Su fecha de vacunación esta atrasada")
                    print("")
                else:
                    print("09-11-2022")
                    print("Su fecha de vacunación esta al dia")
                    print("")
        else:
            print("Volver a intentar")
medico1, medico2, medico3, medico4 = ["ignacio araya","2231"], ["benjamin dinamarca", "7000"], ["ismael cabrera", "8439"], ["bastian bravo", "7830"]
mascotas = []
intentos = 0
while intentos < 3:
    print("")
    print("BIENVENIDOS A CLINICAS SIEMPREVET")
    print("")
    usuario = (input("Ingrese su usuario:"))
    contrasena= (input("Ingrese su contraseña:"))
    print("")
    pe=[usuario, contrasena]
    if pe == medico1:
        print("Ignacio Araya")
        vet()
        print("")
        print("")
        break
    if pe == medico2:
        print("Bnejamin Dinamarca")
        vet()
        print("")
        print("")
        break
    if pe == medico3:
        print("Ismael Cabrera")
        vet()
        print("")
        print("")
        break
    if pe == medico4:
        print("Bastian Bravo")
        vet()
        print("")
        print("")
        break
    else:
        intentos += 1
        print("Contraseña incorrecta. Intento " + str(intentos) + " de 3.")
else:
    print("Has superado el número máximo de intentos. El programa se cerrará.")