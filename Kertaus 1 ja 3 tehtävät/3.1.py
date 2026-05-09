henkilot = {
    "John":  ["John",  30, "Engineer"],
    "Emily": ["Emily", 25, "Artist"],
    "Anna":  ["Anna",  22, "Student"],
}

print("Johnin nimi:", henkilot["John"][0])
print("Johnin ikä:", henkilot["John"][1])
print("Emilyn ammatti:", henkilot["Emily"][2])

henkilot["Anna"][2] = "Teacher"
henkilot["James"] = ["James", 28, "Writer"]
henkilot["Sophia"] = ["Sophia", 35, "Doctor"]
del henkilot["Emily"]

for avain, arvo in henkilot.items():
    print(f"{avain}: {arvo}")