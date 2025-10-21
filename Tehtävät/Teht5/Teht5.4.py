def kasittele_kaupungit():
    """
    Kysyy käyttäjältä viiden kaupungin nimet for-silmukalla,
    tallentaa ne listaan ja tulostaa ne sitten for/in-silmukalla.
    """
    kaupungit = []
    kaupunkien_lkm = 5

    print(f"Anna {kaupunkien_lkm} kaupungin nimet peräkkäin:")

    # 1. Käytetään for-silmukkaa nimien kysymiseen ja listaan tallentamiseen
    # range(kaupunkien_lkm) luo indeksit 0, 1, 2, 3, 4
    for i in range(kaupunkien_lkm):
        # i + 1 antaa järjestyksen 1, 2, 3, 4, 5
        nimi = input(f"Syötä {i + 1}. kaupungin nimi: ")

        # Lisätään syötetty nimi listan perään
        kaupungit.append(nimi)

    print("-" * 30)
    print("Syötetyt kaupungit samassa järjestyksessä:")

    # 2. Käytetään for/in-silmukkaa listan läpikäymiseen ja nimien tulostamiseen
    # for nimi in kaupungit käy läpi suoraan listan alkiot
    for kaupunki in kaupungit:
        print(kaupunki)


# Kutsutaan funktiota ohjelman suorittamiseksi
kasittele_kaupungit()