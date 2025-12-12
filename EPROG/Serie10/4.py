import matplotlib.pyplot as plt


def bisection_method(f, a, b, tol=1e-15, max_iter=50):
    """
    Führt das Bisektionsverfahren aus und gibt die Historie der Approximationen zurück.
    """
    history = []

    if f(a) * f(b) >= 0:
        print(
            "Bisektionsverfahren Fehler: f(a) und f(b) müssen unterschiedliche Vorzeichen haben."
        )
        return history

    for _ in range(max_iter):
        m = (a + b) / 2.0
        history.append(m)

        if abs(f(m)) < tol or (b - a) / 2.0 < tol:
            break

        if f(m) * f(a) < 0:
            b = m
        else:
            a = m

    return history


def newton_method(f, df, x0, tol=1e-15, max_iter=50):
    """
    Führt das Newton-Verfahren aus und gibt die Historie der Approximationen zurück.
    """
    history = []
    x = x0
    history.append(x)

    for _ in range(max_iter):
        fx = f(x)
        dfx = df(x)

        if dfx == 0:
            print("Newton-Verfahren Fehler: Ableitung ist 0.")
            break

        x_next = x - fx / dfx
        history.append(x_next)

        if abs(x_next - x) < tol:  # oder abs(f(x_next)) < tol
            break

        x = x_next

    return history


def run_analysis(f, df, bisection_interval, newton_start, name):
    print(f"\n--- Analyse für Funktion: {name} ---")

    # Bisektion
    a, b = bisection_interval
    hist_bisect = bisection_method(f, a, b)
    errors_bisect = [abs(f(x)) for x in hist_bisect]

    # Newton
    hist_newton = newton_method(f, df, newton_start)
    errors_newton = [abs(f(x)) for x in hist_newton]

    # Plotting
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # Plot 1: Normal skaliert
    ax1.plot(range(len(errors_bisect)), errors_bisect, label="Bisektion", marker="x")
    ax1.plot(range(len(errors_newton)), errors_newton, label="Newton", marker="o")
    ax1.set_title(f"{name}: Konvergenz (Linear)")
    ax1.set_xlabel("Iteration")
    ax1.set_ylabel("|f(x)|")
    ax1.legend()
    ax1.grid(True)

    # Plot 2: Logarithmisch skaliert
    ax2.semilogy(
        range(len(errors_bisect)), errors_bisect, label="Bisektion", marker="x"
    )
    ax2.semilogy(range(len(errors_newton)), errors_newton, label="Newton", marker="o")
    ax2.set_title(f"{name}: Konvergenz (Logarithmisch)")
    ax2.set_xlabel("Iteration")
    ax2.set_ylabel("|f(x)| (log)")
    ax2.legend()
    ax2.grid(True)

    plt.tight_layout()
    plt.show()

    # Interpretation
    print(f"Interpretation ({name}):")
    print(
        "Das Newton-Verfahren konvergiert quadratisch, d.h. die Anzahl der korrekten Dezimalstellen verdoppelt sich in jedem Schritt (sobald man nah genug an der Nullstelle ist)."
    )
    print(
        "Das Bisektionsverfahren konvergiert linear, d.h. der Fehler halbiert sich in jedem Schritt (ca. 1 Dezimalstelle alle 3-4 Schritte)."
    )
    print(
        "Im logarithmischen Plot ist Newton an der steil abfallenden Kurve (bis zur Maschinengenauigkeit) zu erkennen, während die Bisektion eine konstante negative Steigung hat."
    )


if __name__ == "__main__":
    # Aufgabe 4 Teil 1: f(x) = x^3 - x - 2
    def f1(x):
        return x**3 - x - 2

    def df1(x):
        return 3 * x**2 - 1

    # Intervall [1, 3] für Bisektion, Startwert 2 für Newton
    run_analysis(f1, df1, (1, 3), 2.0, "f(x) = x^3 - x - 2")

    # Aufgabe 4 Teil 2: Eigene Funktion
    # Wir nehmen g(x) = x^2 - 5 (Nullstelle bei sqrt(5) approx 2.236)
    def f2(x):
        return x**2 - 5

    def df2(x):
        return 2 * x

    # Intervall [2, 3] (f(2)=-1, f(3)=4), Startwert 2.5
    run_analysis(f2, df2, (2, 3), 2.5, "g(x) = x^2 - 5")
