sanat = ["kissa", "elefantti", "koira", "perhonen", "puu", "aurinko", "talo"]

laskuri = 0
for sana in sanat:
    if len(sana) > 5:
        laskuri += 1

print(f"Yli 5 kirjaimen sanoja: {laskuri}")