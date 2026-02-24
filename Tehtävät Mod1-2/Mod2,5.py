leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

# Muunnetaan kaikki luodeiksi ja sitten grammoiksi
# 1 leiviskä = 20 naulaa, 1 naula = 32 luotia
luodit_yhteensa = (leiviskat * 20 * 32) + (naulat * 32) + luodit
grammat_yhteensa = luodit_yhteensa * 13.3

kilogrammat = int(grammat_yhteensa // 1000) # Kokonaisluvun jako
grammat_loppu = grammat_yhteensa % 1000     # Jakojäännös

print(f"Massa nykymittojen mukaan: {kilogrammat} kilogrammaa ja {grammat_loppu:.2f} grammaa.")