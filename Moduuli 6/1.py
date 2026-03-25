import random

def heita_noppaa():
    """Palauttaa satunnaisen luvun väliltä 1–6."""
    return random.randint(1, 6)

# Pääohjelma
tulos = 0
while tulos != 6:
    tulos = heita_noppaa()
    print(f"Silmäluku: {tulos}")