oppilaat = {
    "Liisa": ["Liisa", 5, "matematiikka"],
    "Pekka": ["Pekka", 3, "liikunta"],
    "Saara": ["Saara", 7, "kuvataide"],
}

print("Liisan vuosiluokka:", oppilaat["Liisa"][1])
print("Pekan lempiaine:", oppilaat["Pekka"][2])

oppilaat["Saara"][2] = "musiikki"
oppilaat["Tommi"] = ["Tommi", 6, "historia"]
del oppilaat["Pekka"]

for avain, arvo in oppilaat.items():
    print(f"{avain}: {arvo}")