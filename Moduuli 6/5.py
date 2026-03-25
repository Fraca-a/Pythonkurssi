def poista_parittomat(lista):
    """Palauttaa uuden listan, josta on poistettu parittomat luvut."""
    uusi_lista = []
    for luku in lista:
        if luku % 2 == 0:
            uusi_lista.append(luku)
    return uusi_lista

# Pääohjelma
alkuperainen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
karsittu = poista_parittomat(alkuperainen)
print(f"Alkuperäinen lista: {alkuperainen}")
print(f"Karsittu lista:     {karsittu}")