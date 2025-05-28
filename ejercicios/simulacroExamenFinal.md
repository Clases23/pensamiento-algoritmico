
### Pregunta 1

En un torneo de matematicas se calcula la variable `puntaje` al terminar el siguiente algoritmo. Cual sera su valor?

```pseudocode
Inicio
Algoritmo TorneoMatematicas
  Variables:
    Entero: base, extra, penalizacion, puntaje

  base = 5
  extra = 3
  penalizacion = 2
  puntaje = base + extra * 2 // 3 - penalizacion
  puntaje = puntaje + extra * (base - 2)
  Mostrar puntaje
Fin
````

* A. 12
* B. 14
* C. 16
* D. 18

---

### Pregunta 2

En un sistema de control de stock, tras cuatro ajustes automáticos, que valor toma la variable `stock`?

```pseudocode
Inicio
Algoritmo ControlStock
  Variables:
    Entero: stock, cont

  stock = 55
  cont = 0
  mientras stock > 35 hacer
    si stock mod 4 == 0 entonces
      stock = stock - 4
    sino
      stock = stock - 3
    fin si
    cont = cont + 1
    si cont == 4 entonces
      salir
    fin si
  fin mientras
  Mostrar stock
Fin
```

* A. 40
* B. 41
* C. 42
* D. 43

---

### Pregunta 3

Un programa asigna valores al vector `datos` usando una formula lineal. Cual sera su contenido al finalizar?

```pseudocode
Inicio
Algoritmo AsignarDatos
  Variables:
    Entero: i
    Vector datos(5)

  para i = 1 hasta 5 hacer
    datos(i) = i * 5 + 1
  fin para
  Mostrar datos
Fin
```

* A. 6, 11, 16, 21, 26
* B. 5, 10, 15, 20, 25
* C. 7, 12, 17, 22, 27
* D. 8, 13, 18, 23, 28

---

### Pregunta 4

Al procesar el arreglo `X` se realiza una modificacion y luego se calcula un nuevo elemento. Que valor muestra `X(3)`?

```pseudocode
Inicio
Algoritmo ActualizarX
  Variables:
    Vector X(4)
    Entero: suma

  X = [3, 6, 9, 12]
  X(1) = X(1) + 2
  suma = X(1) + X(2)
  X(3) = suma - X(4)
  Mostrar X(3)
Fin
```

* A. -1
* B. 0
* C. 1
* D. 2

---

### Pregunta 5

Se suman los primeros n numeros pares positivos. Cual sera el valor de `suma` cuando n es 4?

```pseudocode
Inicio
Algoritmo SumarPares
  Variables:
    Entero: n, x, suma, cont
  n = 4, x = 1, suma = 0, cont = 0
  mientras cont < n hacer
    si x mod 2 == 0 entonces
      suma = suma + x
      cont = cont + 1
    fin si
    x = x + 1
  fin mientras
  Mostrar suma
Fin
```

* A. 18
* B. 20
* C. 22
* D. 24

---

### Pregunta 6

El vector `V` se genera segun una condicion de paridad. Como queda al finalizar?

```pseudocode
Inicio
Algoritmo ConstruirV
  Variables:
    Entero: i
    Vector V(6)

  V(1) = 2; V(2) = 3
  para i = 3 hasta 6 hacer
    si i mod 2 == 1 entonces
      V(i) = V(i-1) + V(i-2)
    sino
      V(i) = V(i-1) * V(i-2)
    fin si
  fin para
  Mostrar V
Fin
```

* A. 2, 3, 5, 15, 20, 300
* B. 2, 3, 5, 8, 13, 21
* C. 2, 3, 6, 18, 54, 324
* D. 2, 3, 5, 10, 20, 40

---

### Pregunta 7

Cual de estas afirmaciones NO corresponde a una ventaja de la programacion modular?

* A. Facilita la depuracion de errores
* B. Obliga a duplicar codigo en cada modulo
* C. Mejora la legibilidad
* D. Permite pruebas unitarias independientes

---

### Pregunta 8

Que caracteristica tiene una variable local en un programa?

* A. Se inicializa en cero automaticamente
* B. Solo existe dentro de la funcion donde se crea
* C. Se comparte con todos los modulos
* D. Mantiene su valor despues de terminar el programa

# Enunciado.

##### **Requerimientos del ejercicio:**

- **Programación Modular**: Cada pregunta debe resolverse en una función independiente. Esto permitirá reutilizar y probar cada función por separado.

- **Formato de Salida**: Cada función debe imprimir un resultado claro y específico para facilitar la interpretación de los datos.

Una biblioteca quiere analizar los datos de sus libros más leídos en distintas áreas de conocimiento. La cantidad de veces que un libro ha sido prestado en cada área está representada en una matriz, donde cada fila representa una categoría de libros y cada columna un mes del año.

La siguiente matriz muestra la cantidad de préstamos para tres categorías de libros en los últimos cinco meses:

|             | Mes 1 | Mes 2 | Mes 3 | Mes 4 | Mes 5 |
|-------------|-------|-------|-------|-------|-------|
| **Categoría A** |  15   |   8   |  20   |   5   |  12   |
| **Categoría B** |  10   |  17   |  13   |   9   |   8   |
| **Categoría C** |   6   |  14   |   7   |  10   |   4   |

```python
matriz = [
    [15, 8, 20, 5, 12],
    [10, 17, 13, 9, 8],
    [6, 14, 7, 10, 4]
]
```

- **Categorías** representan diferentes tipos de libros en la biblioteca.
- **Meses** indican los meses de registro de préstamos en los últimos cinco meses.



**Realiza las siguientes tareas para ayudar a la biblioteca a interpretar estos datos:**

1. **Suma de préstamos en posiciones pares:** Recorre la matriz y calcula la suma de todos los valores en posiciones donde tanto el índice de fila como el de columna son pares. Muestra el resultado de esta suma para el análisis de la biblioteca.

2. **Promedio de préstamos en el último mes:** Calcula el promedio de préstamos de cada categoría en el último mes (última columna de la matriz) y muestra el resultado.

3. **Identificación del préstamo máximo y mínimo:** Encuentra el número de préstamos máximo y mínimo en toda la matriz y muestra sus posiciones. Esto permitirá a la biblioteca saber qué categoría y mes tuvieron la mayor y menor demanda.

4. **Total de préstamos por categoría:** Calcula el total de préstamos para cada categoría sumando todos los valores de cada fila. Muestra estos totales para que la biblioteca pueda evaluar la popularidad de cada categoría.