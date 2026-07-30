"""Corrección del ejercicio de ventas de la Tienda Doña María."""

# Lista original con las ventas registradas durante siete días.
ventas = [150000, 200000, 0, 350000, 400000, 120000, 250000]

total = 0
dias = 0
i = 0

# Se inicia en cero y se usa la longitud de la lista como límite.
# Así se visitan todos los índices válidos, desde 0 hasta 6.
while i < len(ventas):
    # Los días sin ventas no se incluyen para calcular el promedio.
    if ventas[i] > 0:
        total = total + ventas[i]
        dias = dias + 1

    i = i + 1

# La lista contiene ventas positivas, por eso dias es mayor que cero.
promedio = total / dias

print("El total de ventas es:", total)
print("La cantidad de días con ventas es:", dias)
print("El promedio de ventas es:", promedio)
