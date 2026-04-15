lentoasemat = {}

while True:
    print("\n1) Syötä uusi  2) Hae  3) Lopeta")
    valinta = input("Valinta: ")

    if valinta == "1":
        koodi = input("ICAO-koodi: ").upper()
        nimi = input("Lentoaseman nimi: ")
        lentoasemat[koodi] = nimi
        print(f"Tallennettu: {koodi} = {nimi}")

    elif valinta == "2":
        koodi = input("Hae ICAO-koodilla: ").upper()
        if koodi in lentoasemat:
            print(f"{koodi}: {lentoasemat[koodi]}")
        else:
            print("Lentoasemaa ei löydy.")

    elif valinta == "3":
        print("Ohjelma päättyy.")
        break

    else:
        print("Virheellinen valinta.")