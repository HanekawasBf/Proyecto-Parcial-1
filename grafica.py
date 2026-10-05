import matplotlib.pyplot as plt

"""Dibuja los puntos, la recta de ajuste y muestra la ecuacion."""
def graficar(xs, ys, m, b):
    # Puntos de la recta en los extremos del rango de x
    x_min, x_max = min(xs), max(xs)
    recta_x = [x_min, x_max]
    recta_y = [m * x_min + b, m * x_max + b]

    plt.scatter(xs, ys, color="blue", label="Muestras")
    plt.plot(recta_x, recta_y, color="red",
             label=f"y = {m:.4f}x + {b:.4f}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Regresión lineal por mínimos cuadrados")
    plt.legend()
    plt.grid(True)
    plt.show()