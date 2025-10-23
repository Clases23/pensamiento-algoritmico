# Taller de Repaso – Programación II (Condicionales, Ciclos, Listas, Matrices, Funciones)

**Reglas del taller**


* Solo **inputs** sencillos (por consola) y **prints**.
* Usar nombres de variables claros y comentar brevemente cada bloque.

---

## 1) Condicionales

### Mini‑refuerzo teórico (≈5 min)

* Estructuras: `if`, `elif`, `else`.
* Ordena condiciones de lo **más específico** a lo **más general**.
* Evita duplicar cálculos: calcula una vez y reutiliza.

### Ejercicio 1.1 — Tarifa Metro/Bus (Medellín)

**Contexto:** Según edad y si el usuario es estudiante, la tarifa cambia.
**Entradas:** `edad` (int), `es_estudiante` ("si"/"no").
**Reglas:**

* `< 5` años: gratis.
* `5–18` años: 2.500 COP.
* `> 18` y estudiante: 3.000 COP.
* `> 18` y no estudiante: 3.500 COP.
  **Salida:** imprimir la tarifa o “Gratis”.
  **Casos de prueba:**
* `3, no` → `Gratis`
* `15, si` → `2500`
* `20, si` → `3000`
* `40, no` → `3500`

### Ejercicio 1.2 — Descuento Librería Universitaria

**Entradas:** `monto` (int, COP), `tiene_carnet` ("si"/"no").
**Reglas:**

* Si `monto >= 100000`: 15% de descuento.
* Si `monto >= 50000`: 10%.
* Si además `tiene_carnet == "si"`, sumar 5% adicional.
  **Salida:** total a pagar (entero truncado hacia abajo).
  **Pruebas:**
* `120000, si` → `96000` (20%)
* `60000, no` → `54000` (10%)

### Ejercicio 1.3 — Clasificación de Nota

**Entrada:** `nota` (0.0–5.0).
**Salida:** “Bajo (<3.0)”, “Básico (3.0–3.4)”, “Alto (3.5–4.4)”, “Superior (4.5–5.0)”.
**Pruebas:** 2.9→Bajo, 3.2→Básico, 4.0→Alto, 4.7→Superior.

---

## 2) Ciclos (while / for)

### Mini‑refuerzo teórico (≈5 min)

* `while` para repetir **hasta** que una condición cambie; `for` para contar o recorrer rangos.
* Define claramente la **condición de salida**.

### Ejercicio 2.1 — Ahorro Semanal (while)

**Entradas:** `meta` (int), `ahorro_semanal` (int).
**Proceso:** simular semana a semana hasta alcanzar la meta y contar semanas.
**Salida:** semanas necesarias.
**Prueba:** meta=100000, semanal=15000 → 7 semanas.

### Ejercicio 2.2 — Conteo de Dígitos (for)

**Entrada:** número entero positivo.
**Salida:** cantidad de dígitos (sin convertir a string).
**Pista:** dividir entre 10 en un bucle hasta llegar a 0.
**Prueba:** 12345 → 5.

### Ejercicio 2.3 — Tabla de Multiplicar Formateada

**Entrada:** `n` (1–12).
**Salida:** `n x i = resultado` para i=1..10.
**Prueba:** n=4 → líneas de 4×1 a 4×10.

---

## 3) Ciclos anidados

### Mini‑refuerzo teórico (≈5 min)

* El bucle externo **controla filas** o “grupos”; el interno **detalles** o “columnas”.
* Comienza con límites pequeños para validar el orden.

### Ejercicio 3.1 — Calendario Simplificado

**Entrada:** `semanas` (int), `dias_por_semana` (int).
**Salida:** imprimir “Semana s — Día d” en orden.
**Ejemplo (2, 3):**

```
Semana 1 — Día 1
Semana 1 — Día 2
Semana 1 — Día 3
Semana 2 — Día 1
Semana 2 — Día 2
Semana 2 — Día 3
```

### Ejercicio 3.2 — Cuadrícula de Inventario

**Entrada:** `filas`, `columnas`.
**Salida:** imprimir códigos “F{f}C{c}” separados por espacio.
**Ejemplo (3,4):**

```
F1C1 F1C2 F1C3 F1C4
F2C1 F2C2 F2C3 F2C4
F3C1 F3C2 F3C3 F3C4
```

---

## 4) Listas

### Mini‑refuerzo teórico (≈5 min)

* Listas: colecciones ordenadas. Operaciones básicas: `append`, acceso por índice, actualizar elemento, `len`.
* Cuida los índices válidos: `0 <= i < len(lista)`.

### Ejercicio 4.1 — Registro de Gastos Diarios

**Entrada:** primero `n` (días). Luego leer `n` valores (enteros).
**Salida:** total gastado y promedio (entero truncado).
**Prueba:** n=4; 10000, 8000, 0, 7000 → total=25000, promedio=6250.

### Ejercicio 4.2 — Temperaturas y Alertas

**Entrada:** `n` y luego `n` temperaturas (float).
**Salida:** máxima, mínima y **cuántas** están fuera del rango 18–28.
**Prueba:** [20, 17, 28, 30] → max=30, min=17, fuera=2.

### Ejercicio 4.3 — Búsqueda de Producto

**Entrada:** `n` y luego `n` nombres (strings). Luego un `objetivo`.
**Salida:** “Encontrado en índice i” o “No encontrado”.
**Restricción:** búsqueda lineal programada por ti (sin métodos especiales).

---

## 5) Matrices (listas de listas)

### Mini‑refuerzo teórico (≈5 min)

* Una **matriz** es una lista donde **cada elemento** es otra lista, idealmente con el mismo largo.
* Recorrido típico: dos bucles (`for` anidados): por filas y por columnas.

### Ejercicio 5.1 — Ventas Trimestrales (Café 🇨🇴)

**Entradas:**

* `f` (departamentos), `c` (trimestres).
* Luego `f*c` enteros en orden por filas (toneladas).
  **Tareas:**

1. Imprimir la matriz formateada.
2. Total anual por **departamento** (por fila).
3. Total por **trimestre** (por columna).
4. ¿Qué departamento vendió más en total? (imprimir índice o nombre si lo capturas aparte).
   **Prueba pequeña:** f=2, c=3, datos:
   Fila1: 100 120 110; Fila2: 90 95 105  →

* Totales fila: [330, 290]
* Totales col: [190, 215, 215]
* Mayor fila: 0

### Ejercicio 5.2 — Ocupación de Salas

**Entrada:** `filas`, `columnas` y una matriz de 0 (libre) o 1 (ocupada).
**Salida:** porcentaje de ocupación total y por fila (entero %).
**Prueba:**

```
3 3
1 0 1
0 1 0
1 1 0
```

Ocupación total = 5/9 ≈ 55% → imprimir `55`. Por fila (aprox.): `[66, 33, 66]`.

---

## 6) Funciones

### Mini‑refuerzo teórico (≈5 min)

* Una función **recibe** datos (parámetros), **procesa** y **retorna** un resultado con `return`.
* Para probar más fácil, separa la lógica del I/O: la función procesa; el `main` lee/imprime.

### Ejercicio 6.1 — `calcular_imc(peso, estatura)`

**Reglas:** retorna el IMC `peso/(estatura^2)` y una categoría:

* `<18.5` “Bajo”, `18.5–24.9` “Normal”, `25–29.9` “Sobrepeso”, `≥30` “Obesidad”.
  **Salida (en `main`):** pedir peso y estatura, llamar la función, imprimir IMC (2 decimales) y categoría.
  **Prueba:** (70, 1.75) → 22.86, “Normal”.

### Ejercicio 6.2 — `aplicar_descuento(monto, porcentaje)`

Retorna el **nuevo** monto (entero truncado).
**Prueba:** (100000, 12) → 88000.

### Ejercicio 6.3 — `promedio_lista(lista_enteros)`

Recibe una lista y retorna el promedio (entero truncado).
**Prueba:** [10, 20, 30] → 20.

---

## 7) Integrador (todo junto)

### Proyecto — Monitoreo de Cafetería Universitaria

**Contexto:** La cafetería registra ventas por turno (mañana/tarde) y por día de la semana (L–V).

**Entradas:**

* Una matriz `ventas` de 5 filas (Lunes–Viernes) × 2 columnas (Mañana, Tarde) con enteros (COP).
* Un valor `umbral_alerta` (int).

**Tareas:**

1. **Imprimir** la matriz ordenada por días (ciclos anidados).
2. **Totales por día** (lista) y **total semanal**.
3. **Día con mayor venta total** (índice del día).
4. **Cuántos turnos** (celdas) superan el `umbral_alerta`.
5. Define y usa funciones:

   * `total_dia(fila)` → int
   * `total_semanal(matriz)` → int
   * `conteo_umbral(matriz, umbral)` → int
   * `indice_dia_mayor(matriz)` → int

**Prueba rápida:**

```
ventas =
[ [30000, 20000],  # L
  [25000, 35000],  # M
  [40000, 15000],  # X
  [20000, 20000],  # J
  [50000, 30000] ] # V
umbral_alerta = 30000
```

* Totales día: `[50000, 60000, 55000, 40000, 80000]`
* Total semanal: `285000`
* Día mayor: `4` (Viernes)
* Celdas > umbral: `4`

---

## Plantillas mínimas (guía de estructura)

> **Nota:** Son esqueletos para guiar. Completa la lógica con lo visto en clase. Todo con condicionales, `for/while`, listas y matrices.

```python
# ====== PLANTILLA PARA UN PROBLEMA CON FUNCIONES ======

def aplicar_descuento(monto, porcentaje):
    # TODO: calcular y retornar el monto con descuento (entero)
    return 0  # reemplaza

def main():
    # TODO: leer entradas (input), llamar funciones y hacer prints
    pass

if __name__ == "__main__":
    main()
```

