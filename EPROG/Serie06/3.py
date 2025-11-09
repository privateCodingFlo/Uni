# Die globale Variable x wird initialisiert
x = 4


# Definition der äußeren Funktion 'alpha'
def alpha(p):  # p wird bei Aufruf von alpha(10) den Wert 10 erhalten
    # Eine NEUE, lokale Variable x wird im Scope von alpha erstellt
    x = 6
    # Lokale Variable y im Scope von alpha wird initialisiert
    y = 0+p  # y wird 10

    # Definition der Funktion 'beta' im umschließenden Scope von alpha
    def beta(q):  # q wird 2 erhalten (von beta(2))
        # Deklaration: y stammt aus dem umschließenden Scope (alpha)
        nonlocal y
        # Ändert das y im alpha-Scope
        y += 1
        # Ändert das y im alpha-Scope
        y = y+q+p
        # Eine NEUE, lokale Variable z wird in beta erstellt (verschwindet nach Aufruf)
        z = 1

    # Definition der Funktion 'gamma' im umschließenden Scope von beta (HINWEIS: Einrückung ist fehlerhaft für den Aufruf)
    # Wenn der Code so ausgeführt wird, wie er hier steht, ist 'gamma' NUR in 'beta' definiert und unerreichbar von alpha.
    def gamma():
        # Deklaration: x stammt aus dem globalen Scope
        global x
        # Deklaration: z stammt aus dem globalen Scope (wird erstellt, falls nicht existent)
        global z
        # Deklaration: y stammt aus dem umschließenden Scope (beta oder alpha)
        # HINWEIS: Da gamma in beta definiert ist, greift es zuerst auf y in beta zu.
        # Da y in beta nicht existiert, greift es auf das y in alpha zu.
        nonlocal y
        # Ändert das y im alpha-Scope
        y += 1
        # Setzt die globale Variable z auf 2
        z = 2
        # Ändert die globale Variable x (der Wert ist aktuell 4 vor dem Aufruf)
        x += 3
        # Eine lokale Variable w wird in gamma erstellt (verschwindet nach Aufruf)
        w = 5

    # List-Comprehension: 'k' ist nur lokal innerhalb dieser Expression definiert
    comp = [k*k for k in range(3)]  # comp in beta-Scope wird [0, 1, 4]

    # AUFRUF-FEHLER: gamma() und comp sind im Scope von beta definiert und können HIER NICHT aufgerufen werden.
    # Wegen der Einrückung müsste dieser Code zu einem Fehler führen (NameError für comp und gamma).
    gamma()

    # Globale Schleife: Ruft beta(2) zweimal auf
    # AUFRUF-FEHLER: beta ist im Scope von alpha definiert und kann HIER NICHT aufgerufen werden (NameError).
    for i in range(2):
        beta(2)

    # Globale Schleife:
    for i in range(2):
        # DIESE ZEILE ist im globalen Scope, ABER die Variable 'i' existiert NUR im Scope der Schleife.
        # FEHLER: i ist hier NICHT definiert, da es keine Variable 'i' außerhalb dieser Schleife gibt.
        # Führt zu einem NameError: name 'i' is not defined
        x += i


# Globale Operation: Führt alpha aus
alpha(10)
