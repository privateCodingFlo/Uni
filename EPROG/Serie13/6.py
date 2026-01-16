import random

# Gegebene Basisklasse


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.score = {player1: 0, player2: 0}
        self.winner = None

    def announce_winner(self, player):
        if self.winner is None:
            self.winner = player
            print(f"The winner is {player}!")
        else:
            raise Exception("Game already has a winner.")

    def update_score(self, player, points):
        if player in self.score:
            self.score[player] += points
        else:
            raise Exception("Player not found in the game.")

# 1. Klasse Cointoss


class Cointoss(Game):
    def play_round(self):
        # Zufälliger Wurf: 0 für Kopf, 1 für Zahl
        wurf = random.randint(0, 1)
        if wurf == 0:
            print("Kopf! Punkt für", self.player1)
            self.update_score(self.player1, 1)
        else:
            print("Zahl! Punkt für", self.player2)
            self.update_score(self.player2, 1)

        # Punktestand ausgeben
        print(
            f"Stand: {self.player1}: {self.score[self.player1]} | {self.player2}: {self.score[self.player2]}")

        # Überprüfen, ob ein Spieler 3 Punkte hat
        if self.score[self.player1] >= 3:
            self.announce_winner(self.player1)
        elif self.score[self.player2] >= 3:
            self.announce_winner(self.player2)

# 2. Klasse Battleship1d


class Battleship1d(Game):
    def __init__(self, player1, player2):
        super().__init__(player1, player2)
        # Schiffe zufällig auf 10 Feldern (0-9) verstecken
        self.ships = {
            self.player1: random.randint(0, 9),
            self.player2: random.randint(0, 9)
        }

    def play_round(self):
        # Spieler 1 rät
        guess1 = int(
            input(f"{self.player1}, welches Feld (0-9) greifst du an? "))
        if guess1 == self.ships[self.player2]:
            print("Treffer!")
            self.announce_winner(self.player1)
            return  # Runde beenden, wenn Spieler 1 bereits gewonnen hat

        # Spieler 2 rät
        guess2 = int(
            input(f"{self.player2}, welches Feld (0-9) greifst du an? "))
        if guess2 == self.ships[self.player1]:
            print("Treffer!")
            self.announce_winner(self.player2)

# --- Test der Implementierung mit einer while-Schleife ---


print("--- Start Cointoss ---")
coin_game = Cointoss("Alice", "Bob")
while coin_game.winner is None:
    coin_game.play_round()

print("\n--- Start Battleship1d ---")
ship_game = Battleship1d("Spieler A", "Spieler B")
while ship_game.winner is None:
    ship_game.play_round()
