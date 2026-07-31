# Taller de Recuperación de Fundamentos de Programación

## Datos del estudiante

- Nombre: Juan David Manrique Vasquez
- Cédula: 1141315057
- Programa: Soporte de Sistemas y Redes
- Institución: UNINTEP - Roldanillo, Valle
- Usuario de GitHub: XxDavid714

## Descripción

En este repositorio presento mi taller de recuperación de Fundamentos de
Programación. Aquí se encuentra la corrección del ejercicio de ventas, el
programa del Terminal de Transportes de Roldanillo, las bitácoras, las capturas
y los videos.

## Parte 1

En el primer ejercicio encontré que el ciclo comenzaba en el índice 1 y
terminaba intentando consultar el índice 7. La lista tiene siete elementos,
pero sus índices van desde 0 hasta 6.

Para solucionarlo reescribí el ciclo usando `while`, comenzando con `i = 0` y
repitiendo mientras `i < len(ventas)`.

El resultado correcto fue:

- Total de ventas: $1.470.000
- Días con ventas: 6
- Promedio: $245.000

## Parte 2

El segundo programa permite registrar giros del Terminal de Transportes de
Roldanillo. Sus opciones son:

1. Registrar un giro.
2. Mostrar el total.
3. Listar los giros.
4. Buscar por nombre.
5. Salir.

La lista tiene 57 posiciones porque mi cédula termina en 57. También utilicé
funciones, ciclos `while`, validación de datos, búsqueda de nombres y una
función recursiva para calcular el total.

## Cómo ejecutar los programas

En la terminal se pueden ejecutar con:

```bash
py codigo/parte1_analisis.py
py codigo/parte2_terminal.py
```

## Archivos del taller

- En `codigo` están los dos programas de Python.
- En `documentos` están la tabla de seguimiento y las dos bitácoras.
- En `capturas` están las tres pruebas del programa.
- En `videos` están los dos videos de sustentación.

## Estado

El taller está terminado y todos los archivos solicitados están subidos al
repositorio.
