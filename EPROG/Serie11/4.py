import numpy as np


def list_to_numpy_array(data_list):
    """
    Konvertiert eine Liste in ein NumPy-Array und gibt Metadaten aus.
    """
    arr = np.array(data_list)

    print("-" * 30)
    print(f"Eingabe-Liste\n{data_list}")
    print(f"NumPy Array:\n{arr}")
    # shape = (Anzahl an Elementen pro Ebene) [von außen nach innen]
    print(f"Anzahl an Elementen (Shape): {arr.shape}")
    print(f"Dimension (ndim): {arr.ndim}")
    print("-" * 30)

    return arr


def demonstrate_view_vs_copy():
    print("\n=== Demonstration: View vs Copy ===")

    original = np.array([1, 2, 3, 4, 5])
    print(f"Original Array: {original}")

    # 1. View erstellen
    # Ein View ist nur eine neue Sicht auf die GLEICHEN Daten im Speicher.
    # Änderungen im View wirken sich auf das Original aus und umgekehrt.
    arr_view = original.view()

    # 2. Copy erstellen
    # Eine Kopie erstellt ein komplett neues Objekt im Speicher mit eigenen Daten.
    # Änderungen in der Kopie haben KEINE Auswirkung auf das Original.
    arr_copy = original.copy()

    print("Erstelle View (arr_view) und Kopie (arr_copy)...")

    # Änderungen vornehmen
    print("\nÄndere erstes Element im VIEW auf 99...")
    arr_view[0] = 99

    print("Ändere zweites Element in der KOPIE auf 88...")
    arr_copy[1] = 88

    print(f"Original Array (sollte 99 enthalten, aber kein 88): {original}")
    print(f"View Array (spiegelt Original):                     {arr_view}")
    print(f"Copy Array (unabhängig):                            {arr_copy}")

    print("\nErklärung:")
    print("View: Referenziert denselben Speicherbereich (Shallow Copy/Referenz).")
    print("      'arr_view.base' ist 'original':", arr_view.base is original)
    print("Copy: Reserviert neuen Speicher und kopiert die Werte (Deep Copy).")
    print("      'arr_copy.base' ist None:", arr_copy.base is None)


if __name__ == "__main__":
    print("Test mit 1-dimensionaler Liste:")
    list_to_numpy_array([1, 2, 3, 4])

    print("\nTest mit 2-dimensionaler Liste:")
    list_to_numpy_array([[1, 2, 3], [4, 5, 6]])

    print("\nTest mit 3-dimensionaler Liste:")
    list_to_numpy_array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

    demonstrate_view_vs_copy()
