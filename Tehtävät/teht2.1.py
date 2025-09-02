import math
import random

print("Moikka Ope! Mitä kuuluu?")
input("Vastaus:")
print("Toivottavasti kirjotit jotain positiivista! Mulle kuuluu pelkkää aurinkoa.")
print("Mut mennäänkö aiheeseen?! ")

#Tehtävä2.1
käyttäjä = input('Antaisitko nimesi?: ')
print("Tosi hauska tavata, " + käyttäjä + "!")

#Tehtävä2.2
# Kysytään säde käyttäjältä
sade = float(input("Antaisitko ympyrän säteen?:"))

# Lasketaan pinta-ala
pinta_ala = math.pi * sade**2

# Tulostetaan tulos
print(f"Ympyrän pinta-ala on: {pinta_ala:6.2f}")

print("Jatketaan matikka kysymyksillä xD")

#Tehtävä2.3
# Kysytään suorakulmion kanta ja korkeus
kanta = float(input("Antaisitko suorakulmion kannan?: "))
korkeus = float(input("Ja sitten suorakulmion korkeuden?: "))

# Lasketaan piiri ja pinta-alat
piiri = 2 * (kanta + korkeus)
pinta_ala = kanta * korkeus

# Tulostetaan tulokset
print(f"Suorakulmion piiri on: {piiri:6.2f}")
print(f"Suorakulmion pinta-ala on: {pinta_ala:6.2f}")

print("Huhhu on se kova!")

#Tehtävä2.4
# Kysytään käyttäjältä kolme kokonaislukua
luku1 = int(input("Antaisitko ensimmäisen kokonaisluvun: "))
luku2 = int(input("Anna viel toinen kokonaisluku: "))
luku3 = int(input("Kerta kielon päälle, anna kolmas kokonaisluku: "))

# Lasketaan summa, tulo ja keskiarvo
summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = summa / 3

# Tulostetaan tulokset
print(f"Lukujen summa on: {summa:6.2f}")
print(f"Lukujen tulo on: {tulo:6.2f}")
print(f"Lukujen keskiarvo on: {keskiarvo:6.2f}")

print("Eiks oo aika hyvin? " + käyttäjä + "!")
print("Seuraavaks vakavoidutaan hetkeks.")

print("Onko keskiaika tuttu?")
input("Vastaus:")
print("No ei mullekaa, ei se mitään! Vastaa silti seuraaviin kysymyksiin. Iha vaa kokonaislukuina")

#Tehtävä2.5
# Kysytään käyttäjältä massan mitat
leiviska = float(input("Anna leiviskät: "))
naula = float(input("Anna naulat: "))
luoti = float(input("Anna luodit: "))

# Muunnetaan kaikki luodeiksi
luoti_yhteensa = (leiviska * 20 * 32) + (naula * 32) + luoti

# Muunnetaan luodit grammoiksi
grammoja_yhteensa = luoti_yhteensa * 13.3

# Lasketaan kilogrammat ja jäljelle jääneet grammat
kilogrammat = int(grammoja_yhteensa / 1000)
grammat = grammoja_yhteensa % 1000

# Tulostetaan tulokset
print("Ton paino ois tänäpäivänä:")
print(f"{kilogrammat} kilogrammaa ja {grammat} grammaa.")

print("Huhhu, viimeistellään tää tehtävä kunnialla!")

#Tehtävä2.6

print("Seuraavaksi Pycharm arpoo maagisesti numero koodeja!")

# Arvotaan kolmenumeroinen koodi (0-9)
kolmenumeroinen_koodi = ""
for _ in range(3):
    numero = random.randint(0, 9)
    kolmenumeroinen_koodi += str(numero)

# Arvotaan nelinumeroinen koodi (1-6)
nelinumeroinen_koodi = ""
for _ in range(4):
    numero = random.randint(1, 6)
    nelinumeroinen_koodi += str(numero)

# Tulostetaan koodit
print("Kolmenumeroinen koodi:", kolmenumeroinen_koodi)
print("Nelinumeroinen pinkoodi:", nelinumeroinen_koodi)

print("Jeee!! Hyvää yötä, " + käyttäjä + "!")