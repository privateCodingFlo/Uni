from random import randint


def wuerfelsumme(n: int) -> int:
    """
    Simuliert das Würfeln mit n Würfeln (ohne Schleife).
    """
    return sum(randint(1, 6) for _ in range(n))


def wuerfeln_iterativ(anzahl: int) -> dict:
    """
    Führt 'anzahl' Würfe mit je 2 Würfeln durch
    und zählt, wie oft jede Summe vorkommt.
    """
    ergebnisse = {}
    for _ in range(anzahl):
        ergebnis = wuerfelsumme(2)
        
        ergebnisse[ergebnis] = ergebnisse.get(ergebnis, 0) + 1
    return ergebnisse


def haeufigste_zahl_iterativ(d: dict) -> int:
    """
    Ermittelt die häufigste Zahl (iterativ).
    """
    haeufigste = None
    max_anzahl = -1
    for zahl, anzahl in d.items():
        if anzahl > max_anzahl:
            max_anzahl = anzahl
            haeufigste = zahl
    return haeufigste


ergebnisse = wuerfeln_iterativ(10**6)
print("Ergebnisse:", ergebnisse)
print("Am häufigsten gewürfelt wurde:",
      haeufigste_zahl_iterativ(ergebnisse))
