import random

def heita_noppaa_tahkoilla(tahkot):
    """Palauttaa satunnaisen luvun väliltä 1–tahkot."""
    return random.randint(1, tahkot)

# Pääohjelma
tahkot = int(input("Syötä nopan maksimiarvo (tahkojen määrä): "))
tulos = 0
while tulos != tahkot:
    tulos = heita_noppaa_tahkoilla(tahkot)
    print(f"Silmäluku: {tulos}")
print(f"Saatiin maksimiarvo {tahkot}!")