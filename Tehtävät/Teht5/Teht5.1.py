import random

def heita_arpakuutioita():
    """
    Kysyy arpakuutioiden lukumäärän, heittää niitä kerran
    ja tulostaa silmälukujen summan.
    """
    while True:
        try:
            # Kysytään käyttäjältä arpakuutioiden lukumäärä
            lkm_str = input("Kuinkas monta arpakuutiota heitetään? (Anna kokonaisluku): ")
            lkm = int(lkm_str)

            if lkm <= 0:
                print("Luvun täytyy olla positiivinen kokonaisluku.")
                continue
            break
        except ValueError:
            print("Virheellinen syöte. Syötä kokonaisluku.")

    kokonaissumma = 0

    print(f"\nHeitetään {lkm} arpakuutiota...")

    # for-silmukka toistaa heiton jokaiselle arpakuutiolle
    for i in range(lkm):
        # random.randint(1, 6) simuloi nopan heittoa (silmäluvut 1-6)
        silmaluku = random.randint(1, 6)

        # Lisätään silmäluku kokonaissummaan
        kokonaissumma += silmaluku

        # Tulostetaan kunkin nopan tulos
        print(f"Arpakuutio {i + 1}: {silmaluku}")

    # Tulostetaan kaikkien silmälukujen summa
    print("-" * 20)
    print(f"Kaikkien arpakuutioiden silmälukujen summa on: **{kokonaissumma}**")


# Kutsutaan funktiota ohjelman suorittamiseksi
heita_arpakuutioita()