def laske_summa(lista):
    """Laskee ja palauttaa listan kokonaislukujen summan."""
    summa = 0
    for luku in lista:
        summa += luku
    return summa

# Pääohjelma
luvut = [3, 7, 2, 9, 4, 6, 1]
print(f"Lista: {luvut}")
print(f"Summa: {laske_summa(luvut)}")