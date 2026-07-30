# Bitácora de Errores

**Estudiante:** Juan David Manrique Vasquez  
**Cédula:** 1141315057

## Bug 1: recorrido incorrecto de la lista de ventas

- **¿Qué intentaba hacer?** Recorrer las ventas de los siete días para calcular
  el promedio.
- **¿Qué error apareció?** Apareció `IndexError: list index out of range`
  cuando el ciclo intentó consultar `ventas[7]`. Además, la venta ubicada en
  `ventas[0]` no estaba siendo incluida.
- **¿Cómo lo solucionó?** Cambié el recorrido por un ciclo `while` que comienza
  con `i = 0` y continúa mientras `i < len(ventas)`.
- **¿Cuánto tiempo le tomó?** Aproximadamente 15 minutos entre seguir los
  valores manualmente, identificar el índice incorrecto y probar la solución.

## Bug 2: el programa aceptaba un monto negativo

- **¿Qué intentaba hacer?** Validar que el usuario escribiera un monto numérico
  antes de registrar un giro.
- **¿Qué error apareció?** La primera validación convertía correctamente el
  texto a entero, pero también aceptaba valores como `-5000`.
- **¿Cómo lo solucionó?** Agregué la condición `monto > 0`. Si no se cumple, el
  ciclo vuelve a pedir el dato y muestra un mensaje claro.
- **¿Cuánto tiempo le tomó?** Cerca de 10 minutos, incluyendo pruebas con cero,
  números negativos, letras y un monto válido.

## Bug 3: la búsqueda fallaba por mayúsculas o espacios

- **¿Qué intentaba hacer?** Buscar los giros registrados usando el nombre del
  destinatario.
- **¿Qué error apareció?** Una búsqueda como `juan` no encontraba un registro
  guardado como `Juan`, y un espacio accidental también impedía la
  coincidencia.
- **¿Cómo lo solucionó?** Apliqué `.strip()` al dato ingresado y `.lower()` al
  texto buscado y al nombre almacenado. También utilicé `in` para permitir
  coincidencias parciales.
- **¿Cuánto tiempo le tomó?** Aproximadamente 10 minutos para detectar el
  problema y comprobar búsquedas con diferentes combinaciones.
