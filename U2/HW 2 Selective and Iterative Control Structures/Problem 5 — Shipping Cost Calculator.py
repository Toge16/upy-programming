#shipping cost calculator

total=0
w=""
while w != "exit":  #input del ciclo
    w=input("Ingresa el peso del paquete en kg: ")
    if w.lower() == "exit":
        break
    else:       #Process
        w=float(w)
        d=int(input("Ingresa la distancia en km: "))
        if w < 0 or d < 0:
            print("Ingresa valores válidos para peso y distancia")
        elif w < 7 and d <= 100:
            cost=50
            total=total+cost
            print(f"El costo de envío es: ${cost} MXN")
        elif w >= 7 and d <= 100:
            cost=80
            total=total+cost   
            print(f"El costo de envío es: ${cost} MXN")
        elif w < 7 and d > 100:
            cost=120
            total=total+cost
            print(f"El costo de envío es: ${cost} MXN")
        else:
            cost=200
            total=total+cost    
            print(f"El costo de envío es: ${cost} MXN") #final output
            
print(f"El total de los costos de envío es: ${total} MXN")