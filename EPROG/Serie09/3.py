# pip installieren übers Terminal über "py -m ensurepip --upgrade"
# installieren übers Terminal über "pip install matplotlib"
# In Linux ist vielleicht auch "sudo apt install python3-pip" notwendig
import matplotlib.pyplot as plt
import math


def meine_funktion(x):
    """
    Definiert die Funktion, die geplottet werden soll.
    Beispiel: f(x) = x^2 - 4x + 3

    Achtung: Diese Funktion erwartet eine einzelne Zahl (float/int) als Input.
    """
    # return 0.5 * x**4 - 3 * x**3 + 5 * x**2 - 2*x + 0.5
    # return math.exp(x)
    return math.sin(x)


def plotte_funktion(start_x, end_x, schrittweite):
    """
    Generiert die Datenpunkte und erstellt den Plot
    """
    x_werte = []
    y_werte = []

    # 1. Datenpunkte (x-Werte) manuell generieren
    current_x = start_x
    while current_x <= end_x:
        x_werte.append(current_x)

        # 2. Funktionswerte (y-Werte) in der Schleife berechnen
        y_werte.append(meine_funktion(current_x))

        # Gehe zum nächsten Schritt
        current_x += schrittweite

    # 3. Plot erstellen
    plt.figure(figsize=(8, 5))

    # Der Plot ist identisch, nur die Datenlisten wurden anders erzeugt
    plt.plot(x_werte, y_werte, label='f(x)',
             color='darkred', linewidth=2)

    # 4. Plot beschriften und anzeigen
    plt.title('Plot einer Funktion')
    plt.xlabel('x-Achse')
    plt.ylabel('y-Achse')
    plt.axhline(0, color='gray', linestyle='--')
    plt.axvline(0, color='gray', linestyle='--')
    plt.grid(True, linestyle=':', alpha=0.7)
    plt.legend()
    plt.show()


# --- Nutzung der Funktion ---

# Definieren des Plot-Bereichs und der Granularität
START = 0
# ENDE = 2 * math.pi
ENDE = 5
SCHRITTWEITE = 0.0005  # Kleinere Zahl = glattere Kurve

plotte_funktion(START, ENDE, SCHRITTWEITE)
