
import random

# Wikipedia Seite für Statistik Vergleich: https://en.wikipedia.org/wiki/Poker_probability
# ---------- Einstellungen ----------

SYMBOLE = [
    "2", "3", "4", "5", "6", "7", "8",
    "9", "10", "B", "D", "K", "A"
]

FARBEN = ["Kreuz", "Pik", "Herz", "Karo"]

ANZAHL_SPIELE = 100000


# ---------- Kartendeck erstellen ----------
# Liste wird erstellt
KARTEN = []

# Jede Farbe bekommt alle 13 möglichen Symbole.
for farbe in FARBEN:
    for symbol in range(len(SYMBOLE)):
        # Eine Karte besteht aus Symbolposition und Farbe.
        KARTEN.append((symbol, farbe))


# ---------- Pokerhand bewerten ----------

def bewerte(hand):
    """
    Untersucht fünf Karten und gibt die Pokerkombination zurück.
    """

    # Alle Kartenwerte in einer eigenen Liste speichern.
    werte = []

    for karte in hand:
        werte.append(karte[0])

    # Kartenwerte aufsteigend sortieren.
    werte.sort()


    # Prüfen, ob alle Karten dieselbe Farbe haben.
    ist_flush = True

    for karte in hand:
        if karte[1] != hand[0][1]:
            ist_flush = False
            break


    # Alle unterschiedlichen Kartenwerte sammeln.
    einzigartige_werte = []

    for wert in werte:
        if wert not in einzigartige_werte:
            einzigartige_werte.append(wert)


    # Zählen, wie oft jeder Kartenwert vorkommt.
    gleiche = []

    for wert in einzigartige_werte:
        anzahl = werte.count(wert)
        gleiche.append(anzahl)

    # Häufigkeiten absteigend sortieren.
    gleiche.sort(reverse=True)


    # Prüfen, ob eine Straße vorhanden ist.
    ist_strasse = False

    if len(einzigartige_werte) == 5:

        # Normale Straße: fünf aufeinanderfolgende Werte.
        if werte[4] - werte[0] == 4:
            ist_strasse = True

        # Sonderfall: Ass, 2, 3, 4, 5.
        elif werte == [0, 1, 2, 3, 12]:
            ist_strasse = True


    # ---------- Pokerkombination bestimmen ----------

    # Royal Flush: 10, Bube, Dame, König und Ass.
    if ist_flush and werte == [8, 9, 10, 11, 12]:
        return "Royal Flush"

    # Straight Flush: Straße und Flush gleichzeitig.
    if ist_flush and ist_strasse:
        return "Straight Flush"

    # Vier Karten mit demselben Wert.
    if gleiche == [4, 1]:
        return "Poker (Vierling)"

    # Drei gleiche und zwei gleiche Karten.
    if gleiche == [3, 2]:
        return "Full House"

    # Fünf Karten derselben Farbe.
    if ist_flush:
        return "Flush"

    # Fünf aufeinanderfolgende Kartenwerte.
    if ist_strasse:
        return "Strasse"

    # Drei Karten mit demselben Wert.
    if gleiche == [3, 1, 1]:
        return "Drilling"

    # Zwei unterschiedliche Paare.
    if gleiche == [2, 2, 1]:
        return "Zwei Paare"

    # Zwei Karten mit demselben Wert.
    if gleiche == [2, 1, 1, 1]:
        return "Ein Paar"

    # Wenn keine andere Kombination zutrifft.
    return "Höchste Karte"


# ---------- Zähler erstellen ----------

zaehler = {
    "Royal Flush": 0,
    "Straight Flush": 0,
    "Poker (Vierling)": 0,
    "Full House": 0,
    "Flush": 0,
    "Strasse": 0,
    "Drilling": 0,
    "Zwei Paare": 0,
    "Ein Paar": 0,
    "Höchste Karte": 0
}


# ---------- Pokerspiele simulieren ----------

for spiel in range(ANZAHL_SPIELE):

    # Fünf zufällige Karten ohne Zurücklegen ziehen.
    hand = random.sample(KARTEN, 5)

    # Hand bewerten und den passenden Zähler erhöhen.
    kombination = bewerte(hand)
    zaehler[kombination] += 1


# ---------- Ergebnisse ausgeben ----------

print("Ergebnis nach", ANZAHL_SPIELE, "Spielen:\n")

for name, anzahl in zaehler.items():

    # Prozentuale Häufigkeit berechnen.
    prozent = anzahl / ANZAHL_SPIELE * 100

    # Ergebnis formatiert ausgeben.
    print(f"{name:<18} {anzahl:>7}  ({prozent:.4f} %)")
