#grade averaging

cont=0
suma=0
inicio=input("Ingresa [start] para iniciar: ").lower()
#input del ciclo
while inicio == "start":
    ini=input("Ingresa las calificaciones o [done] para finalizar: ")
    if ini.lower() == "done":
        break
    else:#process
        g=float(ini)
        if g >= 5:
            suma=suma+g
            cont=cont+1
        else:
            print("Ingresa una calificacion valida")
        


if cont > 0:
    avg=suma/cont
    print("El promedio de las calificaciones es: ", avg)#output
    if avg >= 8:
        print("Passed")
    else:
        print("Failed")