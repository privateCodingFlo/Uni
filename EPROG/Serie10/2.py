import matplotlib.pyplot as plt


def analyze_and_plot_file(filename):
    """
    Liest eine Datei ein, analysiert die Zeichenhäufigkeit und erstellt ein Balkendiagramm.
    """
    try:
        # Datei einlesen
        with open(filename, "r", encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Fehler: Die Datei '{filename}' wurde nicht gefunden.")
        print("Bitte stellen Sie sicher, dass data.txt im selben Ordner liegt.")
        return

    # Listen erstellen
    # Wir nutzen ein Dictionary um die Reihenfolge des ersten Auftretens zu wahren
    # und gleichzeitig zu zählen.
    # Alternativ: Erst alle zählen, dann unique list extrahieren.

    char_counts = {}
    unique_chars = []  # Liste aller Zeichen (ohne Duplikate) in Auftretensreihenfolge

    for char in text:
        if char not in char_counts:
            char_counts[char] = 0
            unique_chars.append(char)
        char_counts[char] += 1

    # Zweite Liste: Häufigkeiten in der gleichen Reihenfolge
    frequencies = [char_counts[char] for char in unique_chars]

    # Für die Darstellung auf der x-Achse: Sonderzeichen lesbar machen
    display_labels = []
    for c in unique_chars:
        if c == "\n":
            display_labels.append(r"\n")
        elif c == "\t":
            display_labels.append(r"\t")
        elif c == " ":
            display_labels.append("<SPC>")
        elif c == "\r":
            display_labels.append(r"\r")
        else:
            display_labels.append(c)

    # Diagramm erstellen
    # Breite anpassen: Min 10, oder 0.25 Zoll pro Zeichen
    plot_width = max(10, len(unique_chars) * 0.25)

    plt.figure(figsize=(plot_width, 6))

    plt.bar(range(len(unique_chars)), frequencies, tick_label=display_labels)

    plt.xlabel("Zeichen")
    plt.ylabel("Häufigkeit")
    plt.title("Häufigkeit der Zeichen in data.txt")

    # Layout optimieren
    plt.tight_layout()

    print(f"Anzahl einzigartiger Zeichen: {len(unique_chars)}")
    print("Zeige Diagramm...")
    plt.show()


if __name__ == "__main__":
    analyze_and_plot_file("EPROG\Serie10\data.txt")
