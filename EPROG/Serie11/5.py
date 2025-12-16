import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    """Die Funktion f(x, y) = x^2 + y^2"""
    return x**2 + y**2


def E(x, y, x_prime, y_prime):
    """
    Die Tangentialebene E(x, y) im Punkt (x', y').
    E(x, y) = f(x', y') + grad(f)(x', y') * (x-x', y-y')
    grad(f) = (2x, 2y)
    """
    f_val = f(x_prime, y_prime)
    df_dx = 2 * x_prime
    df_dy = 2 * y_prime

    return f_val + df_dx * (x - x_prime) + df_dy * (y - y_prime)


def plot_function_and_tangent():
    # Gitter erstellen für den Bereich [-5, 5]
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x, y)

    # Funktionswerte berechnen
    Z_func = f(X, Y)

    # Tangentialebene im Punkt (-4, 4) berechnen
    x_p, y_p = -4, 4
    Z_tangent = E(X, Y, x_p, y_p)

    # Plotting
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection="3d")

    # Funktion f(x,y) plotten (Transparentes Blau)
    ax.plot_surface(X, Y, Z_func, cmap="viridis", alpha=0.6, label="f(x,y) = x² + y²")

    # Tangentialebene plotten (Transparentes Orange)
    ax.plot_surface(X, Y, Z_tangent, color="orange", alpha=0.4)

    # Den Berührpunkt hervorheben
    z_p = f(x_p, y_p)
    ax.scatter(
        x_p, y_p, z_p, color="red", s=100, label=f"Berührpunkt ({x_p}, {y_p}, {z_p})"
    )

    # Labels und Titel
    ax.set_title("Tangentialebene an f(x,y) = x² + y² im Punkt (-4, 4)")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")

    # Dummy-Plots für die Legende (da plot_surface nicht direkt in legend unterstützt wird)
    from matplotlib.lines import Line2D

    legend_elements = [
        Line2D([0], [0], color="blue", lw=4, label="Funktion f(x,y)"),
        Line2D([0], [0], color="orange", lw=4, alpha=0.4, label="Tangentialebene"),
        Line2D(
            [0],
            [0],
            marker="o",
            color="red",
            label="Berührpunkt",
            markersize=10,
            linestyle="None",
        ),
    ]
    ax.legend(handles=legend_elements)

    plt.show()


if __name__ == "__main__":
    plot_function_and_tangent()
