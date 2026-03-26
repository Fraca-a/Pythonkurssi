def laske_yhteen(a, b):
    return a + b

def laske_vahenna(a, b):
    return a - b

def laske_kerto(a, b):
    return a * b

def laske_jaa(a, b):
    if b == 0:
        return "Virhe: jako nollalla ei onnistu"
    return a / b

print("Valitse laskutoimitus:")
print("1 - Yhteenlasku")
print("2 - Vähennyslasku")
print("3 - Kertolasku")
print("4 - Jakolasku")

valinta = input("Valinta: ")
a = float(input("Anna ensimmäinen luku: "))
b = float(input("Anna toinen luku: "))

if valinta == "1":
    print(f"Tulos: {laske_yhteen(a, b)}")
elif valinta == "2":
    print(f"Tulos: {laske_vahenna(a, b)}")
elif valinta == "3":
    print(f"Tulos: {laske_kerto(a, b)}")
elif valinta == "4":
    print(f"Tulos: {laske_jaa(a, b)}")
else:
    print("Virheellinen valinta.")