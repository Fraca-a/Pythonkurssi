print("1. Yhteenlasku")
print("2. Vähennyslasku")
print("3. Kertolasku")
print("4. Jakolasku")
print("5. Lopeta")

while True:
    valinta = input("\nValitse toiminto (1-5): ")
    if valinta == "5":
        print("Ohjelma lopetetaan.")
        break
    elif valinta in ("1", "2", "3", "4"):
        a = float(input("Anna ensimmäinen luku: "))
        b = float(input("Anna toinen luku: "))
        if valinta == "1":
            print(f"Tulos: {a + b}")
        elif valinta == "2":
            print(f"Tulos: {a - b}")
        elif valinta == "3":
            print(f"Tulos: {a * b}")
        elif valinta == "4":
            if b == 0:
                print("Virhe: jako nollalla ei onnistu.")
            else:
                print(f"Tulos: {a / b}")
    else:
        print("Virheellinen valinta. Valitse 1–5.")