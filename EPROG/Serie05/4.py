from hashlib import sha256

# Die Funktion tresor() aus der Aufgabenstellung, leicht angepasst,
# um den Hash-Check durchzuführen und den Code zurückzugeben, wenn er gefunden wurde.
# Wir müssen den secret_code zusammenfügen.

# \ => Erlaubt ein Zeilenumbruch mitten im Code (Erstellt VS Code bei mir automatisch beim automatischen Formatieren)


def tresor(code):
    secret_code = ("b2b2f104d32c638903e151a9b20d6e27"
                   + "b41d8c0c84cf8458738f83ca2f1dd744")
    m = sha256()
    m.update(code.encode())
    if m.hexdigest() == secret_code:
        print("Tresor geöffnet! Code ist:", code)
        return True


def knacken():
    """
    Probiert alle 10000 möglichen 4-stelligen Codes ("0000" bis "9999") durch.
    """
    # 4-stellige Codes reichen von 0 bis 9999
    for i in range(10000):
        # Generiere den 4-stelligen String mit führenden Nullen (z.B. 5 -> "0005")
        code_string = str(i).zfill(4)

        # Prüfe den Code mit der tresor-Funktion
        if tresor(code_string):
            return  # Code gefunden => funktion ist fertig => beenden der Funktion

    return "Code nicht gefunden."


# Führe die Brute-Force-Attacke aus
knacken()
