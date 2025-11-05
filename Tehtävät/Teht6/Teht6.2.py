import random
def heita_noppaa(tahkojen_lkm: int) -> int:
    if tahkojen_lkm < 1:
        return 0

    silmaluku = random.randint(1, tahkojen_lkm)
    return silmaluku


def paaohjelma():
    while True:
        try:
            tahkojen_lkm_str = input("Syötä nopan tahkojen lukumäärä (esim. 6, 20 tai 21): ")
            tahkojen_lkm = int(tahkojen_lkm_str)
            if tahkojen_lkm >= 2:
                break
            else:
                print("Luvun täytyy olla vähintään 2.")
        except ValueError:
            print("Virheellinen syöte. Syötä kokonaisluku.")

    tavoite = tahkojen_lkm
    tulos = 0
    heittojen_lkm = 0

    print("-" * 50)
    print(f"Aloitetaan {tahkojen_lkm}-tahkoisen nopan heittäminen.")
    print(f"Heitetään, kunnes saadaan tavoiteluku {tavoite}")
    print("-" * 50)

    while tulos != tavoite:
        tulos = heita_noppaa(tahkojen_lkm)
        heittojen_lkm += 1

        print(f"Heitto {heittojen_lkm}. Tulos: {tulos}")

    print("-" * 50)
    print(f"Maksimisilmäluku {tavoite} saavutettu!")
    print(f"Heittoja tarvittiin yhteensä: {heittojen_lkm}")


if __name__ == "__main__":
    paaohjelma()