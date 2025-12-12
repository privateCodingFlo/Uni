import matplotlib.pyplot as plt


def newton_visualize(f, df, x0, tol=1e-10, max_iter=10):
    """
    Führt das Newton-Verfahren aus und visualisiert jeden Schritt.
    """

    # Berechne den ersten Schritt für die Intervallgröße visualisierung
    # Wir machen das vorab, nur um 'initial_step_size' zu bestimmen, wie in der Aufgabe verlangt.
    # Das "Echte" Verfahren startet dann in der Schleife.
    fx0 = f(x0)
    dfx0 = df(x0)

    # Schutz gegen Division durch Null beim Startwert
    if dfx0 == 0:
        print("Ableitung an x0 ist 0. Keine Visualisierung möglich.")
        return None

    x1_temp = x0 - fx0 / dfx0
    dist = abs(x0 - x1_temp)
    if dist == 0:
        dist = 1.0  # Fallback, falls schon auf der Nullstelle

    x = x0

    for k in range(max_iter):
        fx = f(x)
        dfx = df(x)

        # Abbruchkriterium
        if abs(fx) < tol:
            print(f"Verfahren konvergiert bei x = {x}")
            return x

        if dfx == 0:
            raise ValueError("Ableitung ist 0. Keine Lösung gefunden.")

        # Nächster Schritt
        x_next = x - fx / dfx

        # --- Visualisierung ---

        # Intervall: [x_k - 1.5 * dist, x_k + 1.5 * dist]
        # wobei dist = |x0 - x1| (initialer Abstand)

        interval_min = x - 1.5 * dist
        interval_max = x + 1.5 * dist

        # Punkte generieren (ohne Numpy)
        num_points = 100
        step_val = (interval_max - interval_min) / (num_points - 1)
        x_vals = [interval_min + i * step_val for i in range(num_points)]

        # Funktionswerte
        y_vals = [f(v) for v in x_vals]

        # Tangentengleichung: t(v) = f(x) + f'(x) * (v - x)
        tangent_vals = [fx + dfx * (v - x) for v in x_vals]

        plt.figure(figsize=(10, 6))

        # Funktion plotten
        plt.plot(x_vals, y_vals, label="f(x)", color="blue")

        # Tangente plotten
        plt.plot(x_vals, tangent_vals, "--", label="Tangente", color="orange")

        # x_Achse
        plt.axhline(0, color="black", linewidth=0.8)

        # Markierung (x_k, f(x_k))
        plt.plot(x, fx, "bo", label=f"$x_{{{k}}}$")

        # Markierung (x_{k+1}, 0) - Roter Punkt
        plt.plot(x_next, 0, "ro", label=f"$x_{{{k + 1}}}$")

        plt.title(
            f"Newton-Verfahren Schritt {k + 1}\n$x_{{{k}}} = {x:.5f}, x_{{{k + 1}}} = {x_next:.5f}$"
        )
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
        plt.grid(True)

        print(f"Zeige Plot für Schritt {k + 1}...")
        plt.show()

        # Update für nächsten Durchlauf
        x = x_next

    raise ValueError("Maximale Iterationen überschritten.")


if __name__ == "__main__":
    # Testfunktion: f(x) = x^2 - 2 (Nullstelle bei sqrt(2) approx 1.414)
    # Startwert x0 = 3
    print("Starte Newton-Visualisierung für f(x) = x^2 - 2 mit Startwert 3")

    def f_test(x):
        return x**2 - 2

    def df_test(x):
        return 2 * x

    newton_visualize(f_test, df_test, 3.0)
