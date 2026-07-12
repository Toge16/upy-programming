#water bill 
ini="ready"
print("para salir del programa escribe [exit] en el apartado de mes")
total=0
while ini != "exit":  #input del ciclo
    mes=input("Ingresa el mes: ")
    if mes.lower() == "exit":
        break
    else:       #Process
        cons=float(input("Ingresa el consumo de agua en m3: "))
        if cons >= 0 and cons < 11:
            pagar=cons*8
            total=total+pagar
            print(f"monto a pagar: ${pagar} MXN")
        elif cons >= 11 and cons < 21:
            pagar=cons*12
            total=total+pagar
            print(f"monto a pagar: ${pagar} MXN")
        else:
            pagar=cons*18
            total=total+pagar
            print(f"monto a pagar: ${pagar} MXN")
            
            
print(f"el total a pagar es: ${total} MXN")
            
            