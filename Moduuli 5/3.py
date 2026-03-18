n = int(input("Anna kokonaisluku: "))
on_alkuluku = True

if n < 2:
    on_alkuluku = False
else:
    for i in range(2, n):
        if n % i == 0:
            on_alkuluku = False
            break

if on_alkuluku:
    print(f"{n} on alkuluku.")
else:
    print(f"{n} ei ole alkuluku.")