lista = []

while True:
    arvo = int(input("Uusi arvo: "))
    if arvo == 0:
        print("Hei hei!")
        break
    lista.append(arvo)
    print(f"Lista nyt: {lista}")
    print(f"Lista järjestyksessä: {sorted(lista)}")