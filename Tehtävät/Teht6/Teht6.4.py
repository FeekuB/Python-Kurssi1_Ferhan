def laske_summa(luvut: list) -> int:
    kokonaissumma = 0

    for luku in luvut:
        kokonaissumma += luku

    return kokonaissumma


def paaohjelma():
    # 1. Luodaan testiä varten lista kokonaislukuja
    testilista = [10, 5, 20, 3, 12, 0]

    print(f"Testattava lista: {testilista}")

    # 2. Kutsutaan funktiota listan summan laskemiseksi
    summa = laske_summa(testilista)

    # 3. Tulostetaan palautettu summa
    print("-" * 30)
    print(f"Listan kokonaislukujen summa on: {summa}")

if __name__ == "__main__":
    paaohjelma()