def suurin_arvo(a,b,c):
    return max(a,b,c)

luku1 = float(input("Anna ensimmäinen luku: "))
luku2 = float(input("Anna toinen luku: "))
luku3 = float(input("Anna kolmas luku: "))

print(f"Suurin arvo: {suurin_arvo(luku1,luku2,luku3)}")