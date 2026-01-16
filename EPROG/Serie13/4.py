import sympy as sp


def find_polynomial_p(a_val=0, b_val=1):
    x = sp.symbols('x')
    a, b = sp.symbols('a b')

    # p(x) als Polynom 3. Grades mit unbekannten Koeffizienten c_i
    c = sp.symbols('c0:4')
    p = sum(c[i] * x**i for i in range(4))

    # Test-Basis für q(x): {1, x, x^2, x^3}
    # Wenn die Eigenschaft für die Basis gilt, gilt sie für alle q(x) Grad 3
    equations = []
    for deg in range(4):
        q = x**deg
        lhs = sp.integrate(p * q, (x, a, b))
        rhs = q.subs(x, b)
        equations.append(lhs - rhs)

    # System lösen
    solutions = sp.solve(equations, c)
    p_final = p.subs(solutions)

    # Konkrete Werte einsetzen (falls gewünscht)
    return p_final.subs({a: a_val, b: b_val})


# Beispiel für das Intervall (0, 1)
p_01 = find_polynomial_p(0, 1)
print(f"Das gesuchte Polynom p(x) für (0,1) ist: {sp.simplify(p_01)}")

# Bonus: Beweis der Eindeutigkeit
# Da das Integral ein Skalarprodukt auf dem Raum der Polynome definiert,
# handelt es sich bei p(x) um den Repräsentanten des linearen Funktionals
# L(q) = q(b) nach dem Darstellungssatz von Riesz. In einem endlich-
# dimensionalen Hilbertraum ist dieser Repräsentant eindeutig.
