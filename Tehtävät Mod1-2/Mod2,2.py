import math

sade_str = input("Anna ympyrän säde: ")
sade = float(sade_str)  # Muutetaan teksti liukuluvuksi
pinta_ala = math.pi * sade**2

print(f"Ympyrän pinta-ala on {pinta_ala:.2f}") # :.2f pyöristää kahteen desimaaliin