from math import sqrt
from random import randint

# # ========================
# #       Aufgabe 1
# # ========================

# # A: list[list[float]] => man gibt den Datentypen des Inputs als 2D matrix vor, welche nur Floats beinhalten darf


# def matrix_kennwerte_ohne_schleifen(A: list[list[float]]):
#     # 1. Zeilensummennorm: ||A||_inf = max_i(sum_j |a_ij|)
#     # Berechnung: Liste der Zeilensummen der Beträge
#     # Inner: sum(abs(element) for element in zeile) => bildet die Summe jeder Zeile und fügt sie in eine List zusammen
#     # Outer: max(...) => sucht größtes Element
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
# kennwerte = matrix_kennwerte_ohne_schleifen(A_beispiel)


# # ========================
# #       Aufgabe 2
# # ========================
# def readInput(text):
#     name = input(text+":\t")

#     return name


# def readAge(text):
#     while True:  # bitte ignorieren danke (ist definitiv keine Schleife)
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

# all_over_18 = all(person["age"] >= 18 for person in userData)

# outputText = "Es sind alle mind. 18 Jahre alt" if all_over_18 else "Es sind NICHT alle mind. 18 jahre alt."

# print(outputText)

# # ========================
# #       Aufgabe 3
# # ========================


# def finde_nugget_zahl_skriptmethode(koeffizienten: list[int], max_coeff: int = 100) -> int:
#     """
#     Berechnet die größte nicht darstellbare Zahl n0 für die gegebenen Koeffizienten
#     (mindestens 2) unter Verwendung der Set-Comprehension-Methode (Skript-Ansatz).

#     Args:
#         koeffizienten: Eine Liste der Koeffizienten [p1, p2, p3], z.B. [7, 11, 13].
#         max_coeff: Der maximale Wert, den jeder Koeffizient (a, b, c) in der
#                    Set-Comprehension annehmen darf, um den Suchraum zu definieren.

#     Returns:
#         Die größte nicht darstellbare Zahl n0.
#     """

#     # Der kleinste Koeffizient p1 bestimmt die Länge der lückenlosen Folge.
#     p1 = min(koeffizienten)

#     # 1. Menge M aller darstellbaren Zahlen n = p1*a + p2*b + p3*c
#     # Wir nutzen verschachtelte For-Ausdrücke innerhalb der Set-Comprehension.
#     # Dies ist die "schleifenfreie" Entsprechung der dreifach verschachtelten Schleife.
#     M = {
#         koeffizienten[0] * a + koeffizienten[1] * b + koeffizienten[2] * c
#         for a in range(0, max_coeff)
#         for b in range(0, max_coeff)
#         for c in range(0, max_coeff)
#     }

#     # 2. Prüfungs-Menge: Wir müssen nur Zahlen bis zu einer sicheren Obergrenze (z.B. 150) prüfen.
#     # Die gesuchte Zahl n0 ist für (7, 11, 13) 41. Ein Prüfbereich bis ca. 100-200 ist ausreichend.
#     MAX_CHECK_N0 = 150
#     pruef_menge = {n for n in M if n <= MAX_CHECK_N0}

#     # 3. Finde die kleinste Zahl n in PRUEF_MENGE, ab der eine lückenlose Folge von p1 Zahlen beginnt.
#     # all((n + i) in M for i in range(p1)) prüft, ob n, n+1, ..., n+(p1-1) in M sind.
#     consecutive_n_start = {
#         n
#         for n in pruef_menge
#         if all((n + i) in M for i in range(p1))
#     }

#     # 4. n0 ist die kleinste Zahl, die die Bedingung erfüllt, minus 1.
#     # min() findet den Startpunkt der ersten lückenlosen Folge.
#     # Wir müssen sicherstellen, dass die Menge nicht leer ist.
#     if not consecutive_n_start:
#         raise ValueError("Der gewählte Suchbereich (max_coeff) ist zu klein.")

#     n = min(consecutive_n_start)

#     # n-1 ist die gesuchte größte nicht darstellbare Zahl n0
#     n0 = n - 1

#     return n0

# # --- Beispielanwendung mit wählbaren Koeffizienten ---


# # Beispiel 1: Ursprüngliche Aufgabe
# koeffizienten_a = [7, 11, 13]
# ergebnis_a = finde_nugget_zahl_skriptmethode(koeffizienten_a)

# # Beispiel 2: Drei teilerfremde Zahlen (5, 7, 13)
# koeffizienten_b = [5, 7, 13]
# ergebnis_b = finde_nugget_zahl_skriptmethode(koeffizienten_b)


# print("--- Aufgabe 3: Funktion mit wählbaren Koeffizienten ---")
# print(
#     f"Koeffizienten [7, 11, 13]: Die größte nicht darstellbare Zahl n0 ist: **{ergebnis_a}**")
# print(
#     f"Koeffizienten [5, 7, 13]: Die größte nicht darstellbare Zahl n0 ist: **{ergebnis_b}**")
# print("-" * 40)

# # ========================
# #       Aufgabe 4
# # ========================
# # globale gespeichert (etwas effizienter, da die berechnung nur ein mal von Nöten ists)
# sqrt5 = sqrt(5)
# psi = (1+sqrt5)/2


# def fibonaci(n):
#     result = psi**n-(-psi)**(-n)
#     return round(result)


# n = 20
# print("--- Aufgabe 4: Fibonacci-Zahlen ---")
# print(f"für n = {n}: ", fibonaci(n))


# # ========================
# #       Aufgabe 5
# # ========================
# def ableitung_koeffizienten(a: list[float]) -> list[float]:

#     # Der Koeffizient a0 fällt weg (Multiplikation mit Index 0),
#     # daher wird er ignoriert => Iteration über die Indizes i = 1, 2, 3, ..., n.

#     # 1. Erstellen eines Index-Bereichs von 1 bis n (Länge - 1)
#     # range(1, len(a)) liefert die Indizes 1, 2, ..., len(a) - 1.
#     indizes = range(1, len(a))

#     # 2. Anwendung der Ableitungsregel (i * a_i) mithilfe einer List-Comprehension
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

# # ========================
# #       Aufgabe 6
# # ========================
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
#     # daten[1:] bei einer Länge von 1 liefert [] und darauf springt not daten an beim nöchsten rekursiven Aufruf
#     if not daten:
#         return haeufigkeiten_dict

#     # Zählen was als erstes gewürfelt wurde
#     ergebnis = daten[0]
#     # restliche Daten (ohne erstes Element nehmen für den nächsten Aufruf)
#     restliche_daten = daten[1:]

#     # Dictionary aktualisieren
#     # haeufigkeiten_dict.get(ergebnis, 0) => Die Anzahl des Gewürfelten Ergebnisses holen, oder falls es nicht im dictonary
#     #                                        inkludiert ist => nimm 0.
#     # haeufigkeiten_dict[ergebnis] = fügt das Würfelergebnis automatisch selbst hinzu, falls es noch nicht im dictonary ist
#     haeufigkeiten_dict[ergebnis] = haeufigkeiten_dict.get(ergebnis, 0) + 1

#     # Rekursiver Aufruf
#     return zaehle_haeufigkeiten_rekursiv(restliche_daten, haeufigkeiten_dict)


# # Simulation und Berechnung (Ohne Schleife)
# # ANZAHL_SIMULATIONEN = 1000 # 1k nicht möglich aufgrund von stack overflow
# ANZAHL_SIMULATIONEN = 500
# ergebnisse = [wuerfelsumme(2) for _ in range(ANZAHL_SIMULATIONEN)]

# # Rekursive Zählung
# haeufigkeiten = zaehle_haeufigkeiten_rekursiv(ergebnisse, {})

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
