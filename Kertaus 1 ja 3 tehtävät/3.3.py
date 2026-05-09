kirjasto = {
    "Tuntematon sotilas":  ["Väinö Linna",  1954, "sota"],
    "Sinuhe egyptiläinen": ["Mika Waltari", 1945, "historiallinen romaani"],
    "Seitsemän veljestä":  ["Aleksis Kivi", 1870, "klassikko"],
}

print("Kirjoittaja:", kirjasto["Tuntematon sotilas"][0])
print("Genre:", kirjasto["Seitsemän veljestä"][2])

kirjasto["Sinuhe egyptiläinen"][2] = "seikkailu"
kirjasto["Mielensäpahoittaja"] = ["Tuomas Kyrö", 2010, "komedia"]
del kirjasto["Seitsemän veljestä"]

for avain, arvo in kirjasto.items():
    print(f"{avain}: {arvo}")