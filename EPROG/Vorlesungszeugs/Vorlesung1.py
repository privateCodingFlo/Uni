# Nur für mich neues wird mitgeschrieben
x = 2/3

# {:A.Bf}
# A: Anzahl an Zeichen insgesamt (kann von B "überschrieben" werden)
# B: Anzahl der Kommastellen
# f: Zeichen für ein Float (wichtig scheinbar, vielleicht geht aber auch lf oder ähnliches)

print("2/3 = {:4.2f}".format(x))
print("2/3 = {:4.3f}".format(x))
print("2/3 = {:6.2f}".format(x))    # A begrenzt
print("2/3 = {:6.10f}".format(x))   # B überschreibt A

# lesbare Schreibweise für Große Zahlen (statt '.' nutzt man '_')
print(5_000_000)

# groß Buchstaben -> klein buchstaben
# klein Buchstaben -> groß Buchstaben
print("OlAaAaAaAaAaaaAAAA".swapcase())

x = 3.14
print(isinstance(x, float))  # Typencheck
x = 3
print(isinstance(x, float))  # Typencheck
print(isinstance(x, int))   # Typencheck

print("\nXOR:")
print(True ^ True)
print(True ^ False)
