nimet = set()
while True:
    nimi = input("Syötä nimi (tyhjä lopettaa): ")
    if nimi == "":
        break
    if nimi in nimet:
        print(f"Aiemmin syötetty {nimi}")
    else:
        nimet.add(nimi)
        print(f"Uusi nimi {nimi}")

print("Syötetyt nimet:")
for n in nimet:
    print(n)