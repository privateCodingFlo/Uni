# =============================================================================
# AUFGABE 2: IEEE-754 Single Precision (32 Bit) Berechnung
# =============================================================================

# 1. Vorzeichen (Sign):
# Bit: 0
# Interpretation: Die Zahl ist positiv (+).

# 2. Exponent (E):
# Binär: 00001010
# Dezimal-Umrechnung: 2^3 + 2^1 = 8 + 2 = 10
# Wichtig: Bei IEEE-754 Single Precision wird ein Bias von 127 verwendet.
# Berechnung des realen Exponenten (e): e = E - Bias
# e = 10 - 127 = -117

# 3. Mantisse (M) / Fraction (f):
# Binär: 01000000000000000000000 (nur die erste Stelle nach dem Komma ist 1)
# Interpretation: In der normalisierten Darstellung steht vor dem Komma eine implizite 1.
# Mantissenwert (m) = 1 + f
# m = 1 + (0 * 2^-1) + (1 * 2^-2) + (0 * 2^-3) ...
# m = 1 + 0.25 = 1.25

# 4. Zusammenführung der Formel:
# Wert = (-1)^s * m * 2^e
# Wert = (-1)^0 * 1.25 * 2^-117
# Wert = 1 * 1.25 * 2^-117

# 5. Dezimalwert (wissenschaftliche Notation):
# 1.25 * 2^-117 ≈ 7.524581 * 10^-36

# -----------------------------------------------------------------------------
# Zusammenfassung:
# Vorzeichen: +
# Mantisse: 1.25
# Exponent: 2^-117
# Ergebnis: 1.25 * 2^-117
# -----------------------------------------------------------------------------

# Beispielhafter Python-Check:
import math
print(1.25 * math.pow(2, -117))
