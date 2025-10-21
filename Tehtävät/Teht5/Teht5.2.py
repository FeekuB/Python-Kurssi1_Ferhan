def etsi_viisi_suurinta():
    """
    Kysyy käyttäjältä lukuja kunnes syöte on tyhjä,
    ja tulostaa lopuksi viisi suurinta lukua.
    """
    luvut = []

    print("Syötä kokonaislukuja yksitellen. Paina Enteriä kaks kertaa putkeen lopettaaksesi syötön.")

    # while-silmukka jatkaa kysymistä, kunnes syöte on tyhjä
    while True:
        syote = input("Syötä luku: ")

        # Tarkistetaan lopetusehto
        if syote == "":
            print("\nSyöte loppu.")
            break

        try:
            # Muutetaan syöte kokonaisluvuksi
            luku = int(syote)
            luvut.append(luku)
        except ValueError:
            # Käsittelee virheelliset syötteet, jotka eivät ole lukuja
            print("Virheellinen syöte. Syötä vain kokonaislukuja tai jätä tyhjäksi.")

    # Tarkistetaan, onko lukuja syötetty ollenkaan
    if not luvut:
        print("Ei lukuja syötetty. Ohjelma päättyy.")
        return

    # Lajitellaan luvut suuruusjärjestykseen, suurimmasta pienimpään
    # Vihjeen mukaisesti: reverse=True kääntää järjestyksen
    luvut.sort(reverse=True)

    # Valitaan viisi ensimmäistä (eli suurinta) lukua
    # Jos lukuja on alle viisi, valitaan kaikki syötetyt luvut.
    viisi_suurinta = luvut[:5]

    print("-" * 30)
    print("Lajittelun jälkeen syötetyt luvut (viisi suurinta ylhäällä):")
    # Tulostetaan koko lajiteltu lista lyhyesti nähtäväksi
    print(luvut)
    print("-" * 30)

    # Tulostetaan tulos
    if len(luvut) < 5:
        print(f"Syöte sisälsi alle viisi lukua. Tässä ovat kaikki syötetyt luvut ({len(luvut)} kpl):")
    else:
        print("Viis suurinta syötettyä lukua ovat (suurimmasta alkaen):")

    for luku in viisi_suurinta:
        print(luku)


# Kutsutaan funktiota ohjelman suorittamiseksi
etsi_viisi_suurinta()