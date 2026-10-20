
def main():
    # 1. List Comprehension mit if-else
    print("1. List Comprehension")

    zahlen = [1, 2, 3, 4, 5, 6]

    ergebnisListe = [
        "gerade" if zahl % 2 == 0 else "ungerade"
        for zahl in zahlen
    ]

    print(ergebnisListe)

    # 2. Set Comprehension mit if-else
    print("\n2. Set Comprehension")

    temperaturen = [10, 25, 15, 30, 10]

    ergebnisSet = {
        "warm" if temperatur >= 20 else "kalt"
        for temperatur in temperaturen
    }

    print(ergebnisSet)

    # 3. Dictionary Comprehension mit if-else
    print("\n3. Dictionary Comprehension")

    punkte = {
        "Anna": 85,
        "Max": 42,
        "Lisa": 67,
        "Tom": 30
    }

    ergebnisDict = {
        name: "bestanden" if punkt >= 50 else "nicht bestanden"
        for name, punkt in punkte.items()
    }

    print(ergebnisDict)


if __name__ == "__main__":
    main()
