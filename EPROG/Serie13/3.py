# =============================================================================
# LÖSUNG AUFGABE 3: Beweis der Eindeutigkeit
# =============================================================================

# Behauptung: Die Darstellung x = +/- (m * B^e) mit m \in [1, B) ist eindeutig.

# Beweis durch Widerspruch:
# Angenommen, es gäbe zwei verschiedene Darstellungen für dieselbe Zahl x > 0:
# (1) x = m1 * B^e1
# (2) x = m2 * B^e2
# Wobei m1, m2 im Intervall [1, B) liegen und e1, e2 ganze Zahlen sind.

# Schritt 1: Gleichsetzen
# m1 * B^e1 = m2 * B^e2  =>  m1 / m2 = B^(e2 - e1)

# Schritt 2: Grenzen betrachten
# Da 1 <= m1 < B und 1 <= m2 < B, gilt für das Verhältnis:
# 1/B < m1/m2 < B

# Schritt 3: Exponenten analysieren
# Damit die Gleichung m1/m2 = B^(e2 - e1) erfüllt ist, muss B^(e2 - e1)
# im offenen Intervall (1/B, B) liegen.
# Die einzige Potenz von B, die in diesem Intervall liegt, ist B^0 = 1.
# Daraus folgt: e2 - e1 = 0  =>  e1 = e2.

# Schritt 4: Folgerung
# Wenn e1 = e2 ist, dann muss aus m1 * B^e1 = m2 * B^e1 auch folgen:
# m1 = m2.

# Ergebnis:
# Da sowohl die Exponenten als auch die Mantissen identisch sein müssen,
# ist die Darstellung EINDEUTIG. Q.E.D.
