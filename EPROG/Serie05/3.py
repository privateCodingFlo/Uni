# Die Dictionaries, basierend auf der Aufgabenstellung (A=1 bis Z=26)
letters = {
    "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
    "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
    "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17,
    "R": 18, "S": 19, "T": 20,
    "U": 21, "V": 22, "W": 23, "X": 24,
    "Y": 25, "Z": 26
}

# Das umgekehrte Dictionary (Position zu Buchstabe)
numbers_to_letters = {v: k for k, v in letters.items()}
ALPHABET_SIZE = 26


def encrypt(m):
    """
    Verschlüsselt das Wort m mithilfe der Cäsar-Verschlüsselung (Verschiebung +1).
    """
    encrypted_word = ""

    for char in m.upper():
        if char in letters:
            current_pos = letters[char]

            # Verschiebung +1 mit Wrap-Around (26 -> 1)
            new_pos = current_pos + 1
            if new_pos > ALPHABET_SIZE:
                new_pos = 1

            encrypted_word += numbers_to_letters[new_pos]
        else:
            encrypted_word += char

    return encrypted_word


def decrypt(m):
    """
    Entschlüsselt das Wort m mithilfe der inversen Cäsar-Verschlüsselung (Verschiebung -1).
    """
    decrypted_word = ""

    for char in m.upper():
        if char in letters:
            current_pos = letters[char]

            # Verschiebung -1 mit Wrap-Around (1 -> 26)
            new_pos = current_pos - 1
            if new_pos < 1:
                new_pos = ALPHABET_SIZE

            decrypted_word += numbers_to_letters[new_pos]
        else:
            decrypted_word += char

    return decrypted_word


# --- Testaufrufe ---
test_text = "GEHEIMNIS ZWEI"
chiffre = encrypt(test_text)
klartext = decrypt(chiffre)

print("--- Test Cäsar-Verschlüsselung ---")
print(f"Klartext:    {test_text}")
print(f"Verschlüsselt: {chiffre}")
print(f"Entschlüsselt: {klartext}")
print("-" * 34)
