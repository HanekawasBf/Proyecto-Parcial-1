"""Calcula la pendiente (m) y el intercepto (b) de la recta y = mx + b.

    Fórmulas:
        m = (Σxy − ΣxΣy/n) / (Σx² − (Σx)²/n)
        b = ȳ − m·x̄
    """
def calcular_recta(xs, ys):
    n = len(xs)
    suma_x = sum(xs)
    suma_y = sum(ys)
    suma_xy = sum(x * y for x, y in zip(xs, ys))
    suma_x2 = sum(x ** 2 for x in xs)

    m = (suma_xy - suma_x * suma_y / n) / (suma_x2 - suma_x ** 2 / n)
    promedio_x = suma_x / n
    promedio_y = suma_y / n
    b = promedio_y - m * promedio_x
    return m, b