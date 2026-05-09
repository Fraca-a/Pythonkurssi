tuntipalkka = float(input("Tuntipalkka: "))
tunnit = float(input("Tehdyt tunnit: "))
paiva = input("Viikonpäivä: ")

if paiva.lower() == "sunnuntai":
    palkka = tuntipalkka * 2 * tunnit
else:
    palkka = tuntipalkka * tunnit

print(f"Päiväpalkka: {palkka} euroa")