import copy

# --- 1. Variante: Beibehaltung von Referenzen (Flache Kopie der Zeilenliste) ---


def reverse_rows_reference(matrix):
    """
    Kehrt die Zeilenreihenfolge der Matrix um.
    Die neue Matrix enthält Referenzen auf die originalen Zeilenobjekte (Flache Kopie der äußeren Liste).
    Änderungen in der neuen Matrix wirken auf die alte Matrix zurück.
    """
    # [::-1] kehrt die Liste der Zeilen um. Die Zeilen selbst sind die originalen Objekte.
    new_matrix = matrix[::-1]
    return new_matrix

# --- 2. Variante: Völlig unabhängige Matrix (Tiefe Kopie) ---


def reverse_rows_independent(matrix):
    """
    Kehrt die Zeilenreihenfolge der Matrix um und stellt sicher, dass die neue 
    Matrix völlig unabhängig von der alten ist (Tiefe Kopie).
    """
    # copy.deepcopy kopiert die gesamte verschachtelte Struktur (jede einzelne Zeile).
    deep_copy_matrix = copy.deepcopy(matrix)

    # Kehre die Reihenfolge der Zeilen in dieser tiefen Kopie um.
    new_matrix = deep_copy_matrix[::-1]
    return new_matrix

# ----------------------------------------------------------------------
# 🧪 Test der Unterschiede
# ----------------------------------------------------------------------


# Original-Matrix A für beide Tests
A = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# --- 1. Test: Referenz-Variante ---
# Wir müssen eine Kopie erstellen, da die Funktion A_ref direkt ändern wird (durch Referenzen)
A_ref_test = [row[:] for row in A]
ref_matrix = reverse_rows_reference(A_ref_test)

print("--- 1. Test: Referenz (Rückwirkung auf Original) ---")
print(f"Original A_ref vor Änderung: {A_ref_test}")

# Änderung in der NEUEN Matrix (Zeile 0, Spalte 0)
ref_matrix[0][0] = 99

print(f"\nNeue Matrix (Referenz):      {ref_matrix}")
print(f"Original A_ref NACH Änderung:  {A_ref_test}")
print(
    f"Prüfung: Das Element A_ref[2][0] ist 99 -> {A_ref_test[2][0] == 99} (Änderung wurde übertragen)")

print("-" * 50)

# --- 2. Test: Unabhängige Variante ---
A_ind_test = [row[:] for row in A]  # Startet mit der originalen Matrix
ind_matrix = reverse_rows_independent(A_ind_test)

print("--- 2. Test: Unabhängig (Keine Rückwirkung) ---")
print(f"Original A_ind vor Änderung: {A_ind_test}")

# Änderung in der NEUEN unabhängigen Matrix
ind_matrix[0][0] = 100

print(f"\nNeue Matrix (Unabhängig):    {ind_matrix}")
print(f"Original A_ind NACH Änderung:  {A_ind_test}")
print(
    f"Prüfung: Das Element A_ind[2][0] ist immer noch 7 -> {A_ind_test[2][0] == 7} (Original blieb unverändert)")
