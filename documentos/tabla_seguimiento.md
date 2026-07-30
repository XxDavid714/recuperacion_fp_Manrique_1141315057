# Tabla de Seguimiento

**Estudiante:** Juan David Manrique Vasquez  
**Cédula:** 1141315057

La siguiente tabla muestra el comportamiento del ciclo original hasta que se
produce el error. El valor de `total` solamente cambia cuando la venta es mayor
que cero.

| Iteración | i | ventas[i] | total | dias |
|---:|---:|---:|---:|---:|
| 1 | 1 | 200000 | 200000 | 1 |
| 2 | 2 | 0 | 200000 | 1 |
| 3 | 3 | 350000 | 550000 | 2 |
| 4 | 4 | 400000 | 950000 | 3 |
| 5 | 5 | 120000 | 1070000 | 4 |
| 6 | 6 | 250000 | 1320000 | 5 |
| 7 | 7 | Error: índice fuera de rango | 1320000 | 5 |

## Error identificado

La lista `ventas` tiene siete elementos, pero sus posiciones válidas van desde
el índice 0 hasta el índice 6. El ciclo `range(1, 8)` empieza en 1, por lo que
omite la primera venta de 150000, y termina intentando consultar `ventas[7]`,
posición que no existe. Esto provoca un error `IndexError`.

La solución consiste en comenzar con `i = 0` y repetir el ciclo mientras `i`
sea menor que `len(ventas)`. De esta manera se recorren exactamente todas las
posiciones válidas de la lista. El resultado corregido es un total de 1470000
en seis días con ventas, para un promedio de 245000.

## Ciclo reescrito con while

```python
ventas = [150000, 200000, 0, 350000, 400000, 120000, 250000]

total = 0
dias = 0
i = 0

while i < len(ventas):
    if ventas[i] > 0:
        total = total + ventas[i]
        dias = dias + 1

    i = i + 1

promedio = total / dias

print("El promedio de ventas es:", promedio)
```
