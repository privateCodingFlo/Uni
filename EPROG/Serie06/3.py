# Globale Scope: x wird als globale Variable initialisiert
x = 4


# Definition der äußeren Funktion 'alpha'
def alpha(p):  # p nimmt bei alpha(10) den Wert 10 an
    # Lokale Scope von alpha: Eine NEUE lokale Variable x wird erstellt.
    x = 6
    # Lokale Variable y im Scope von alpha wird initialisiert
    y = 0+p  # y wird 10

    # Definition der Funktion 'beta'. Diese ist lokal zu alpha.
    def beta(q):  # q nimmt den Wert 2 an (von beta(2))
        # Deklaration: y stammt aus dem umschließenden Scope (alpha)
        nonlocal y
        # Ändert das y im alpha-Scope
        y += 1
        # Ändert das y im alpha-Scope
        y = y+q+p
        # Eine NEUE, lokale Variable z wird in beta erstellt (verschwindet nach Aufruf, da sie nicht benutzt wird)
        z = 1

        # Definition der Funktion 'gamma'. Diese ist lokal zu beta.
        # WICHTIG: Gamma ist nur innerhalb von beta sichtbar.
        def gamma():
            # Deklaration: x stammt aus dem globalen Scope
            global x
            # Deklaration: z stammt aus dem globalen Scope (wird dort erstellt)
            global z
            # Deklaration: y stammt aus dem umschließenden Scope (alpha)
            nonlocal y

            # Ändert das y im alpha-Scope
            y += 1
            # Setzt die globale Variable z auf 2
            z = 2
            # Ändert die globale Variable x (aktueller Wert: 4 und danach 7)
            x += 3
            # Eine lokale Variable w wird in gamma erstellt (verschwindet nach Aufruf)
            w = 5

        # List-Comprehension: 'k' ist nur lokal innerhalb dieser Expression definiert
        # 'comp' ist eine lokale Variable im Scope von beta
        comp = [k*k for k in range(3)]

        # Aufruf von gamma(): Korrekt, da gamma in beta definiert ist.
        gamma()

    # AUFRUF-FEHLER: Die folgenden Schleifen sind im Scope von beta, aber
    # rufen beta() auf, was hier zu einer REKURSION führen würde, die nicht beendet wird.
    # Zudem wird beta(2) nicht innerhalb von alpha, sondern innerhalb von beta aufgerufen.
    for i in range(2):
        beta(2)

    # Die Variable 'x' ist die lokale x von alpha
    for i in range(2):
        # i ist die lokale Schleifenvariable
        x += i  # Nutzt die lokale x von alpha.


# Globale Operation: Startet die Ausführung
alpha(10)
