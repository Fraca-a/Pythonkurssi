kaupungit = []

for i in range(5):
    nimi = input(f"Anna kaupunki {i + 1}: ")
    kaupungit.append(nimi)

print("\nKaupungit syöttöjärjestyksessä:")
for kaupunki in kaupungit:
    print(kaupunki)