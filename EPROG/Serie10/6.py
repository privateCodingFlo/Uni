from random import choice
import textwrap


# Klasse zur Generierung von Text basierend auf Markov-Ketten
# Hier angepasst, sodass Zeichen (und nicht ganze Wörter) genutzt werden.
class TextGenerator:
    # Die __init__ Methode wird aufgerufen, wenn ein neues Objekt dieser Klasse erstellt wird.
    # Sie dient hier dazu, das "Gedächtnis" (das Dictionary) aufzubauen.
    def __init__(self, filename):
        # Wir speichern mögliche Übergänge in einem Dictionary
        # Der Schlüssel (Key) ist ein Paar aus zwei Zeichen, z.B. ('H', 'a').
        # Der Wert (Value) ist eine Liste aller Zeichen, die jemals auf 'Ha' folgten, z.B. ['l', 'b', 't'].
        self.possible_chars = dict()

        # c1 und c2 speichern die letzten zwei gesehenen Zeichen.
        c1 = ""
        c2 = ""

        try:
            # Datei öffnen (mit 'r' für read/lesen und utf-8 für Sonderzeichen)
            with open(filename, "r", encoding="utf-8") as f:
                # Den kompletten Text der Datei in eine einzige String-Variable laden
                content = f.read()

                # Wir brauchen mindestens zwei Zeichen, um zu starten
                if len(content) >= 2:
                    # Initialisierung: Die ersten beiden Zeichen des Textes nehmen
                    c1 = content[0]
                    c2 = content[1]

                    # Jetzt gehen wir durch den Rest des Textes (ab dem 3. Zeichen, Index 2)
                    for i in range(2, len(content)):
                        # Das ist das aktuelle Zeichen, das wir gerade betrachten (das "Nächste")
                        char = content[i]

                        # Idee: anhand der Kombination, welche Zeichen zuvor kam
                        # können wir dann sagen, welche Zeichen wahrscheinlich danach kommen müssen

                        # Das heitßt unser Schlüssel ist das Paar aus den zwei vorherigen Zeichen
                        key = (c1, c2)  # z.B. ('H', 'a')

                        # Wenn wir dieses Paar noch nie gesehen haben, legen wir eine neue Liste an
                        if key not in self.possible_chars:
                            self.possible_chars[key] = [char]
                        else:
                            # Wenn wir es schon kennen, fügen wir das neue Zeichen zur Liste der Möglichkeiten hinzu
                            self.possible_chars[key].append(char)

                        # Für den nächsten Schritt rücken wir weiter:
                        # Das alte c2 wird zum neuen c1
                        # Das aktuelle Zeichen (char) wird zum neuen c2
                        c1, c2 = c2, char

        except FileNotFoundError:
            # Falls die Datei nicht existiert, geben wir eine Fehlermeldung aus, damit das Programm nicht abstürzt
            print(f"Fehler: Die Datei '{filename}' wurde nicht gefunden.")

    # Diese Methode generiert neuen Text basierend auf dem gelernten Wissen
    def generate_text(self, char_count=300):
        # Falls beim Einlesen etwas schief ging und das Dictionary leer ist, brechen wir ab
        if not self.possible_chars:
            return "Kein Modell trainiert (Datei leer oder nicht gefunden)."

        # Wir müssen irgendwo anfangen. Wir suchen uns alle Paare (Keys) aus dem Dictionary,
        # bei denen das erste Zeichen ein Großbuchstabe ist. Das simuliert einen Satzanfang.
        start_candidates = [k for k in self.possible_chars if k[0].isupper()]

        # Falls wir keine Großbuchstaben gefunden haben (z.B. Text kleingeschrieben), nehmen wir einfach alle Paare
        if not start_candidates:
            start_candidates = list(self.possible_chars.keys())

        # Wir wählen zufällig (choice) eines dieser geeigneten Startpaare aus
        c1, c2 = choice(start_candidates)

        # Unser generierter Text beginnt mit diesen zwei Zeichen
        text = c1 + c2

        # Jetzt generieren wir solange neue Zeichen, bis wir die gewünschte Länge (char_count) erreicht haben
        for _ in range(char_count):
            key = (c1, c2)

            # Prüfen, ob wir für das aktuelle Paar (c1, c2) wissen, wie es weitergeht
            if key in self.possible_chars:
                # Wir holen uns die Liste aller Zeichen, die jemals auf dieses Paar folgten
                possible_next_chars = self.possible_chars[key]

                # Wir wählen zufällig eines davon aus.
                # Das ist der Kern von Markov-Ketten: Wenn 'e' nach 'Ha' sehr oft vorkam,
                # ist es wahrscheinlicher, dass 'e' gewählt wird, weil es öfter in der Liste steht.
                # choice: nimm ein random Element aus der Liste (stammt aus der random Library)
                next_char = choice(possible_next_chars)

                # Wir hängen das neue Zeichen an unseren Text an
                text += next_char

                # Wir rücken das Fenster weiter für den nächsten Durchlauf
                c1, c2 = c2, next_char
            else:
                # Sackgasse: Für das Paar (c1, c2) haben wir keinen Eintrag. Das sollte selten passieren.
                break

        # textwrap.fill sorgt dafür, dass der Text schön umgebrochen wird und nicht eine riesige lange Zeile ist
        return textwrap.fill(text)


if __name__ == "__main__":
    # Hier prüfen wir wieder, wo die Datei liegt (im Unterordner oder direkt hier)
    import os

    target_file = "EPROG/Serie10/data.txt"
    if not os.path.exists(target_file):
        target_file = "data.txt"

    print(f"Lese Datei ein und lerne Muster: {target_file}...")

    # Hier erstellen wir eine INSTANZ unserer Klasse. __init__ wird jetzt ausgeführt.
    my_generator = TextGenerator(target_file)

    print("\n--- Generierter Text (basiert auf zufälligen Wahrscheinlichkeiten) ---")
    # Hier rufen wir die Methode auf, um 500 Zeichen Text zu erzeugen
    print(my_generator.generate_text(500))
