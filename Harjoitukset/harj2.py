print('Hei, maailma!')
print("Hei, maailma!")
print('"Hei", sanoi Ville')
print("Hyvää")
print("huomenta")
print("Hyvää\nhuomenta")

käyttäjä = input('Anna nimesi: ')
print("Hauska tavata, " + käyttäjä + "!")
print(käyttäjä)

eka = -9
toka = 12_456_123_180
kolmas = 4.973
neljäs = -4 + 2j

print(eka)
print(toka)
print(kolmas)
print(neljäs)
print(neljäs.real)
print(neljäs.imag)

fahrenheit_str = input("Anna lämpötila Fahrenheit-asteina: ")
fahrenheit = float(fahrenheit_str)
celsius = (fahrenheit-32)*5/9
print("Lämpötila Celsius-asteina: " + str(celsius))

fahrenheit_str = input("Anna lämpötila Fahrenheit-asteina: ")
fahrenheit = float(fahrenheit_str)
celsius = (fahrenheit-32)*5/9
print(f"Lämpötila Celsius-asteina: {celsius:6.2f}")