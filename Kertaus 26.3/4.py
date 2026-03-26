def kuusi(koko):
    print("Tämä on kuusi!")
    for i in range(koko):
        tahdet = 2 * i + 1
        print(("*" * tahdet).center(2 * koko - 1))
    # Runko
    print("*".center(2 * koko - 1))

kuusi(5)