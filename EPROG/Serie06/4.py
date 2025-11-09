from functools import reduce  # Importiere reduce für den Vergleich

# --- mymap Implementierung ---


def mymap(func, iterable):
    """
    Simuliert die map()-Funktion: Wendet 'func' auf jedes Element an und gibt die Ergebnisse als Liste zurück.
    """
    results = []
    for item in iterable:
        results.append(func(item))
    return results

# --- myfilter Implementierung ---


def myfilter(func, iterable):
    """
    Simuliert die filter()-Funktion: Gibt eine Liste mit Elementen zurück, 
    für die 'func' True zurückgibt.
    """
    results = []
    for item in iterable:
        if func(item):
            results.append(item)
    return results

# --- myreduce Implementierung ---


def myreduce(func, iterable, initializer=None):
    """
    Simuliert die reduce()-Funktion: Wendet 'func' kumulativ an und reduziert die Liste auf einen Einzelwert.
    """
    it = iter(iterable)

    if initializer is None:
        try:
            value = next(it)
        except StopIteration:
            raise TypeError('reduce() of empty sequence with no initial value')
    else:
        value = initializer

    for element in it:
        value = func(value, element)

    return value

# ------------------------------------------------------
#                         TESTS
# ------------------------------------------------------

# Hilfsfunktionen


def square(x):
    return x * x


def is_even(x):
    return x % 2 == 0


def add(x, y):
    return x + y


# Testdaten
numbers_map = [1, 2, 3, 4]
numbers_filter = [1, 2, 3, 4, 5, 6]
numbers_reduce = [1, 2, 3, 4, 5]


# --- 1. mymap vs. map ---
mymap_result = mymap(square, numbers_map)
# Konvertiere das Ergebnis von map() explizit in eine Liste zum Vergleich
map_builtin_result = list(map(square, numbers_map))

print("--- 1. mymap vs. map ---")
print(f"Original: {numbers_map}")
print(f"mymap Ergebnis:         {mymap_result}")
print(f"Standard map() Ergebnis: {map_builtin_result}")
print(f"Ergebnisse gleich: {mymap_result == map_builtin_result}")
print("-" * 30)

# --- 2. myfilter vs. filter ---
myfilter_result = myfilter(is_even, numbers_filter)
# Konvertiere das Ergebnis von filter() explizit in eine Liste zum Vergleich
filter_builtin_result = list(filter(is_even, numbers_filter))

print("--- 2. myfilter vs. filter ---")
print(f"Original: {numbers_filter}")
print(f"myfilter Ergebnis:         {myfilter_result}")
print(f"Standard filter() Ergebnis: {filter_builtin_result}")
print(f"Ergebnisse gleich: {myfilter_result == filter_builtin_result}")
print("-" * 30)

# --- 3. myreduce vs. functools.reduce ---
myreduce_result = myreduce(add, numbers_reduce)
reduce_builtin_result = reduce(add, numbers_reduce)
myreduce_init = myreduce(add, numbers_reduce, 10)
reduce_builtin_init = reduce(add, numbers_reduce, 10)

print("--- 3. myreduce vs. functools.reduce ---")
print(f"Liste: {numbers_reduce}")
print(f"myreduce (ohne Init):       {myreduce_result}")
print(f"Standard reduce (ohne Init): {reduce_builtin_result}")
print(f"Ergebnisse gleich: {myreduce_result == reduce_builtin_result}")
print("-" * 30)
print(f"myreduce (mit Init 10):       {myreduce_init}")
print(f"Standard reduce (mit Init 10): {reduce_builtin_init}")
print(f"Ergebnisse gleich: {myreduce_init == reduce_builtin_init}")
print("-" * 30)
