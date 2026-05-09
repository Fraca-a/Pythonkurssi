from math import sqrt

while True:
    luku = int(input("Anna numero: "))
    if luku == 0:
        print("Exiting...")
        break
    elif luku < 0:
        print("Virheellinen numero")
    else:
        print(sqrt(luku))