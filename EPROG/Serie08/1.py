# Aufgabe 1: Sieb des Eratosthenes
# Implementieren Sie das Sieb des Eratosthenes, um alle Primzahlen bis zu einer gegebenen Zahl n zu finden.

def sieve_of_eratosthenes(n: int) -> list[int]:
    """
    Berechnet alle Primzahlen kleiner oder gleich n mithilfe des Siebs des Eratosthenes.

    :param n: Die Obergrenze.
    :return: Eine Liste aller Primzahlen <= n.
    """
    if n < 2:
        return []

    # Wir erstellen eine boolesche Liste "is_prime" der Größe n+1.
    # Der Index i repräsentiert die Zahl i.
    # is_prime[i] = True bedeutet, i ist (noch) eine Primzahl.
    # Wir initialisieren alle Einträge von 2 bis n mit True.
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 und 1 sind keine Primzahlen

    # Wir beginnen mit der kleinsten Primzahl p=2.
    p = 2
    # Wir müssen nur bis zur Wurzel von n iterieren, da jeder Vielfache > n bereits
    # durch einen kleineren Faktor (kleiner als sqrt(n)) gestrichen wurde.
    while p * p <= n:
        # Wenn is_prime[p] immer noch True ist, dann ist p eine Primzahl.
        if is_prime[p]:
            # Alle Vielfachen von p, beginnend bei p*p, sind keine Primzahlen mehr
            # und werden auf False gesetzt.
            # Wir starten bei p*p, weil alle kleineren Vielfachen (2p, 3p, ...)
            # bereits von kleineren Primzahlen (2, 3, ...) gestrichen wurden.
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        # Zum nächsten Kandidaten (Zahl) wechseln
        p += 1

    # Zum Schluss sammeln wir alle Zahlen, für die is_prime[i] True ist.
    print(is_prime)
    # enumerate() loopt über alle Elemente von isPrime.
    # Für alle Werte die true sind, wird die Zahl an primes weiter übergeben (bzw. in die Liste miteingefügt)
    primes = [i for i, is_p in enumerate(is_prime) if is_p]
    return primes


# Test
test_n = 50
primes_list = sieve_of_eratosthenes(test_n)
print(f"Primzahlen bis {test_n}:")
print(primes_list)

# Beispiel-Output: Primzahlen bis 50:
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
