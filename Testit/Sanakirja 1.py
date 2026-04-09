hedelmat = {"ananas":4,
           "mango":3,
           "päärynä":2}

yhteishinta = 0
while True:
    hedelma = input("anna hedelmä jonka kilohinnan haluat(tyhjä lopettaa): ").lower()

    if hedelma == "":
        print("tilaus päättyy...")
        break

    if hedelma in hedelmat:
        print(f"hedelmän {hedelma}n kilohinta on {hedelmat[hedelma]}€")
        yhteishinta += hedelmat[hedelma]
    else:
        print("Meillä ei valitettavasti ole tätä hedelmää varastossa.")
        lisataanko=input("Haluako lisätä sen (Y/N):").lower()
        if lisataanko == "y":
            hinta =float(input(f"anna hinta {hedelma}lle:"))
            print(f"{hedelma} on lisätty kilohinnalla {hinta}!")

    print("yhteishinta tilauksella on", yhteishinta, "euroa.")

    print("päivitetty hinnasto: ")
    for hedelma in hedelmat:
        print(f"hedelmä: {hedelmat[hedelma]}")