# bmi calculator

inicio="ready"
while inicio != "exit":
    w=input("Ingresa tu peso en kg: ")
    if w.lower() == "exit":
        break
    else:
        h=input("Ingresa tu altura en metros: ")
        w=float(w)
        h=float(h)
        bmi=w/(h**2)
        if bmi < 18.5:
            print("underweight")
        elif bmi >= 18.5 and bmi < 25:
            print("normal")
        else:
            print("overweight")
        
