pituus = float(input("Anna kuhan pituus senttimetreinä: "))

if pituus < 37:
    erotus = 37 - pituus
    print(f"Kuha on alamittainen. Laske se takaisin järveen.")
    print(f"Kuhan pituudesta puuttuu {erotus} cm.")
else:
    print("Kuha on täysimittainen, voit pitää sen!")