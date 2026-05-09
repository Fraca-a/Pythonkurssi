tarina = []
edellinen = None

while True:
    sana = input("Anna sana lisättäväksi tarinaan: ")
    if sana == "loppu":
        break
    if sana == edellinen:
        break
    tarina.append(sana)
    edellinen = sana

print(" ".join(tarina))