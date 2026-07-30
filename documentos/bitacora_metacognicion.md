# Bitácora de Metacognición

**Estudiante:** Juan David Manrique Vasquez  
**Cédula:** 1141315057

## 1. Concepto más difícil del semestre y cómo lo superé

El concepto que más se me dificultó fue entender los ciclos y controlar sus
índices.  
Al principio no tenía claro que una lista de siete elementos termina en el
índice 6.  
Esto hacía que confundiera la cantidad de elementos con la última posición
válida.  
Lo fui entendiendo al realizar tablas de seguimiento y anotar el valor de cada
variable.  
También ejecuté ejemplos pequeños y revisé cómo cambiaban el contador y el
acumulador.  
Ahora comprendo mejor cuándo comienza y cuándo debe terminar un ciclo.

## 2. Ejemplo cotidiano de recursividad

Un ejemplo cotidiano puede ser una fila de personas que necesitan saber cuántas
personas hay.  
La primera persona le pregunta a la siguiente cuántas personas quedan detrás de
ella.  
Cada persona repite la misma pregunta a quien está a continuación.  
La última persona responde que detrás de ella no hay nadie, que sería el caso
base.  
Después, cada persona suma uno y devuelve la respuesta hacia el principio de la
fila.  
Así se obtiene el total mediante la repetición de una misma acción.

## 3. Utilidad de Python para Soporte de Sistemas

Python es útil en Soporte de Sistemas porque permite automatizar tareas
repetitivas.  
Por ejemplo, se puede crear un programa para revisar equipos, organizar datos o
generar reportes.  
Esto reduce el tiempo que un técnico tendría que dedicar a hacer el trabajo
manualmente.  
En UNINTEP podría utilizarse para leer una lista de computadores de una sala y
registrar su estado.  
También serviría para detectar cuáles equipos necesitan mantenimiento o una
actualización.  
De esta forma, el personal de soporte tendría información más ordenada.

## 4. Bug memorable y cómo lo resolví

El bug que más recuerdo es el error de índices del ejercicio de ventas.  
El programa comenzaba en el índice 1, aunque la primera posición de la lista era
la 0.  
Después intentaba llegar al índice 7, que no existía, y el programa se detenía.  
Para entenderlo escribí una tabla con el valor de `i`, `total` y `dias` en cada
iteración.  
La tabla permitió ver tanto la venta omitida como la posición que causaba el
error.  
Finalmente lo corregí usando `while`, empezando en cero y comparando con
`len(ventas)`.

## 5. Uso de inteligencia artificial en el taller

Sí tuve la tentación y utilicé inteligencia artificial como herramienta de
apoyo durante el taller.  
La usé para recibir explicaciones paso a paso, organizar el trabajo y revisar
posibles errores.  
Sin embargo, no considero suficiente copiar un resultado sin comprender cómo
funciona.  
Por eso revisé el código, seguí las variables y probé las opciones del programa.  
La sustentación me exige explicar las funciones y modificar el ciclo en vivo.  
Mi responsabilidad es estudiar el resultado y poder defender cada decisión que
aparece en el proyecto.

## 6. Pregunta personalizada: guardar los giros en un archivo `.txt`

Mi cédula termina en 57, que es un número impar.  
Por esa razón, la pregunta indicada en el taller sería qué hacer si el usuario
ingresa letras en lugar de números.  
Usaría un ciclo `while True` para repetir la solicitud hasta recibir un dato
válido.  
Dentro del ciclo intentaría convertir el texto con `int()` y controlaría el
`ValueError` mediante `try` y `except`.  
Si el usuario escribe letras, mostraría un mensaje sin cerrar el programa.  
Cuando escriba un número mayor que cero, usaría `break` y devolvería el monto
validado.
