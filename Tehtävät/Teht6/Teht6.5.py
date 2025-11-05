def karsi_parittomat(alkuperainen_lista: list) -> list:
    parilliset_luvut = []

    for luku in alkuperainen_lista:
        if (luku % 2) == 0:
            parilliset_luvut.append(luku)

    return parilliset_luvut


def paaohjelma():
    alkuperainen = [4, 7, 18, 1, 23, 13, 100, 0, 55]

    print("Testilista valmis:")
    print(f"Alkuperäinen lista: {alkuperainen}")
    karsittu = karsi_parittomat(alkuperainen)

    print("-" * 35)
    print("Parittomat luvut karsittu:")
    print(f"Alkuperäinen lista (muuttumaton): {alkuperainen}")
    print(f"Karsittu lista (vain parilliset): {karsittu}")
    print("-" * 35)


if __name__ == "__main__":
    paaohjelma()