def gallona_litroiksi(gallonaa):
    """Muuntaa US-gallonat litroiksi. 1 gallona = 3,785 litraa."""
    return gallonaa * 3.785

# Pääohjelma
while True:
    gallonaa = float(input("Syötä gallonamäärä (negatiivinen lopettaa): "))
    if gallonaa < 0:
        print("Lopetetaan.")
        break
    litraa = gallona_litroiksi(gallonaa)
    print(f"{gallonaa} gallonaa = {litraa:.3f} litraa")