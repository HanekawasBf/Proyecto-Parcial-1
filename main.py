""" 
Nombre: Ortega Plaza Diego
Cuatrimestre:7mo
Carrera :Ing. Desarrollo de Software
Matricula: 2403230009
"""

from lectura_datos import leer_muestras
from calculo import calcular_recta
from grafica import graficar


def main():
    xs, ys = leer_muestras("datos.csv")
    m, b = calcular_recta(xs, ys)
    print(f"Ecuación de la recta: y = {m:.4f}x + {b:.4f}")
    graficar(xs, ys, m, b)


if __name__ == "__main__":
    main()