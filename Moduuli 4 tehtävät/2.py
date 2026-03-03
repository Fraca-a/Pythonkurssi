tuuma = float(input("Anna tuumamäärä (negatiivinen luku lopettaa): "))

while tuuma >= 0:
    cm = tuuma * 2.54
    print(f"{tuuma} tuumaa on {cm:.2f} cm.")
    tuuma = float(input("Anna uusi tuumamäärä: "))

print("Ohjelma lopetettu.")