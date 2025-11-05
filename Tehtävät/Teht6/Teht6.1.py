import random
def heita_noppaa():
    silmaluku = random.randint(1, 6)
    return silmaluku

def paaohjelma():
    tavoite_saavutettu = False
    heittojen_lkm = 0

    print("Aletaan heittämään noppaa. Heitetään, kunnes saadaan kuutonen.")
    while not tavoite_saavutettu:
        tulos = heita_noppaa()
        heittojen_lkm += 1

        print(f"Heitto {heittojen_lkm}. Tulos: {tulos}")
        if tulos == 6:
            tavoite_saavutettu = True

    print("-" * 35)
    print(f"Kuutonen saavutettu! 🥳")
    print(f"Heittoja tarvittiin yhteensä: {heittojen_lkm}")

if __name__ == "__main__":
    paaohjelma()