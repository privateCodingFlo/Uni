import math
from math import factorial as factorial
from random import randint as randInt

# ========================
#       Aufgabe 1
# ========================
# name = input("Name:\t")
# age = input("Alter:\t")

# print("Hallo ich heiße {0}, und bin {1} Jahre alt.".format(name, age))

# ========================
#       Aufgabe 2
# ========================


# def checkInput(text):
#     while True:
#         # Warnung: keine Überprüfung eingebaut, ob die Eingabe keine Zahl ist
#         userInput = int(input(text+":\t"))

#         if userInput < 0:
#             userInput = 0

#         return userInput


# n1 = checkInput("n1")
# n2 = checkInput("n2")
# print("Divisionrest von n1/n2 =", n1 % n2)


# ========================
#       Aufgabe 3
# ========================
# approximatePi = 3

# errorQuote = math.fabs(approximatePi - math.pi)/math.pi * 100

# print("Relativer Fehler: {0:.3f}%".format(errorQuote))


# ========================
#       Aufgabe 4
# ========================
# def CalculatePossibilty(dayAmount, personAmount):
#     """
#     Berechnet die Wahrscheinlichkeit P (als Dezimalwert [0, 1])
#     für die Geburtstagsparadoxon.
#     """
#     if personAmount <= 1:
#         return 0.0  # P = 0 für 0 oder 1 Person

#     if personAmount > dayAmount:
#         return 1.0  # P = 1 für N > 365 (Schubfachprinzip)

#     # P = 1 - (365! / ((365-N)! * 365^N))
#     produkt_teil = factorial(dayAmount) / factorial(dayAmount - personAmount)

#     # Berechnung des komplementären Terms
#     komplementaer_term = produkt_teil / (dayAmount ** personAmount)

#     # Berechnung der gesuchten Wahrscheinlichkeit P
#     possibilty = 1.0 - komplementaer_term

#     return possibilty

# # Bonus Aufgabe
# def SearchPossibilty(dayAmount, wantedPossibilty_percent):
#     """
#     Sucht die Personenanzahl (N), deren Wahrscheinlichkeit der
#     gewünschten Prozentzahl am nächsten kommt.
#     """
#     wantedPossibilty_decimal = wantedPossibilty_percent / 100.0

#     # Wir brauchen einen großen Wert für die Differenz, damit der erste Vergleich erfolgreich ist.
#     # Daher nehmen wir unendlich
#     bestFoundDiff = float('inf')
#     bestFoundPerson = 0

#     # Suchbereich von 1 bis 366
#     for i in range(1, dayAmount + 2):
#         # i = PersonenAnzahl
#         prob_decimal = CalculatePossibilty(dayAmount, i)

#         # Berechne die absolute Differenz zur Zielwahrscheinlichkeit
#         diff = math.fabs(wantedPossibilty_decimal - prob_decimal)

#         # Vergleich: Ist die neue Differenz kleiner als die beste bisher gefundene?
#         if diff < bestFoundDiff:
#             bestFoundDiff = diff
#             bestFoundPerson = i

#         # Optionaler Abbruch: Wenn P das Ziel überschreitet und die Differenz
#         # wieder beginnt zu steigen
#         elif prob_decimal > wantedPossibilty_decimal and bestFoundPerson > 0:
#             break

#     return bestFoundPerson


# dayAmount = 365  # Soll eine Konstante sein, aber die sind Python zu "schwer" zu schreiben

# personAmount = int(input("Personenanzahl:\t"))

# print("Die Wahrscheinlichkeit, dass {0} Personen am selben Tag Geburtstag haben, liegt bei {1:.2f}%".format(
#     personAmount, CalculatePossibilty(dayAmount, personAmount)))

# searchedPossibilty = 0.0  # in Prozent angeben (sprich das hier sind 50%)
# print("Für eine Wahrscheinlichkeit von {0}% liegt bei UNGEFÄHR {1}".format(
#     searchedPossibilty, SearchPossibilty(dayAmount, searchedPossibilty)))

# ========================
#       Aufgabe 5
# ========================
# n1 = int(input("Zahl1:\t"))
# n2 = int(input("Zahl2:\t"))

# if (n1 > n2):
#     print("Zahl1 ist größer ({0})".format(n1))
# elif (n1 < n2):
#     print("Zahl2 ist größer ({0})".format(n2))
# else:
#     print("Beide Zahlen sind gleich groß ({0} <=> {1})".format(n1, n2))

# ========================
#       Aufgabe 6
# ========================
# sum = randInt(1, 6) + randInt(1, 6)

# print("Du hast eine {0} gewürfelt".format(sum))