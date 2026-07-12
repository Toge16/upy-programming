#seasons
season = ""
while season != "exit":  #input del ciclo
    season=input("Ingresa el número del mes (1-12): ")
    if season.lower() == "exit":
        break
    else:       #Process
        season=int(season)
        if season < 1 or season > 12:
            print("Ingresa un número de mes válido (1-12)")
        elif season == 12 or season == 1 or season == 2:
            print("Es invierno")
        elif season == 3 or season == 4 or season == 5:
            print("Es primavera")
        elif season == 6 or season == 7 or season == 8:
            print("Es verano")
        else:
            print("Es otoño") #final output
        