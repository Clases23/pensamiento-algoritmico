
# Ejercicios de Matrices en Python

## Ejercicio 1: Monitoreo de temperatura semanal  
**Contexto:**  
Una estación meteorológica registra la temperatura de **5 ciudades** durante **7 días**. Los datos se almacenan en una matriz `temperaturas` de tamaño 5×7, donde cada fila es una ciudad y cada columna un día de la semana (0 = lunes, 6 = domingo).

**Puntos a resolver:**  
1. Define la función `promedio_ciudades(temperaturas)` que calcule y retorne una lista de 5 promedios, uno por cada ciudad.  
2. Define la función `dia_mas_calido(temperaturas)` que busque la temperatura máxima en toda la matriz y devuelva una tupla `(indice_ciudad, indice_dia)` correspondientes.  

---

## Ejercicio 2: Control de inventario en cadena de tiendas  
**Contexto:**  
Una cadena de retail tiene **3 sucursales** y vende **4 productos**. El stock disponible en cada sucursal se guarda en una matriz `stock` 3×4 (filas = sucursales, columnas = productos).

**Puntos a resolver:**  
1. Crea la función `total_stock_por_producto(stock)` que reciba la matriz y devuelva una lista de 4 elementos, donde cada elemento es la suma del stock de ese producto en las 3 sucursales.  
2. Crea la función `sucursales_bajo_stock(stock, umbral)` que, dado un valor entero `umbral`, retorne una lista de tuplas `(indice_sucursal, indice_producto)` para todos los casos donde el stock sea inferior al umbral.  

---

## Ejercicio 3: Análisis de calificaciones de estudiantes  
**Contexto:**  
Un colegio registra las calificaciones de **4 estudiantes** en **5 asignaturas**. Los datos se almacenan en una matriz `calificaciones` 4×5 (filas = estudiantes, columnas = asignaturas), con valores entre 0 y 100.

**Puntos a resolver:**  
1. Define la función `promedio_por_estudiante(calificaciones)` que retorne una lista de 4 promedios, uno por cada estudiante.  
2. Define la función `promedio_por_asignatura(calificaciones)` que retorne una lista de 5 promedios, uno por cada asignatura.  
3. Define la función `estudiantes_desaprobados(calificaciones, umbral)` que, dado un umbral (por ejemplo, 60), retorne una lista de índices de estudiantes cuya nota promedio sea menor al umbral.  

