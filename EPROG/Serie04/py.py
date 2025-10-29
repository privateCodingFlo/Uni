from math import sqrt
from random import randint

# ========================
#       Aufgabe 1
# ========================

# A: list[list[float]] := man gibt den Datentypen des Inputs vor als 2D matrix, welche nur Floats beinhalten darf
# def matrix_kennwerte_ohne_numpy_oder_schleifen(A: list[list[float]]):
#     # 1. Zeilensummennorm: ||A||_inf = max_i(sum_j |a_ij|)
#     # Berechnung: Liste der Zeilensummen der Beträge
#     # Inner: sum(abs(element) for element in zeile)
#     # Outer: max(...)
#     betrags_zeilensummen = [sum(abs(a_ij) for a_ij in zeile) for zeile in A]
#     zeilensummennorm = max(betrags_zeilensummen)

#     # 2. Spaltensummennorm: ||A||_1 = max_j(sum_i |a_ij|)
#     # Hier müssen wir die Matrix transponieren, um die Spalten einfacher zu summieren.

#     # Manuelle Transponierung einer 3x3-Matrix mit List Comprehension
#     # A[i][j] -> Transponierte_A[j][i]
#     A_transponiert = [
#         [A[i][j] for i in range(3)]
#         for j in range(3)
#     ]

#     # Jetzt ist die Spaltensummennorm die Zeilensummennorm der transponierten Matrix
#     betrags_spaltensummen = [sum(abs(a_ij) for a_ij in spalte)
#                              for spalte in A_transponiert]
#     spaltensummennorm = max(betrags_spaltensummen)

#     # 3. Spur: tr(A) = a_11 + a_22 + a_33
#     # Direkter Zugriff auf die Diagonalelemente
#     spur = A[0][0] + A[1][1] + A[2][2]

#     # Ausgabe der Kennwerte
#     print("--- Ergebnisse ---")
#     print(f"Matrix A:")
#     for row in A:
#         print(row)
#     print("-" * 30)
#     print(f"1. Zeilensummennorm (||A||_inf): {zeilensummennorm}")
#     print(f"2. Spaltensummennorm (||A||_1):   {spaltensummennorm}")
#     print(f"3. Spur (tr(A)):               {spur}")

#     return zeilensummennorm, spaltensummennorm, spur


# # --- Beispielanwendung ---
# # Definieren einer 3x3 Matrix
# A_beispiel = [
#     [1.0, -2.0, 3.0],
#     [4.0, 5.0, -6.0],
#     [-7.0, 8.0, 9.0]
# ]

# # Funktion aufrufen
# kennwerte = matrix_kennwerte_ohne_numpy_oder_schleifen(A_beispiel)


# ========================
#       Aufgabe 2
# ========================
# def readInput(text):
#     name = input(text+":\t")

#     return name


# def readAge(text):
#     while True:
#         try:
#             age = int(float(input(text+":\t")))

#             if age < 0:
#                 age = -age
#             elif age == 0:
#                 raise Exception()  # 0 = Ungültiges Alter => rein in den Except-Zweig

#             return age

#         except:
#             print("Keine gültiges Alter")


# def dictonaryOfInput():
#     firstName = readInput("first name")
#     lastName = readInput("last name")
#     age = readAge("age")

#     # return the values as Dictonary
#     return {
#         "firstName": firstName,
#         "LastName": lastName,
#         "age": age
#     }


# userData = [dictonaryOfInput(), dictonaryOfInput(), dictonaryOfInput()]

# all_over_18 = all(
#     person["age"] >= 18
#     for person in userData
# )

# outputText = "Es sind alle mind. 18 Jahre alt" if all_over_18 else "Es sind NICHT alle mind. 18 jahre alt."

# print(outputText)

# ========================
#       Aufgabe 3
# ========================
# def finde_nugget_zahl(p: list[int]):
#     p1 = p[0]

#     # Maximalwert zur Überprüfung:
#     # Eine sichere, moderate Obergrenze, da wir wissen, dass die Zahl nicht extrem groß ist.
#     # Theoretische obere Schätzung ist ca. 200, ich gehe etwas höher.
#     max_check = 1000

#     # ein Array erstellen der für den gefragten Rahmen ein Array mit boolschen wertne speichert um zu speichern,
#     # welche Zahlen von 0 bis max_check die Form erfüllen
#     darstellbar = [False] * (max_check + 1)

#     # 0 ist immer darstellbar (a=0, b=0, c=0)
#     darstellbar[0] = True

#     # Anzahl der aufeinanderfolgenden darstellbaren Zahlen, die wir benötigen.
#     # Wenn wir p1 (7) aufeinanderfolgende Zahlen finden, sind alle folgenden darstellbar.
#     benoetigte_anzahl = p1

#     # Iteration über alle Zahlen von 1 bis max_check
#     # HINWEIS: Hier ist die Verwendung einer for-Schleife erforderlich.
#     # Diese ist effizienter und üblicher für dieses Problem als Rekursion.
#     for i in range(1, max_check + 1):
#         # Prüfe, ob i darstellbar ist
#         for koeffizient in p:
#             if i >= koeffizient and darstellbar[i - koeffizient]:
#                 darstellbar[i] = True
#                 break

#     # Finde die längste Sequenz von True (darstellbar) am Ende
#     # und die letzte False (nicht darstellbar) davor.

#     # Wir suchen rückwärts nach der letzten False-Stelle (der größten nicht darstellbaren Zahl)
#     # Bevor wir die 'benoetigte_anzahl' (7) aufeinanderfolgende darstellbare Zahlen finden.

#     folge_zaehler = 0

#     # HINWEIS: Hier ist die Verwendung einer for-Schleife erforderlich.
#     for i in range(max_check, -1, -1):
#         if darstellbar[i]:
#             folge_zaehler += 1
#             if folge_zaehler == benoetigte_anzahl:
#                 # Wir haben 7 aufeinanderfolgende darstellbare Zahlen gefunden.
#                 # Die größte nicht darstellbare Zahl ist die davor.
#                 # Da i die kleinste Zahl in der Folge ist (rückwärtszählend),
#                 # ist i - 1 die letzte nicht darstellbare Zahl.
#                 return i - 1
#         else:
#             # Die Folge ist unterbrochen
#             folge_zaehler = 0

#     # Falls wir die Obergrenze max_check erreichen, muss diese erhöht werden
#     raise ValueError(
#         f"Die Nugget-Zahl ist größer als {max_check}. Obergrenze erhöhen.")


# # --- Ausführung des Programms ---
# # 7  => 7a  => [0] = n * a
# # 11 => 11b => [1] = n * b
# # 13 => 13c => [2] = n * c
# koeffizienten = [7, 11, 13]
# n0 = finde_nugget_zahl(koeffizienten)

# print("--- Aufgabe 3: Chicken-McNugget-Theorem ---")
# print(f"Koeffizienten: {koeffizienten}")
# print("-" * 40)
# print(f"Die größte Zahl n0, die NICHT in der Form 7a + 11b + 13c")
# print(f"dargestellt werden kann, ist: {n0}")

# ========================
#       Aufgabe 4
# ========================
# # globale gespeichert (etwas effizienter, da die berechnung nur ein mal von Nöten ists)
# sqrt5 = sqrt(5)
# psi = (1+sqrt5)/2


# def fibonaci(n):
#     result = psi**n-(-psi)**(-n)
#     return round(result)


# n = 20
# print("--- Aufgabe 4: Fibonacci-Zahlen ---")
# print(f"für n = {n}: ", fibonaci(n))


# ========================
#       Aufgabe 5
# ========================
# def ableitung_koeffizienten(a: list[float]) -> list[float]:

#     # Der Koeffizient a0 fällt weg (Multiplikation mit Index 0),
#     # daher wird er ignoriert => Iteration über die Indizes i = 1, 2, 3, ..., n.

#     # 1. Erstellen eines Index-Bereichs von 1 bis n (Länge - 1)
#     # range(1, len(a)) liefert die Indizes 1, 2, ..., len(a) - 1.
#     indizes = range(1, len(a))

#     # 2. Anwendung der Ableitungsregel (i * a_i) mithilfe einer List-Comprehension
#     # Die List-Comprehension ist die "schleifenfreie" Lösung.
#     ableitungs_koeffizienten = [
#         i * a[i]
#         for i in indizes
#     ]

#     return ableitungs_koeffizienten


# # --- Beispiel 1: f(x) = 5 + 3x + 2x^2 + 4x^3 ---
# # Koeffizienten: [a0=5, a1=3, a2=2, a3=4]
# a_beispiel1 = [5, 3, 2, 4]
# resultat1 = ableitung_koeffizienten(a_beispiel1)

# # Erwartet: [1*3, 2*2, 3*4] = [3, 4, 12]
# print("--- Aufgabe 5: Polynom-Ableitung ---")
# print(f"Ursprüngliche Koeffizienten (f(x)): {a_beispiel1}")
# print(f"Koeffizienten der Ableitung (f'(x)): {resultat1}")
# print("-" * 40)

# # --- Beispiel 2: f(x) = 10 + 0x + 0x^2 + 0x^3 + 5x^4 ---
# # Koeffizienten: [a0=10, a1=0, a2=0, a3=0, a4=5]
# a_beispiel2 = [10, 0, 0, 0, 5]
# resultat2 = ableitung_koeffizienten(a_beispiel2)

# # Erwartet: [1*0, 2*0, 3*0, 4*5] = [0, 0, 0, 20]
# print(f"Ursprüngliche Koeffizienten (f(x)): {a_beispiel2}")
# print(f"Koeffizienten der Ableitung (f'(x)): {resultat2}")

# ========================
#       Aufgabe 6
# ========================

# def wuerfelsumme(n: int) -> int:
#     """
#     Simuliert das Würfeln mit n Würfeln (ohne Schleife).
#     """
#     # Generiert n Zufallswürfe und summiert diese
#     wuerfe = [randint(1, 6) for _ in range(n)]
#     return sum(wuerfe)


# def zaehle_haeufigkeiten_rekursiv(daten: list, haeufigkeiten_dict: dict):
#     """
#     Zählt die Häufigkeiten der Ergebnisse in der Liste rekursiv (ersetzt die for-Schleife).
#     """
#     if not daten:
#         return haeufigkeiten_dict

#     ergebnis = daten[0]
#     restliche_daten = daten[1:]

#     # Dictionary aktualisieren
#     haeufigkeiten_dict[ergebnis] = haeufigkeiten_dict.get(ergebnis, 0) + 1

#     # Rekursiver Aufruf
#     return zaehle_haeufigkeiten_rekursiv(restliche_daten, haeufigkeiten_dict)


# # Simulation und Berechnung (Ohne Schleife)
# # ANZAHL_SIMULATIONEN = 1000 # 1k nicht möglich aufgrund von stack overflow
# ANZAHL_SIMULATIONEN = 500
# ergebnisse_1000 = [wuerfelsumme(2) for _ in range(ANZAHL_SIMULATIONEN)]

# # Rekursive Zählung
# haeufigkeiten = zaehle_haeufigkeiten_rekursiv(ergebnisse_1000, {})

# # Häufigstes Ergebnis finden mit max() und Generator-Ausdruck
# haeufigstes_ergebnis = max(haeufigkeiten)
# haeufigkeit_des_ergebnisses = haeufigkeiten[haeufigstes_ergebnis]

# # Ausgabe
# print("--- Aufgabe 6: Würfelsumme (Simulation) ---")
# print(f"Anzahl Simulationen: {ANZAHL_SIMULATIONEN}")
# print("Häufigkeiten der Würfelsummen (Dict):")
# print(haeufigkeiten)
# print(
#     f"\nDas häufigste Ergebnis ist: **{haeufigstes_ergebnis}** (mit {haeufigkeit_des_ergebnisses} Würfen)")
# print("-" * 40)
