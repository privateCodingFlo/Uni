from math import sqrt as sqrt
import random
import time

# ========================
# #       Aufgabe 1
# ========================


# def readNumber(text):
#     while True:
#         try:
#             number = int(float(input(text+"\t")))

#             if number < 0:
#                 number = -number

#             return number

#         except:
#             print("Keine Natürliche Zahl")


# n1 = readNumber("Zahl1:")
# n2 = readNumber("Zahl2:")

# # n1 Soll größer sein
# if (n2 > n1):
#     (n2, n1) = (n1, n2)

# if n1 % n2 == 0:
#     print("die kleinere Zahl ist ein Teiler")
# else:
#     print("die kleinere Zahl ist KEIN Teiler")

# ========================
#       Aufgabe 2
# ========================


# def readNumber(text):
#     while True:
#         try:
#             number = float(input(text+"\t"))

#             if number < 0:
#                 number = -number

#             return number

#         except:
#             print("Keine Natürliche Zahl")


# # makes c the biggest
# def rotatingSort(a, b, c):
#     if (c >= a and c >= b):
#         return (a, b, c)
#     else:
#         return rotatingSort(b, c, a)  # ein mal durchrotieren


# a = readNumber("Seitenlänge a:")
# b = readNumber("Seitenlänge b:")
# c = readNumber("Seitenlänge c ")

# # Seiten sortieren, damit c die längste Seite ist
# a, b, c = rotatingSort(a, b, c)

# # Überprüfung auf unmögliches oder entartetes Dreieck
# if c > a + b:
#     print("Das Dreieck ist unmöglich (eine Seite ist länger als die Summe der beiden anderen).")
# elif c == a + b:
#     print("Das Dreieck ist entartet (eindimensional).")
# else:
#     if a == b == c:
#         print("Das Dreieck ist gleichseitig.")
#     elif a == b or b == c or a == c:
#         print("Das Dreieck ist gleichschenklig.")
#     else:
#         print("Das Dreieck ist unregelmäßig (ungleichseitig).")

#     # Überprüfung auf rechtwinkliges Dreieck (Satz des Pythagoras)
#     # kleiner Toleranzwert wegen Rundungsfehlern durch float (1e-10 => 10er Potenz)
#     if abs(c**2 - (a**2 + b**2)) < 1e-10:
#         print("Das Dreieck ist außerdem rechtwinklig.")

# ========================
# #       Aufgabe 3
# ========================


# def mittelwert_und_std(x1, x2, x3):
#     # Liste der Werte
#     werte = [x1, x2, x3]
#     n = len(werte)  # Anzahl der Elemente in der Liste

#     # Mittelwert berechnen
#     # sum Python Funktion die alle Elemente einer Liste zusammenaddiert
#     mittelwert = sum(werte) / n

#     # Varianz berechnen (nach der Formel mit n-1)
#     # Der Generator-Ausdruck "(x - mittelwert)**2 for x in werte"
#     # for x in werte geht alle x (neu angelegte Variable in for) durch, berechnet damit dann die Suptraktion mit dem Mittlerwert,
#     # Quadriert diese und gibt das Ergebnis als neu erstellt Liste an Sum() weiter
#     varianz = sum((x - mittelwert)**2 for x in werte) / (n - 1)

#     # Standardabweichung ist die Wurzel der Varianz (s² steht in der Formel)
#     std = sqrt(varianz)

#     # Rückgabe beider Werte
#     return mittelwert, std


# # Testfälle (eine Liste an tuples)
# testwerte = [
#     (1, 2, 3),
#     (5, 5, 5),
#     (2, 8, 10),
#     (0, -3, 3)
# ]

# # gehe alle Elemente in den testwerten durch
# for x1, x2, x3 in testwerte:
#     mw, s = mittelwert_und_std(x1, x2, x3)
#     print(f"Werte: {x1}, {x2}, {x3}")
#     print(f" → Mittelwert = {mw:.2f}, Standardabweichung = {s:.2f}\n")

# ========================
# #       Aufgabe 4
# ========================
# runde = 1

# botPunkte = 0
# playerPunkte = 0

# while runde <= 3:
#     print(f"------Runde{runde}------")

#     throw_computer = random.randint(1, 3)  # 1: Schere, 2: Stein, 3: Papier

#     throw_user = int(input("Schere(1), Stein(2), Papier(3): "))
#     if throw_computer == throw_user:
#         print("Unentschieden")
#     elif throw_computer == 1 and throw_user == 2:
#         print("Stein bricht Schere, du gewinnst!")
#         playerPunkte += 1
#     elif throw_computer == 1 and throw_user == 3:
#         print("Schere schneidet Papier, Computer gewinnt!")
#         botPunkte += 1
#     elif throw_computer == 2 and throw_user == 1:
#         print("Stein bricht Schere, Computer gewinnt!")
#         botPunkte += 1
#     elif throw_computer == 2 and throw_user == 3:
#         print("Papier bedeckt Stein, du gewinnst!")
#         playerPunkte += 1
#     elif throw_computer == 3 and throw_user == 1:
#         print("Schere schneidet Papier, du gewinnst!")
#         playerPunkte += 1
#     elif throw_computer == 3 and throw_user == 2:
#         print("Papier bedeckt Stein, Computer gewinnt!")
#         botPunkte += 1
#     else:
#         print("Ungültige Eingabe")
#         runde -= 1  # ungültige Eingabe = Runde von neu
#     runde += 1

# if (botPunkte == playerPunkte):
#     print("Duell vorbei! Es ist ein UNENTSCHIEDEN")
# elif (botPunkte > playerPunkte):
#     print("Duell vorbei! Der Bot gewinnt")
# else:
#     print("Duell vorbei! Du (cheater) gewinnst")

# ========================
# #       Aufgabe 5
# ========================

# def searchForN(list, n) -> bool:

#     # Wenn Element gefunden = Schleifen abbruch, andernfalls nach n-Schritten Funktion returned False
#     for element in list:
#         if element == n:
#             list.remove(element)  # entfernt das gefundene Element

#     return list


# n = 5
# list = list(range(1, 10))  # erstelle ein Liste mit Elementen von Y bis X

# newList = searchForN(list, n)
# print(newList)


# ========================
# #       Aufgabe 6
# ========================

# # Konstante für die Anzahl der Sekunden in einem Jahr (ohne Schaltjahre)
# # 365 Tage * 24 Stunden/Tag * 60 Minuten/Stunde * 60 Sekunden/Minute
# SEKUNDEN_PRO_JAHR = 365 * 24 * 60 * 60


# def pruefe_konsistenz_alter_geburtsjahr(alter: int, geburtsjahr: int) -> bool:
#     """Überprüft, ob die Angaben Alter und Geburtsjahr konsistent sind."""

#     aktuelle_sekunden = time.time()

#     # Berechnung des aktuellen Jahres basierend auf der 365-Tage-Annahme
#     jahre_seit_1970 = aktuelle_sekunden / SEKUNDEN_PRO_JAHR
#     aktuelles_jahr = int(1970 + jahre_seit_1970)

#     # Die Konsistenzprüfung erlaubt eine Differenz von Aktuelles Jahr - Geburtsjahr
#     # gleich Alter (Geburtstag war bereits) oder gleich Alter + 1 (Geburtstag steht noch bevor).

#     erwartetes_alter_max = aktuelles_jahr - geburtsjahr
#     erwartetes_alter_min = erwartetes_alter_max - 1

#     return alter == erwartetes_alter_max or alter == erwartetes_alter_min


# # --- Beispiele für Konsistenz (Aktuelles_Jahr - Geburtsjahr = Alter ODER Aktuelles_Jahr - Geburtsjahr = Alter + 1) ---

# # Test 1: Geburtstag war bereits (Alter = Aktuelles_Jahr - Geburtsjahr)
# # Erwartung: True (z.B. 2025 - 1990 = 35; Alter ist 35)
# print(
#     f"Test 1 (Alter 35, Geburtsjahr 1990): {pruefe_konsistenz_alter_geburtsjahr(35, 1990)}")

# # Test 2: Geburtstag steht noch bevor (Alter = Aktuelles_Jahr - Geburtsjahr - 1)
# # Erwartung: True (z.B. 2025 - 1990 = 35; Alter ist 34)
# print(
#     f"Test 2 (Alter 34, Geburtsjahr 1990): {pruefe_konsistenz_alter_geburtsjahr(34, 1990)}")

# # Test 3: Konsistenz für junge Person (Geburtstag war bereits)
# # Erwartung: True (z.B. 2025 - 2020 = 5; Alter ist 5)
# print(
#     f"Test 3 (Alter 5, Geburtsjahr 2020): {pruefe_konsistenz_alter_geburtsjahr(5, 2020)}")

# # Test 4: Konsistenz für junge Person (Geburtstag steht noch bevor)
# # Erwartung: True (z.B. 2025 - 2020 = 5; Alter ist 4)
# print(
#     f"Test 4 (Alter 4, Geburtsjahr 2020): {pruefe_konsistenz_alter_geburtsjahr(4, 2020)}")


# # --- Beispiele für Inkonsistenz ---

# # Test 5: Alter zu hoch (Aktuelles_Jahr - Geburtsjahr < Alter)
# # Erwartung: False (z.B. 2025 - 1990 = 35; Alter ist 36)
# print(
#     f"Test 5 (Alter 36, Geburtsjahr 1990): {pruefe_konsistenz_alter_geburtsjahr(36, 1990)}")

# # Test 6: Alter zu niedrig (Aktuelles_Jahr - Geburtsjahr > Alter + 1)
# # Erwartung: False (z.B. 2025 - 1990 = 35; Alter ist 33)
# print(
#     f"Test 6 (Alter 33, Geburtsjahr 1990): {pruefe_konsistenz_alter_geburtsjahr(33, 1990)}")

# # Test 7: Geburtsjahr liegt in der Zukunft
# # Erwartung: False (z.B. 2025 - 2030 = -5. Alter kann nicht 1 sein)
# print(
#     f"Test 7 (Alter 1, Geburtsjahr 2030): {pruefe_konsistenz_alter_geburtsjahr(1, 2030)}")

# # Test 8: Alter ist negativ (sollte immer False sein)
# # Erwartung: False
# print(
#     f"Test 8 (Alter -5, Geburtsjahr 1990): {pruefe_konsistenz_alter_geburtsjahr(-5, 1990)}")
