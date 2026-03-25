import math

def laske_yksikkohinta(halkaisija_cm, hinta_euroa):
    """
    Laskee pizzan yksikköhinnan (€/m²).
    Halkaisija annetaan senttimetreinä, hinta euroina.
    """
    sade_m = (halkaisija_cm / 2) / 100
    pinta_ala_m2 = math.pi * sade_m ** 2
    return hinta_euroa / pinta_ala_m2

# Pääohjelma
h1 = float(input("Pizza 1 – halkaisija (cm): "))
p1 = float(input("Pizza 1 – hinta (€): "))
h2 = float(input("Pizza 2 – halkaisija (cm): "))
p2 = float(input("Pizza 2 – hinta (€): "))

yk1 = laske_yksikkohinta(h1, p1)
yk2 = laske_yksikkohinta(h2, p2)

print(f"\nPizza 1: yksikköhinta {yk1:.2f} €/m²")
print(f"Pizza 2: yksikköhinta {yk2:.2f} €/m²")

if yk1 < yk2:
    print("Pizza 1 antaa paremman vasteen rahalle!")
elif yk2 < yk1:
    print("Pizza 2 antaa paremman vasteen rahalle!")
else:
    print("Pizzat ovat yhtä hyvä vastine rahalle.")