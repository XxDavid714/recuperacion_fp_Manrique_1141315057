# Taller de Recuperación - Fundamentos de Programación

## Datos del estudiante

- **Nombre:** Juan David Manrique Vasquez
- **Cédula:** 1141315057
- **Programa:** Soporte de Sistemas y Redes
- **Institución:** UNINTEP - Roldanillo, Valle
- **Usuario de GitHub:** XxDavid714

## Descripción

Este repositorio contiene el desarrollo del Taller de Recuperación de
Fundamentos de Programación en Python. El trabajo incluye el análisis de un
error de índices, un programa para registrar giros del Terminal de Transportes
de Roldanillo, las bitácoras solicitadas y el material de sustentación.

## Estructura

```text
recuperacion_fp_Manrique_1141315057/
├── README.md
├── codigo/
│   ├── parte1_analisis.py
│   └── parte2_terminal.py
├── documentos/
│   ├── tabla_seguimiento.md
│   ├── bitacora_errores.md
│   └── bitacora_metacognicion.md
├── capturas/
│   ├── ejecucion_1.png
│   ├── ejecucion_2.png
│   └── ejecucion_3.png
├── videos/
│   ├── sustentacion_codigo.mp4
│   └── modificacion_en_vivo.mp4
└── .gitignore
```

## Parte 1: análisis y depuración

El código original utiliza `range(1, 8)` para recorrer una lista de siete
elementos. Esto omite el índice 0 e intenta acceder al índice 7, que no existe.
La solución comienza en cero y utiliza la condición `i < len(ventas)`.

El programa corregido obtiene estos resultados:

- Total de ventas positivas: **$1.470.000**
- Días con ventas: **6**
- Promedio de ventas: **$245.000**

## Parte 2: programa del terminal

El programa permite:

1. Registrar un giro.
2. Mostrar el total de los giros mediante recursividad.
3. Listar los giros registrados.
4. Buscar giros por nombre.
5. Salir.

La lista tiene **57 posiciones**, de acuerdo con los dos últimos dígitos de la
cédula. El código también incluye un menú con `while`, validación con
`while True` y `break`, funciones, búsqueda de texto y comentarios en español.

## Ejecución

Desde la carpeta principal del repositorio:

```bash
python codigo/parte1_analisis.py
python codigo/parte2_terminal.py
```

## Evidencias de ejecución y sustentación

El repositorio contiene las tres capturas de ejecución solicitadas y los dos
videos de sustentación grabados por el estudiante con cámara encendida y
pantalla compartida.

## Estado

Proyecto terminado con código, documentos, capturas y videos de sustentación.
