# Regresión lineal por mínimos cuadrados

Programa en Python que lee muestras (x, y) desde un archivo CSV, calcula la recta de ajuste `y = mx + b` y la grafica junto con los puntos.

Proyecto del Parcial 1 de Ciencia de Datos.

## Fórmulas

```
m = (Σxy − ΣxΣy/n) / (Σx² − (Σx)²/n)
b = ȳ − m·x̄
```

Para usar otros datos, solo hay que reemplazar el contenido de `datos.csv`.
