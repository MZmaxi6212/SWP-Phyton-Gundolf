import random


def lottoziehung():
    """
    Führt eine Lottoziehung mit 6 Zahlen aus 45 Zahlen durch.

    Jede Zahl kann nur einmal gezogen werden.
    """

    verfuegbareZahlen = list(range(1, 46))
    ziehung = []

    for i in range(6):
        index = random.randint(0, len(verfuegbareZahlen) - 1)
        zahl = verfuegbareZahlen.pop(index)
        ziehung.append(zahl)

    return ziehung


def statistikErhoehen(statistik, ziehung):
    """
    Erhöht für jede gezogene Zahl den Statistik-Zähler.
    """

    for zahl in ziehung:
        statistik[zahl] += 1


def statistikErstellen():
    """
    Erstellt ein Dictionary mit den Zahlen 1 bis 45.
    Jeder Zähler startet bei 0.
    """

    statistik = {}

    for zahl in range(1, 46):
        statistik[zahl] = 0

    return statistik


def statistikAusgeben(statistik):
    """
    Gibt die Häufigkeit jeder Lottozahl aus.
    """

    for zahl in range(1, 46):
        print(zahl, ":", statistik[zahl])


# Eine einzelne Lottoziehung
ziehung = lottoziehung()

print("Lottoziehung:")
print(ziehung)


# Statistik für viele Ziehungen
statistik = statistikErstellen()

anzahlZiehungen = 1000

for i in range(anzahlZiehungen):
    ziehung = lottoziehung()
    statistikErhoehen(statistik, ziehung)

print()
print("Statistik nach", anzahlZiehungen, "Ziehungen:")
statistikAusgeben(statistik)