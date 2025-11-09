# 1. Definieren der Liste der zu sortierenden Wörter
words = ["Programming", "Python", "algorithm", "sort", "data", "a", "aeiou"]

# 2. Definieren der Schlüsselfunktion (Key-Funktion)


def count_vowels(word):
    """
    Zählt die Anzahl der Vokale (A, E, I, O, U und ihre Kleinbuchstaben)
    in einem gegebenen Wort.
    """
    vowels = "aeiouAEIOU"
    vowel_count = 0
    # Der Hinweis legt die Verwendung von .count() nahe.
    # Wir iterieren über jeden einzelnen Vokal (a, e, i, o, u, A, E, I, O, U).
    for vowel in vowels:
        # Zählen der Vorkommen des spezifischen Vokals (z. B. 'a' oder 'A')
        # innerhalb des Wortes und Summierung der Ergebnisse.
        vowel_count += word.count(vowel)
    return vowel_count

# --- Alternativ, eine präzisere Schreibweise mit einem Generator-Ausdruck: ---
# def count_vowels(word):
#     vowels = "aeiouAEIOU"
#     return sum(word.count(v) for v in vowels)
# -----------------------------------------------------------------------


# 3. Sortieren der Liste unter Verwendung der Key-Funktion
# Die Funktion `sorted()` sortiert die Liste basierend auf dem *Rückgabewert* der
# Funktion `count_vowels`, die auf jedes Element angewendet wird.
# Da die Standard-Sortierung aufsteigend ist (kleinste Zahl zuerst) und wir
# Wörter mit *weniger* Vokalen zuerst möchten, verwenden wir die Vokalanzahl als Schlüssel.
sorted_words = sorted(words, key=count_vowels)

# 4. Ausgabe des Ergebnisses
print(f"Ursprüngliche Wortliste: {words}")
print("-" * 35)
print(f"Sortierte Liste (weniger Vokale zuerst): {sorted_words}")

# Optional: Ausgabe der Vokalanzahl zur Überprüfung
print("\nÜberprüfung (Wort: Vokalanzahl)")
for word in sorted_words:
    print(f"  {word}: {count_vowels(word)}")
