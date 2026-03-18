luvut = []
while True:
    syote = input("Anna luku (tai tyhjä lopettaaksesi): ")
    if syote == "":
        break
    luvut.append(float(syote))

luvut.sort(reverse=True)
print("Viisi suurinta:")
for luku in luvut[:5]:
    print(luku)