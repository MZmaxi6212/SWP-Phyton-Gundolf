# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# if, elif und else

zahl = 10

if zahl > 10:
    print("Größer als 10")
elif zahl == 10:
    print("Genau 10")
else:
    print("Kleiner als 10")

# For-Schleife

for i in range(5):
    print(i)

# While-Schleife

zahl = 0

while zahl < 5:
    print(zahl)
    zahl += 1

# Break (Schleife vorzeitig beenden)
for i in range(10):
    if i == 5:
        break

    print(i)

# pass (Platzhalter)
zahl = 10

if zahl > 5:
    pass
else:
    print("Zahl ist klein")

# Try-except
try:
    zahl = int(input("Gib eine Zahl ein: "))
    print(zahl)
except ValueError:
    print("Das war keine Zahl!")

# Bedingter Ausdruck (Ternary)
zahl = 10
# wertWennWahr if bedingung else wertWennFalsch
ergebnis = "Positiv" if zahl >= 0 else "Negativ"

print(ergebnis)

