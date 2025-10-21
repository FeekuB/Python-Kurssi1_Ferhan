def onko_alkuluku():
    """
    Kysyy käyttäjältä kokonaisluvun ja ilmoittaa, onko se alkuluku.
    """
    while True:
        try:
            # Kysytään kokonaisluku käyttäjältä
            syote = input("Syötä kokonaisluku (vähintään 2): ")
            luku = int(syote)
            break
        except ValueError:
            print("Virheellinen syöte. Syötä kokonaisluku.")

    # Alkuluvun määritelmä poissulkee luvut < 2
    if luku < 2:
        print(f"Luku {luku} ei ole alkuluku.")
        return

    # Asetetaan lippumuuttuja (flag) oletukseksi, että luku on alkuluku
    on_alkuluku_flag = True

    # Tarkistetaan jaollisuus luvuilla 2:sta lukuun luku-1
    # Huom! Riittää tarkistaa lukuun neliöjuuri(luku) asti, mutta
    # yksinkertaisuuden vuoksi käytetään tässä koko väliä: range(2, luku)

    # for-silmukka käy läpi kaikki mahdolliset jakajat
    for jakaja in range(2, luku):
        # Moduulo-operaattori (%) tarkistaa, meneekö jako tasan
        if (luku % jakaja) == 0:
            # Jos jako menee tasan, luku ei ole alkuluku
            on_alkuluku_flag = False
            print(f"Luku {luku} on jaollinen luvulla {jakaja}.")
            # Jos jakaja on löydetty, silmukka voidaan lopettaa (ei tarvitse jatkaa)
            break

    print("-" * 30)

    # Tulostetaan lopputulos lipun (flag) perusteella
    if on_alkuluku_flag:
        print(f"**Luku {luku} on alkuluku.** 👍")
    else:
        print(f"**Luku {luku} ei ole alkuluku.** 👎")


# Kutsutaan funktiota ohjelman suorittamiseksi
onko_alkuluku()