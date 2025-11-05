GALLONA_LITRAKSI = 3.785

def muunna_gallonat_litroiksi(gallonat: float) -> float:
    litrat = gallonat * GALLONA_LITRAKSI
    return litrat

def paaohjelma():
    print("Gallona–litra-muunnin. Muunnos lopetetaan negatiivisella syötteellä.")

    while True:
        try:
            gallona_syote = input("\nSyötä gallonamäärä (tai negatiivinen luku lopettaaksesi): ")
            gallonat = float(gallona_syote)

            if gallonat < 0:
                print("Negatiivinen arvo syötetty. Ohjelma lopetetaan. Kiitos!")
                break

            litrat = muunna_gallonat_litroiksi(gallonat)

            print(f"{gallonat:.3f} gallonaa vastaa {litrat:.3f} litraa.")

        except ValueError:
            print("Virheellinen syöte. Syötä kelvollinen numeerinen arvo (desimaali tai kokonaisluku).")

if __name__ == "__main__":
    paaohjelma()