import random

pisteiden_maara = int(input("Kuinka monta pistettä arvotaan? "))
n = 0  # Ympyrän sisään osuvat pisteet
N = 0  # Kaikki pisteet

while N < pisteiden_maara:
    # Arvotaan x ja y väliltä -1 ja 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    # Testataan onko piste ympyrän sisällä (x^2 + y^2 < 1)
    if x ** 2 + y ** 2 < 1:
        n += 1

    N += 1

piin_likiarvo = 4 * n / pisteiden_maara
print(f"Piin likiarvo on noin: {piin_likiarvo}")