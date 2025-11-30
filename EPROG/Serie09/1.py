class MySet:
    def __init__(self, elements=None):
        """
        Initialisiert ein neues Set. Erlaubt die Übergabe eines einzelnen Elements, 
        einer Liste oder None für ein leeres Set.
        """
        # self.elements speichert die einzigartigen Elemente in einer Liste
        self.elements = []

        # Füllt das Set mit den übergebenen Elementen (falls vorhanden)
        if elements is not None:
            self.__hilfsfunktionZumAddenDerElemente(elements)

    def __hilfsfunktionZumAddenDerElemente(self, elements):
        """
        Interne Hilfsfunktion: Fügt Elemente oder ein einzelnes Element hinzu, 
        wobei Duplikate vermieden werden.
        """
        # Sicherstellen, dass elements ein Iterable ist, selbst wenn es nur ein Einzelelement ist
        if not isinstance(elements, (list, tuple)):
            # Einzelelement in eine Liste verpacken, um die Iteration zu vereinfachen
            elements = [elements]

        for currentElement in elements:
            if currentElement not in self.elements:
                self.elements.append(currentElement)

    # --- 1. Grundlegende Manipulation (wie im Original) ---

    def add(self, element):
        """Fügt ein einzelnes Element zum Set hinzu."""
        self.__hilfsfunktionZumAddenDerElemente(element)

    def remove(self, element):
        """
        Entfernt das Element. Löst einen ValueError aus, wenn es nicht existiert.
        (Wie das Verhalten des eingebauten set.remove())
        """
        if element in self.elements:
            self.elements.remove(element)
        else:
            # Für die Konsistenz mit dem eingebauten Set-Verhalten
            raise ValueError(f"{element} not in set")

    # --- 2. Erweiterte Manipulation ---

    def update(self, iterable):
        """Fügt mehrere Elemente aus einem Iterable (z.B. Liste, Set) hinzu."""
        self.__hilfsfunktionZumAddenDerElemente(iterable)

    def discard(self, element):
        """Entfernt das Element, löst keinen Fehler aus, wenn es nicht existiert."""
        if element in self.elements:
            self.elements.remove(element)

    def pop(self):
        """Entfernt und gibt ein zufälliges (hier: das letzte) Element zurück."""
        if not self.elements:
            raise KeyError("pop from empty set")

        # Entfernt das letzte Element (einfachste Implementierung für eine Liste)
        return self.elements.pop()

    def clear(self):
        """Entfernt alle Elemente aus dem Set."""
        self.elements = []

    # --- 3. Mathematische Mengenoperationen ---

    def union(self, other_set):
        """
        Gibt ein neues Set mit allen Elementen beider Sets zurück (Vereinigung).
        """
        if not isinstance(other_set, MySet):
            raise TypeError("Argument must be a MySet instance")

        # Erstellt eine Kopie der aktuellen Elemente
        new_set = MySet(self.elements.copy())

        # Fügt alle Elemente des anderen Sets hinzu
        new_set.update(other_set.elements)

        return new_set

    def intersection(self, other_set):
        """
        Gibt ein neues Set mit den Elementen zurück, die in beiden Sets enthalten sind (Schnittmenge).
        """
        if not isinstance(other_set, MySet):
            raise TypeError("Argument must be a MySet instance")

        new_set_elements = []
        for element in self.elements:
            if element in other_set.elements:
                new_set_elements.append(element)

        # Erstellt ein neues MySet-Objekt mit der Schnittmenge
        return MySet(new_set_elements)

    def difference(self, other_set):
        """
        Gibt ein neues Set mit den Elementen zurück, die nur in diesem Set, 
        aber nicht im other_set enthalten sind (Differenz).
        """
        if not isinstance(other_set, MySet):
            raise TypeError("Argument must be a MySet instance")

        new_set_elements = []
        for element in self.elements:
            if element not in other_set.elements:
                new_set_elements.append(element)

        return MySet(new_set_elements)

    # --- 4- Magic Methods (Dunder Methods) ---

    def __len__(self):
        """Ermöglicht die Verwendung der integrierten Funktion len()."""
        return len(self.elements)

    def __str__(self):
        """Definiert die 'informelle' String-Repräsentation für print()."""
        # Gibt das Set als lesbaren String aus, z.B. '{1, 2, 3}'
        return "{" + ", ".join(map(str, self.elements)) + "}"

    def __repr__(self):
        """Definiert die 'offizielle' String-Repräsentation für Debugging/Shell-Ausgabe."""
        # Gibt den Konstruktor-Aufruf aus, z.B. MySet([1, 2, 3])
        return f"MySet({self.elements})"

    def __iter__(self):
        """Ermöglicht die Iteration über das Set (z.B. in for-Schleifen)."""
        # Gibt einen Iterator über die interne Liste zurück
        return iter(self.elements)

    def __contains__(self, item):
        """Ermöglicht die Verwendung des 'in'-Operators (z.B. if 5 in my_set:)."""
        return item in self.elements

    # Vergleichsmethoden (Equality & Hashing)

    def __eq__(self, other):
        """Ermöglicht den Vergleich mit dem == Operator."""
        if not isinstance(other, MySet):
            return NotImplemented

        # Zwei Sets sind gleich, wenn sie die gleiche Länge haben und alle Elemente
        # des einen Sets im anderen Set enthalten sind (ungeachtet der Reihenfolge).
        return len(self) == len(other) and all(e in other.elements for e in self.elements)

    # Methoden für die Set-Operationen mit Operatoren

    def __or__(self, other):
        """Ermöglicht die Vereinigung (Union) mit dem | Operator (set_a | set_b)."""
        return self.union(other)

    def __and__(self, other):
        """Ermöglicht die Schnittmenge (Intersection) mit dem & Operator (set_a & set_b)."""
        return self.intersection(other)

    def __sub__(self, other):
        """Ermöglicht die Differenz (Difference) mit dem - Operator (set_a - set_b)."""
        return self.difference(other)

    def __add__(self, other):
        """Implementiert den '+' Operator für die Vereinigung"""
        return self.union(other)


# ----------------------------------------------------------------------
# 🧪 Testausgaben
# ----------------------------------------------------------------------

# 1. Basis-Methoden-Tests
print("--- 1. Basis-Methoden-Tests ---")

# Erstellung des ersten Sets
set_a = MySet([1, 2, 3, 4, 4, 4, 4, 1])
print(f"Set A ({set_a.__repr__()}): {set_a}")

# Hinzufügen eines einzelnen Elements
set_a.add(5)
print(f"Set A nach add(5): {set_a}")

# Hinzufügen mehrerer Elemente
set_a.update([6, 7, 3])
print(f"Set A nach update: {set_a}")

# Erstellung des zweiten Sets
set_b = MySet([4, 5, 8, 9])
print(f"Set B ({set_b.__repr__()}): {set_b}")

# Vereinigung (Union)
set_c = set_a.union(set_b)
print(f"Union (C) (Methode): {set_c}")

# Schnittmenge (Intersection)
set_d = set_a.intersection(set_b)
print(f"Intersection (D) (Methode): {set_d}")

# Differenz (Difference)
set_e = set_a.difference(set_b)
print(f"Difference (E) (Methode): {set_e}")

# Entfernen (Discard)
set_e.discard(1)
set_e.discard(100)
print(f"Set E nach discard: {set_e}")

# Leeren (Clear)
set_e.clear()
print(f"Set E nach clear: {set_e}")

print("-" * 35)

# 2. Magic-Methods-Tests

print("--- 2. Magic-Methods-Tests ---")

set1 = MySet([10, 20, 30])
set2 = MySet([30, 40, 50])
set3 = MySet([20, 10, 30])  # Gleich wie set1, nur andere Reihenfolge

# __len__: Länge
print(f"Länge von set1 (len(set1)): {len(set1)}")

# __contains__: Elementprüfung ('in'-Operator)
print(f"Ist 20 in set1? (20 in set1): {20 in set1}")
print(f"Ist 99 in set1? (99 in set1): {99 in set1}")

# __or__: Vereinigung mit dem '|'-Operator (Union)
set_union_op = set1 | set2
print(f"Union (set1 | set2): {set_union_op}")

# __and__: Schnittmenge mit dem '&'-Operator (Intersection)
set_intersection_op = set1 & set2
print(f"Intersection (set1 & set2): {set_intersection_op}")

# __sub__: Differenz mit dem '-'-Operator (Difference)
set_difference_op = set1 - set2
print(f"Difference (set1 - set2): {set_difference_op}")

# __add__: Differenz mit dem '+'-Operator (Union)
set_add_result = set1 + set2
# Ausgabe: {10, 20, 30, 40, 50}
print(f"Vereinigung mit '+': {set_add_result}")

# __eq__: Gleichheit mit dem '=='-Operator
print(f"Ist set1 gleich set3? (set1 == set3): {set1 == set3}")
print(f"Ist set1 gleich set2? (set1 == set2): {set1 == set2}")

# __iter__: Iteration in einer for-Schleife
print("Iteriere über set1:")
for element in set1:
    print(f"-> {element}")

print("-" * 35)

# __repr__ (Offizielle Repräsentation, z.B. bei Listen)
set_list = [set1, set2]
print(f"Liste von Sets ([set1, set2]): {set_list}")
