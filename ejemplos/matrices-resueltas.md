
# Ejercicios de Matrices (Listas de Listas) en Python

Estos ejercicios están diseñados para practicar el uso de **matrices** (listas de listas) usando únicamente **estructuras básicas** de Python: ciclos, condicionales y funciones.

---

## Ejercicio 1: Monitoreo de temperatura semanal

**Contexto:**  
Una estacion meteorologica registra la temperatura de **5 ciudades** durante **7 dias**.  
Los datos se almacenan en una matriz `temperaturas` de tamaño 5x7, donde cada fila representa una ciudad y cada columna un dia de la semana (0 = lunes, 6 = domingo).

```python
temperaturas = [
    [22, 24, 23, 25, 26, 24, 22],  # Ciudad 0
    [18, 19, 20, 21, 22, 23, 21],  # Ciudad 1
    [30, 31, 29, 28, 32, 33, 34],  # Ciudad 2
    [25, 25, 24, 23, 26, 27, 25],  # Ciudad 3
    [20, 21, 22, 21, 20, 19, 18],  # Ciudad 4
]

# Funcion que calcula el promedio de temperatura por ciudad
def promedio_ciudades(temperaturas):
    promedios = []
    for ciudad in temperaturas:
        suma = 0
        for temp in ciudad:
            suma += temp
        promedio = suma / len(ciudad)
        promedios.append(promedio)
    return promedios

# Funcion que encuentra el dia y ciudad con la temperatura mas alta
def dia_mas_calido(temperaturas):
    max_temp = temperaturas[0][0]
    ciudad_max = 0
    dia_max = 0
    for i in range(len(temperaturas)):
        for j in range(len(temperaturas[i])):
            if temperaturas[i][j] > max_temp:
                max_temp = temperaturas[i][j]
                ciudad_max = i
                dia_max = j
    return (ciudad_max, dia_max)

# Pruebas
print("Promedios por ciudad:", promedio_ciudades(temperaturas))
print("Dia mas calido (ciudad, dia):", dia_mas_calido(temperaturas))
````

---

## Ejercicio 2: Control de inventario en cadena de tiendas

**Contexto:**
Una cadena de tiendas tiene **3 sucursales** y vende **4 productos**.
El stock se representa con una matriz `stock` de 3x4.

```python
stock = [
    [15, 20, 13, 5],   # Sucursal 0
    [9,  18, 25, 2],   # Sucursal 1
    [7,  30, 10, 1],   # Sucursal 2
]

# Total de productos por columna (producto)
def total_stock_por_producto(stock):
    totales = []
    for j in range(len(stock[0])):
        suma = 0
        for i in range(len(stock)):
            suma += stock[i][j]
        totales.append(suma)
    return totales

# Posiciones donde el stock es menor a un umbral
def sucursales_bajo_stock(stock, umbral):
    resultado = []
    for i in range(len(stock)):
        for j in range(len(stock[i])):
            if stock[i][j] < umbral:
                resultado.append((i, j))
    return resultado

# Pruebas
print("Stock total por producto:", total_stock_por_producto(stock))
print("Stock bajo el umbral 10:", sucursales_bajo_stock(stock, 10))
```

---

## Ejercicio 3: Analisis de calificaciones de estudiantes

**Contexto:**
Un colegio guarda las calificaciones de **4 estudiantes** en **5 asignaturas**, en una matriz `calificaciones` de 4x5.

```python
calificaciones = [
    [70, 80, 90, 85, 75],  # Estudiante 0
    [60, 65, 55, 70, 58],  # Estudiante 1
    [95, 100, 98, 97, 96], # Estudiante 2
    [40, 50, 60, 45, 55],  # Estudiante 3
]

# Promedio de cada estudiante (por fila)
def promedio_por_estudiante(calificaciones):
    promedios = []
    for estudiante in calificaciones:
        suma = 0
        for nota in estudiante:
            suma += nota
        promedio = suma / len(estudiante)
        promedios.append(promedio)
    return promedios

# Promedio de cada asignatura (por columna)
def promedio_por_asignatura(calificaciones):
    promedios = []
    for j in range(len(calificaciones[0])):
        suma = 0
        for i in range(len(calificaciones)):
            suma += calificaciones[i][j]
        promedio = suma / len(calificaciones)
        promedios.append(promedio)
    return promedios

# Estudiantes cuyo promedio es menor que el umbral
def estudiantes_desaprobados(calificaciones, umbral):
    resultado = []
    for i in range(len(calificaciones)):
        suma = 0
        for nota in calificaciones[i]:
            suma += nota
        promedio = suma / len(calificaciones[i])
        if promedio < umbral:
            resultado.append(i)
    return resultado

# Pruebas
print("Promedio por estudiante:", promedio_por_estudiante(calificaciones))
print("Promedio por asignatura:", promedio_por_asignatura(calificaciones))
print("Estudiantes desaprobados (umbral 60):", estudiantes_desaprobados(calificaciones, 60))
```
