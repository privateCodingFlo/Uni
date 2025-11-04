def check_win(position):
    """
    Überprüft, ob in der gegebenen 3x3 Tic-Tac-Toe-Position ein Spieler (X oder O) gewonnen hat.

    Args:
        position (list[list[str]]): Eine 3x3 geschachtelte Liste, z.B. 
                                    [["X", "O", "X"], ["X", "X", "O"], ["O", "X", "O"]]

    Returns:
        str: "X gewinnt", "O gewinnt", oder None, falls kein Gewinner gefunden wird.
    """

    # Spieler-Symbole, die geprüft werden sollen
    players = ["X", "O"]

    for player in players:
        # 1. Zeilen prüfen
        # Prüft, ob alle Elemente in einer Zeile dem aktuellen Spieler entsprechen
        for row in position:
            if all(cell == player for cell in row):
                return f"{player} gewinnt"

        # 2. Spalten prüfen
        # Iteriert über Spalten-Indizes (0, 1, 2)
        for col_index in range(3):
            # Erstellt eine Liste aller Zellen in dieser Spalte: [position[0][col_index], position[1][col_index], position[2][col_index]]
            column = [position[row_index][col_index] for row_index in range(3)]
            if all(cell == player for cell in column):
                return f"{player} gewinnt"

        # 3. Hauptdiagonale prüfen (von oben links nach unten rechts)
        if (position[0][0] == player and
            position[1][1] == player and
                position[2][2] == player):
            return f"{player} gewinnt"

        # 4. Nebendiagonale prüfen (von oben rechts nach unten links)
        if (position[0][2] == player and
            position[1][1] == player and
                position[2][0] == player):
            return f"{player} gewinnt"

    # Wenn nach allen Prüfungen kein Gewinner gefunden wurde
    return None


# --- Testbeispiele ---
position_example = [
    ["X", "O", "X"],
    ["X", "X", "O"],  # kein Gewinner
    ["O", "X", "O"]
]

position_x_win = [
    ["X", "O", "O"],
    ["X", "X", "X"],  # X gewinnt in dieser Zeile
    ["O", "O", "X"]
]

position_o_win_diag = [
    ["O", "X", "X"],
    ["X", "O", "X"],
    ["X", "O", "O"]   # O gewinnt in der Hauptdiagonale
]


print("--- Testergebnisse Aufgabe 5 ---")
print(f"Beispielposition: {check_win(position_example)}")
print(f"X-Gewinn (Zeile): {check_win(position_x_win)}")
print(f"O-Gewinn (Diagonale): {check_win(position_o_win_diag)}")
