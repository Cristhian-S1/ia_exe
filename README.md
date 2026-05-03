# IQ Digits Solver — CP-SAT + NumPy

Solver automático para el puzzle **IQ Digits** usando programación por restricciones (OR-Tools CP-SAT). Coloca los 10 dígitos del 0 al 9 (representados con segmentos estilo 7 segmentos) sobre un tablero de 4×5 celdas, respetando restricciones de posición, orientación y pistas de suma.

---

## Descripción del problema

El tablero tiene **49 aristas** (25 horizontales + 24 verticales). Cada dígito ocupa un subconjunto de esas aristas según su forma de 7 segmentos:

| Dígito | Segmentos | Aristas |
|--------|-----------|---------|
| 0 | cuadrado 1×1 | 4 |
| 1 | b, c | 2 |
| 2 | a, b, g, e, d | 5 |
| 3 | a, b, g, c, d | 5 |
| 4 | f, b, g, c | 4 |
| 5 | a, f, g, c, d | 5 |
| 6 | a, f, g, e, c, d | 6 |
| 7 | a, b, c | 3 |
| 8 | todos | 7 |
| 9 | a, f, b, g, c, d | 6 |

Total: **47 aristas** usadas, 2 quedan libres.

Cada pieza puede colocarse en **8 orientaciones** (4 rotaciones × 2 reflejos).

---

## Requisitos

- Python 3.8+
- [OR-Tools](https://developers.google.com/optimization/install) — `pip install ortools`
- [NumPy](https://numpy.org/) — `pip install numpy`

---

## Instalación

```bash
git clone https://github.com/tu-usuario/iq-digits-solver.git
cd iq-digits-solver
pip install ortools numpy
```

---

## Uso

```bash
python main.py
```

El programa presenta un menú interactivo con las siguientes opciones:

```
═════════════════════════════════════════════
         IQ Digits — Solver CP-SAT
═════════════════════════════════════════════
1) Resolver con piezas fijas
2) Resolver con pistas por celda
3) Resolver combinando fijas + pistas
4) Mostrar tablero (referencia de posiciones)
5) Salir
```

### Opción 1 — Piezas fijas

Permite fijar uno o más dígitos en una posición y orientación específica antes de resolver.

Ejemplo de entrada:
```
Dígito (0-9): 8
  Disposición (0-7): 0
  Fila columna: 0 0
```

### Opción 2 — Pistas por celda

Restringe la suma de las 4 aristas que rodean una celda a un valor dado.

Ejemplo de entrada:
```
Fila columna suma: 1 2 15
```

### Opción 3 — Combinado

Combinación de piezas fijas y pistas por celda en una sola resolución.

---

## Referencia del tablero

### Grilla de posiciones (corners)

```
         c=0    c=1    c=2    c=3    c=4    c=5
  f=0   (0,0)──(0,1)──(0,2)──(0,3)──(0,4)──(0,5)
           │     │     │     │     │     │
  f=1   (1,0)──(1,1)──(1,2)──(1,3)──(1,4)──(1,5)
           │     │     │     │     │     │
  f=2   (2,0)──(2,1)──(2,2)──(2,3)──(2,4)──(2,5)
           │     │     │     │     │     │
  f=3   (3,0)──(3,1)──(3,2)──(3,3)──(3,4)──(3,5)
           │     │     │     │     │     │
  f=4   (4,0)──(4,1)──(4,2)──(4,3)──(4,4)──(4,5)
```

### Celdas (para pistas de suma)

```
         c=0    c=1    c=2    c=3    c=4
  f=0   [0,0]  [0,1]  [0,2]  [0,3]  [0,4]
  f=1   [1,0]  [1,1]  [1,2]  [1,3]  [1,4]
  f=2   [2,0]  [2,1]  [2,2]  [2,3]  [2,4]
  f=3   [3,0]  [3,1]  [3,2]  [3,3]  [3,4]
```

### Orientaciones

```
  0 = original            4 = reflejo + original
  1 = rot 90° CCW         5 = reflejo + rot 90°
  2 = rot 180°            6 = reflejo + rot 180°
  3 = rot 270° CCW        7 = reflejo + rot 270°
```

---

## Salida

Si se encuentra solución, el solver imprime tres vistas:

1. **Aristas horizontales** (matriz 5×5) — valor del dígito en cada arista, o `-1` si está vacía.
2. **Aristas verticales** (matriz 4×6) — ídem para aristas verticales.
3. **Tablero visual** — representación ASCII del tablero completo con `·` para aristas libres y `+` en las esquinas.

Ejemplo de tablero resuelto:
```
+ 3 + · + 2 + · + · +
3 · 3 2 · 2 · · · · ·
+ 3 + 2 + 2 + · + · +
· · · 2 2 2 · · · · ·
+ · + 2 + · + · + · +
```

Si no existe solución: `❌ No hay solución para esta configuración.`

---

## Arquitectura

| Componente | Descripción |
|------------|-------------|
| `D` | Plantillas de cada dígito en grilla unificada (par=arista, impar=segmento) |
| `build_placements()` | Genera todas las colocaciones válidas para cada dígito en las 8 orientaciones |
| `solve()` | Construye y resuelve el modelo CP-SAT |
| `display_solution()` | Visualiza la solución en consola |
| `e_idx(i, j)` | Convierte coordenadas de grilla unificada a índice lineal de arista |

---

## Detalles del modelo CP-SAT

- **Variables:** `x[d][i]` booleana — 1 si se usa la colocación `i` del dígito `d`.
- **Restricción de unicidad:** cada dígito aparece exactamente una vez (`AddExactlyOne`).
- **Restricción de no solapamiento:** cada arista es cubierta por a lo sumo un dígito.
- **Restricción de pista:** la suma de los valores en las 4 aristas de una celda iguala el objetivo.
- **Workers:** el solver utiliza 8 workers en paralelo para mayor velocidad.

---

## Licencia

MIT
