
# Listas y Matrices en Python

Las **listas** son una estructura de datos fundamental en Python que permite almacenar múltiples valores en una sola variable. A lo largo de estas notas exploraremos qué son las listas, cómo utilizarlas y manipularlas, y cómo trabajar con listas anidadas (matrices). Cada sección incluye ejemplos prácticos en código Python y ejercicios recomendados para reforzar el aprendizaje.

## Que son las listas

Una **lista** en Python es una colección **ordenada** de elementos. Esto significa que cada elemento ocupa una posición (índice) específica dentro de la lista, y ese orden se mantiene. Las listas pueden contener elementos de **cualquier tipo de dato**: números, cadenas de texto, booleanos, e incluso otras listas. A diferencia de algunos tipos de datos más simples, las listas son **mutables**, lo que significa que se pueden modificar después de creadas (podemos agregar, cambiar o eliminar elementos). También son **dinámicas**, ya que su tamaño puede cambiar durante la ejecución del programa.

**Características principales de las listas:**

* **Ordenadas:** Mantienen el orden en el que se agregan los elementos.
* **Indexadas:** Cada elemento se accede mediante un índice entero, comenzando desde 0.
* **Heterogéneas:** Pueden contener datos de diferentes tipos (ejemplo: enteros, strings, etc.).
* **Mutables:** Sus elementos se pueden modificar, añadir o eliminar en cualquier momento.
* **Dinámicas:** Pueden crecer o encoger al agregar o quitar elementos.
* **Anidables:** Una lista puede contener otras listas como elementos (lo que permite crear estructuras en 2D, como matrices, que veremos más adelante).

**Ejemplo:** A continuación se muestra una lista que contiene tres tipos de datos distintos (entero, cadena y booleano) en orden:

```python
mi_lista = [10, "Hola", True]
print(mi_lista)  # Imprime: [10, "Hola", True]
```

En este ejemplo, `mi_lista` es una lista con tres elementos. El primer elemento es `10` (entero), el segundo es `"Hola"` (cadena de texto), y el tercero es `True` (booleano).

### Ejercicios

* Crea una lista llamada `frutas` que contenga el nombre de 3 frutas de tu preferencia. Imprime la lista completa.
* Crea una lista llamada `mix` que contenga un entero, una cadena y un valor booleano (por ejemplo: `5`, `"hola"`, `False`). Imprime la lista para verificar su contenido.
* Piensa en 5 cosas que llevas en tu mochila y almacenalas en una lista llamada `mochila`. Luego imprime los elementos de `mochila` uno por uno (puedes hacerlo usando múltiples `print` o más adelante mediante un bucle).

## Como se crean las listas

Existen varias formas de **crear listas** en Python. La manera más común es usando corchetes `[]` y separando los elementos por comas. También es posible crear una lista vacía (sin elementos) o convertir otros objetos en listas usando la función `list()`.

* **Lista vacía:** Se puede crear una lista vacía con `[]` o con `list()`. Por ejemplo:

  ```python
  lista_vacia1 = []
  lista_vacia2 = list()
  print(lista_vacia1)  # Imprime: []
  print(lista_vacia2)  # Imprime: []
  ```

  Ambas formas crean una lista sin elementos. Las listas vacías son útiles para luego ir agregando elementos dinámicamente.

* **Lista con valores iniciales:** Para crear una lista con valores predefinidos, escribimos los elementos dentro de los corchetes, separados por comas. Por ejemplo:

  ```python
  numeros = [1, 2, 3, 4, 5]
  palabras = ["hola", "mundo"]
  mixto = [42, "respuesta", 3.14, False]
  print(numeros)   # Imprime: [1, 2, 3, 4, 5]
  print(palabras)  # Imprime: ["hola", "mundo"]
  print(mixto)     # Imprime: [42, "respuesta", 3.14, False]
  ```

  En estos ejemplos, `numeros` es una lista de enteros, `palabras` es una lista de cadenas de texto, y `mixto` contiene diferentes tipos de datos.

* **Usando la función `list()`:** La función incorporada `list(iterable)` permite crear una lista a partir de otro iterable (como otra lista, una tupla, un rango, o una cadena de texto). Por ejemplo, podemos convertir una cadena en lista de caracteres, o un rango de números en una lista:

  ```python
  lista_desde_cadena = list("Python")
  lista_desde_rango = list(range(5))
  print(lista_desde_cadena)  # Imprime: ['P', 'y', 't', 'h', 'o', 'n']
  print(lista_desde_rango)   # Imprime: [0, 1, 2, 3, 4]
  ```

  En el primer caso, la cadena `"Python"` se convirtió en `['P', 'y', 't', 'h', 'o', 'n']`, una lista de caracteres. En el segundo caso, `range(5)` (que genera la secuencia 0,1,2,3,4) se convirtió en `[0, 1, 2, 3, 4]`.

### Ejercicios

* Crea una lista vacía llamada `lista_temporal` y luego agrega manualmente (usando `append`, que veremos más adelante, o inicializando de nuevo) tres valores: tu color favorito, tu número favorito y tu ciudad favorita. Imprime la lista resultante.
* Crea una lista llamada `pares` usando `list(range(...))` que contenga los números pares del 0 al 10 (usa la función `range` para generar los números y conviértela en lista). Imprime la lista `pares`.
* Escribe una lista en una sola línea que contenga los días de la semana. Asignala a una variable `dias` y luego muestra el primer y el ultimo día (utiliza índices, que aprenderemos en la siguiente sección, para acceder a esos elementos).

## Indices en las listas (positivos y negativos)

Cada elemento de una lista tiene una posición asociada llamada **índice**. En Python (y muchos lenguajes), los índices comienzan en `0` para el primer elemento. Veamos un ejemplo de lista y sus índices:

```python
#            0        1        2        3        4   <- indices positivos
#           -5       -4       -3       -2       -1   <- indices negativos
valores = ["a", "b", "c", "d", "e"]
```

En la lista `valores`:

* Índice `0` corresponde a `"a"` (primer elemento).
* Índice `1` corresponde a `"b"` (segundo elemento).
* ... y así sucesivamente.
* Índice `4` corresponde a `"e"` (quinto elemento, ya que la lista tiene longitud 5).
* Índice `-1` corresponde a `"e"` también (último elemento usando índice negativo).
* Índice `-2` corresponde a `"d"` (penúltimo elemento), índice `-5` corresponde a `"a"` (primer elemento, usando negativo equivalente a -len(lista)).

**Índices positivos:** Se cuentan desde el inicio de la lista, comenzando en 0. El último índice positivo es `len(lista) - 1` (ya que `len(lista)` da la longitud de la lista). Por ejemplo, si una lista tiene 5 elementos, sus índices positivos van de 0 a 4.

**Índices negativos:** Se cuentan desde el final de la lista, comenzando en -1 para el último elemento. El índice -1 es el último elemento, -2 el penúltimo, y así sucesivamente. Usar índices negativos es útil para acceder a elementos finales sin tener que saber exactamente la longitud de la lista.

Veamos algunos accesos a elementos por índice en la práctica:

```python
letras = ["a", "b", "c", "d", "e"]
print(letras[0])   # Imprime: a  (primer elemento)
print(letras[2])   # Imprime: c  (tercer elemento, indices empiezan en 0)
print(letras[4])   # Imprime: e  (quinto elemento, indice 4)
print(letras[-1])  # Imprime: e  (ultimo elemento con indice negativo)
print(letras[-3])  # Imprime: c  (tercer desde el final)
```

En el ejemplo anterior, observamos cómo usar índices positivos y negativos para obtener diferentes elementos de la lista `letras`.

**¡Cuidado!:** Si intentas acceder a un índice que no existe en la lista (por ejemplo `letras[5]` en la lista anterior, que solo tiene índices 0 a 4), Python producirá un error de tipo `IndexError` indicando que el índice está fuera de rango (*"list index out of range"*). Por lo tanto, siempre asegúrate de usar índices válidos entre `0` y `len(lista)-1` (o los negativos correspondientes que existan).

### Ejercicios

* Dada la lista `animales = ["gato", "perro", "pajaro", "pez", "hamster"]`, imprime el primer y el ultimo elemento usando índices positivos. Luego imprime el ultimo elemento usando un índice negativo.
* Crea una lista de al menos 5 elementos a tu elección y muestra por pantalla el elemento en la posición 2 y el elemento en la posición -2 (tercer elemento y penúltimo elemento de la lista, respectivamente).
* ¿Qué sucede si intentas acceder al índice 10 de una lista que tiene solo 5 elementos? (Puedes probar en un intérprete de Python para ver el mensaje de error). Escribe brevemente la razón del error como comentario en tu código de prueba.

## Acceso, modificacion y eliminacion de elementos

Ya hemos visto cómo acceder a un elemento específico de una lista usando su índice (por ejemplo `mi_lista[0]`). Además de acceder, podemos **modificar** el valor de un elemento existente o **eliminar** elementos de la lista.

### Acceder a elementos

Para **acceder** a un elemento, simplemente usamos `nombre_lista[indice]`. Esto devuelve el valor almacenado en esa posición de la lista. Por ejemplo:

```python
nombres = ["Ana", "Juan", "Carlos"]
primero = nombres[0]   # "Ana"
segundo = nombres[1]   # "Juan"
ultimo = nombres[-1]   # "Carlos" (ultimo elemento)
print(primero, segundo, ultimo)  # Imprime: Ana Juan Carlos
```

### Modificar elementos

Las listas son mutables, lo que significa que podemos cambiar el valor de un elemento existente. Para ello, accedemos al elemento por índice y le asignamos un nuevo valor con el operador de asignación (`=`):

```python
numeros = [10, 20, 30]
numeros[1] = 99        # Cambiamos el segundo elemento (indice 1) de 20 a 99
print(numeros)         # Imprime: [10, 99, 30]
numeros[-1] = 5        # Cambiamos el ultimo elemento de 30 a 5 usando indice negativo
print(numeros)         # Imprime: [10, 99, 5]
```

En este ejemplo, la lista inicial `numeros` es `[10, 20, 30]`. Después de `numeros[1] = 99`, la lista se convierte en `[10, 99, 30]` (el elemento en índice 1, originalmente 20, ahora es 99). Luego, `numeros[-1] = 5` cambia el último elemento (30) a 5, resultando en `[10, 99, 5]`.

### Eliminar elementos

Para **eliminar** uno o más elementos de una lista, podemos usar la instrucción `del` (abreviatura de "delete" en inglés). Existen diferentes formas de utilizar `del`:

* `del lista[indice]` elimina el elemento en la posición especificada.
* `del lista[inicio:fin]` elimina una sección (slice) de la lista, desde el índice `inicio` hasta `fin-1`.
* `del lista` eliminaría la lista completa (menos común, solo se usa si queremos borrar la variable entera).

Por ahora, enfoquémonos en eliminar elementos individuales por índice:

```python
letras = ["x", "y", "z", "w"]
del letras[2]      
print(letras)      # Imprime: ["x", "y", "w"]
```

En este ejemplo, `letras` inicialmente es `["x", "y", "z", "w"]`. Después de `del letras[2]`, el elemento en el índice 2 (que era `"z"`) se elimina de la lista. La lista resultante es `["x", "y", "w"]`, y los elementos posteriores al eliminado se desplazan una posición hacia la izquierda para llenar el hueco.

También podemos usar `del` con índices negativos del mismo modo para eliminar, por ejemplo, el último elemento:

```python
numeros = [5, 6, 7, 8]
del numeros[-1]    
print(numeros)     # Imprime: [5, 6, 7]
```

Aquí eliminamos el elemento con índice `-1` (último elemento, el `8`), quedando la lista con `[5, 6, 7]`.

Más adelante veremos métodos como `remove()` y `pop()` que también eliminan elementos (por valor o por índice, respectivamente). La diferencia es que esos son métodos de la lista, mientras `del` es una instrucción del lenguaje.

### Ejercicios

* Dada la lista `puntos = [10, 20, 30, 40, 50]`, realiza las siguientes operaciones en orden:

  1. Cambia el segundo elemento (`20`) por `25`.
  2. Cambia el último elemento (`50`) por `55` usando un índice negativo.
  3. Elimina el primer elemento de la lista.
  4. Imprime la lista resultante.
* Crea una lista con los nombres de tus 5 películas favoritas. Luego:

  * Reemplaza la película en la posición 3 por otra distinta.
  * Elimina la última película de la lista.
  * Muestra la lista modificada.
* Escribe un programa corto que tome una lista predefinida, elimine el elemento central (por ejemplo, si la lista tiene 5 elementos, eliminar el de índice 2) usando `del`, e imprima la lista resultante.

## Metodos comunes de listas

Python proporciona muchos **métodos** incorporados para facilitar el trabajo con listas. Los métodos son funciones asociadas a las listas que se llaman con la sintaxis `lista.metodo(argumentos)`. A continuación se describen los métodos más comunes y útiles para manipular listas, junto con ejemplos prácticos de uso:

### append()

Agrega un elemento al **final** de la lista. Este método aumenta la longitud de la lista en 1.

* **Uso:** `mi_lista.append(x)`
* **Descripción:** Añade el elemento `x` como último elemento de `mi_lista`.
* **Retorno:** No devuelve nada útil (devuelve `None` internamente); simplemente modifica la lista existente.

**Ejemplo:**

```python
# Lista inicial
numeros = [1, 2, 3]
# Agregar un elemento al final
numeros.append(4)
print(numeros)  # Imprime: [1, 2, 3, 4]
# Podemos agregar distintos tipos de datos
numeros.append("cinco")
print(numeros)  # Imprime: [1, 2, 3, 4, "cinco"]
```

En el ejemplo, empezamos con `numeros = [1, 2, 3]`. Tras `numeros.append(4)`, la lista pasa a ser `[1, 2, 3, 4]`. Luego añadimos la cadena `"cinco"` al final, resultando `[1, 2, 3, 4, "cinco"]`.

### insert()

Inserta un elemento en una posición específica de la lista, desplazando los demás elementos a la derecha.

* **Uso:** `mi_lista.insert(indice, x)`
* **Descripción:** Inserta el valor `x` en la posición dada por `indice`. Los elementos a partir de esa posición se mueven una posición hacia la derecha. Si `indice` es 0, el elemento se inserta al inicio. Si `indice` es igual al tamaño de la lista, el elemento se agrega al final (comportamiento similar a append).
* **Retorno:** No devuelve nada (modifica la lista en sitio).

**Ejemplo:**

```python
letras = ["A", "B", "D", "E"]
# Insertar "C" en la posicion 2 (tercer lugar, indices empiezan en 0)
letras.insert(2, "C")
print(letras)  # Imprime: ["A", "B", "C", "D", "E"]
# Insertar "X" al inicio (posicion 0)
letras.insert(0, "X")
print(letras)  # Imprime: ["X", "A", "B", "C", "D", "E"]
```

Aquí, la lista `letras` comienza como `["A", "B", "D", "E"]`. Después de `letras.insert(2, "C")`, la `"C"` se inserta antes de la posición 2, resultando `["A", "B", "C", "D", "E"]`. Luego `letras.insert(0, "X")` inserta `"X"` al inicio, desplazando todo lo demás a la derecha.

### pop()

Elimina un elemento de la lista **por índice** y lo devuelve. Si no se especifica índice, `pop()` quita y devuelve el último elemento.

* **Uso:** `mi_lista.pop(indice)` o simplemente `mi_lista.pop()` para el último.
* **Descripción:** Remueve el elemento en la posición `indice` de la lista y lo retorna como resultado. Si no se proporciona `indice`, se asume el último elemento (`-1`).
* **Retorno:** Devuelve el elemento eliminado de la lista.

**Ejemplo:**

```python
frutas = ["manzana", "banana", "cereza", "durazno"]
# Remover y obtener el ultimo elemento
ultima = frutas.pop()  
print(ultima)   # Imprime: durazno
print(frutas)   # Imprime: ["manzana", "banana", "cereza"]
# Remover y obtener el elemento en indice 1
segundo = frutas.pop(1)
print(segundo)  # Imprime: banana
print(frutas)   # Imprime: ["manzana", "cereza"]
```

En el ejemplo, `frutas.pop()` quita `"durazno"` (último elemento) de la lista y lo almacena en `ultima`. Después, `frutas` queda con tres elementos. Luego `frutas.pop(1)` quita el elemento de índice 1 (que era `"banana"`) y lo almacena en `segundo`. La lista final queda como `["manzana", "cereza"]`.

**Nota:** Si se intenta hacer `pop()` en una lista vacía o con un índice fuera del rango, se producirá un error.

### remove()

Elimina la **primera ocurrencia** de un valor específico en la lista.

* **Uso:** `mi_lista.remove(x)`
* **Descripción:** Busca el valor `x` en la lista y elimina la primera vez que aparece. Si el valor `x` no está en la lista, ocurre un error (`ValueError`).
* **Retorno:** Ninguno (solo modifica la lista).

**Ejemplo:**

```python
numeros = [10, 20, 30, 20, 40]
numeros.remove(20)
print(numeros)  # Imprime: [10, 30, 20, 40]
numeros.remove(20)
print(numeros)  # Imprime: [10, 30, 40]
```

Inicialmente `numeros` es `[10, 20, 30, 20, 40]`. La primera llamada `numeros.remove(20)` elimina la primera aparición de `20` (la que está en índice 1). La lista resulta `[10, 30, 20, 40]`. La segunda llamada elimina la siguiente aparición de `20` (ahora en índice 2 después del ajuste), quedando `[10, 30, 40]`. Si llamáramos `numeros.remove(50)` en ese momento, obtendríamos un error porque `50` no está en la lista.

### sort()

Ordena los elementos de la lista en orden ascendente de forma **in situ** (la lista es modificada directamente).

* **Uso:** `mi_lista.sort()`
* **Descripción:** Ordena la lista de menor a mayor. Por defecto, los números se ordenan de menor a mayor y las cadenas en orden alfabético (lexicográfico). Este método modifica la lista original.
* **Retorno:** Ninguno (devuelve `None`).

**Ejemplo:**

```python
numeros = [3, 1, 4, 2, 5]
numeros.sort()
print(numeros)  # Imprime: [1, 2, 3, 4, 5]
letras = ["b", "d", "a", "c"]
letras.sort()
print(letras)   # Imprime: ["a", "b", "c", "d"]
```

Después de `numeros.sort()`, la lista de números que era `[3, 1, 4, 2, 5]` se convierte en `[1, 2, 3, 4, 5]` (ordenada ascendentemente). Lo mismo ocurre con las letras, quedando en orden alfabético.

**Nota:** Todos los elementos de la lista deben ser comparables entre sí para poder ordenarse. Si intentas ordenar una lista que contiene tipos no comparables (por ejemplo números y cadenas mezclados), obtendrás un error en tiempo de ejecución. Existe un parámetro opcional `reverse=True` si deseas ordenar en orden descendente, o la función separada `sorted(lista)` que devuelve una lista ordenada sin modificar la original. Pero esos detalles pueden explorarse más adelante.

### reverse()

Invierte el orden de los elementos de la lista.

* **Uso:** `mi_lista.reverse()`
* **Descripción:** Reorganiza la lista invirtiendo la secuencia de elementos: el primer elemento pasa a ser el último, el segundo pasa a ser el penúltimo, y así sucesivamente.
* **Retorno:** Ninguno (modifica la lista directamente).

**Ejemplo:**

```python
puntos = [100, 200, 300]
puntos.reverse()
print(puntos)  # Imprime: [300, 200, 100]
palabra = ["P", "y", "t", "h", "o", "n"]
palabra.reverse()
print(palabra) # Imprime: ["n", "o", "h", "t", "y", "P"]
```

En el ejemplo, `puntos` que era `[100, 200, 300]` pasa a ser `[300, 200, 100]` tras aplicar `reverse()`. Y la lista `palabra`, que contenía los caracteres de `"Python"`, se invierte completamente.

### index()

Devuelve el índice de la primera aparición de un valor especificado en la lista.

* **Uso:** `mi_lista.index(x)` (también admite argumentos opcionales para iniciar o limitar la búsqueda, e.g. `mi_lista.index(x, inicio, fin)`).
* **Descripción:** Busca en la lista el valor `x` y retorna el índice de su primera ocurrencia. Si `x` no está en la lista, genera un `ValueError`.
* **Retorno:** Un número entero que es el índice donde se encontró `x`.

**Ejemplo:**

```python
nombres = ["Ana", "Luis", "Pedro", "Luis"]
pos = nombres.index("Luis")
print(pos)  # Imprime: 1
```

En la lista `nombres`, la primera vez que aparece `"Luis"` es en el índice `1` (recordando que empezamos a contar en 0). Aunque `"Luis"` aparece de nuevo más adelante, `index` solo da la primera posición. Si quisiéramos encontrar siguientes apariciones, tendríamos que usar `index` nuevamente indicando un punto de inicio diferente, o recorrer la lista.

Si hubiéramos buscado un nombre que no está en la lista, por ejemplo `nombres.index("Julia")`, se produciría un error porque ese elemento no existe en `nombres`.

### count()

Cuenta cuántas veces aparece un valor específico en la lista.

* **Uso:** `mi_lista.count(x)`
* **Descripción:** Recorre la lista y cuenta cuántas veces aparece el valor `x`.
* **Retorno:** Un entero representando el número de ocurrencias de `x` en la lista (0 si no está presente).

**Ejemplo:**

```python
valores = [7, 7, 3, 7, 5, 3]
print(valores.count(7))  # Imprime: 3
print(valores.count(3))  # Imprime: 2
print(valores.count(8))  # Imprime: 0
```

En la lista `valores`, el número `7` aparece 3 veces, el `3` aparece 2 veces, y el `8` no aparece (por eso `count(8)` devuelve 0).

### clear()

Elimina todos los elementos de la lista, dejándola vacía.

* **Uso:** `mi_lista.clear()`
* **Descripción:** Borra **todos** los elementos de `mi_lista`. Después de llamar a este método, la lista quedará vacía (`[]`).
* **Retorno:** Ninguno (modifica la lista).

**Ejemplo:**

```python
datos = [1, 2, 3, 4]
datos.clear()
print(datos)  # Imprime: []
```

Después de ejecutar `datos.clear()`, la lista `datos` que contenía `[1, 2, 3, 4]` queda como `[]`. La lista sigue existiendo (no se elimina la variable), pero ahora está vacía.

### copy()

Crea una **copia superficial** de la lista. Esto es útil cuando queremos duplicar una lista para manipularla sin afectar la original.

* **Uso:** `nueva_lista = mi_lista.copy()`
* **Descripción:** Genera una nueva lista con los mismos elementos que `mi_lista`. Es una copia **superficial**, lo que significa que si la lista original contiene objetos mutables (por ejemplo, sublistas), la copia contendrá referencias a los mismos objetos, no copias profundas de ellos.
* **Retorno:** La nueva lista copiada.

**Ejemplo:**

```python
a = [1, 2, 3]
b = a.copy()
b.append(4)
print(a)  # Imprime: [1, 2, 3]
print(b)  # Imprime: [1, 2, 3, 4]
```

En este caso, `b` es una copia de `a`. Al agregar `4` a la lista `b`, la lista `a` original permanece sin cambios. Esto demuestra que `b` y `a` son listas independientes después de la copia. (Si la lista contuviera sublistas y se modifican elementos dentro de esas sublistas, la situación es más compleja debido a que la copia es superficial, pero ese es un detalle avanzado).

### extend()

Agrega múltiples elementos al final de la lista, tomando los elementos de otro iterable (como otra lista) y extendiendo la lista original con ellos.

* **Uso:** `mi_lista.extend(iterable)`
* **Descripción:** Toma cada elemento del `iterable` proporcionado (por ejemplo, otra lista, una tupla o incluso una cadena) y lo añade al final de `mi_lista`. Es equivalente a hacer varios `append` uno por uno por cada elemento del iterable.
* **Retorno:** Ninguno (modifica la lista original).

**Ejemplo:**

```python
nombres1 = ["Ana", "Luis"]
nombres2 = ["Pedro", "Marta"]
# Extender nombres1 con los elementos de nombres2
nombres1.extend(nombres2)
print(nombres1)  # Imprime: ["Ana", "Luis", "Pedro", "Marta"]
```

Aquí teníamos dos listas, `nombres1` y `nombres2`. Después de `nombres1.extend(nombres2)`, la lista `nombres1` termina conteniendo los elementos de ambas listas (fusionadas). `nombres2` permanece sin cambios.

Para entender la diferencia entre `extend` y `append`, consideremos lo siguiente:

```python
lista_a = [1, 2, 3]
lista_b = [4, 5]
lista_a.append(lista_b)
print(lista_a)  # Imprime: [1, 2, 3, [4, 5]]

lista_c = [1, 2, 3]
lista_d = [4, 5]
lista_c.extend(lista_d)
print(lista_c)  # Imprime: [1, 2, 3, 4, 5]
```

* Con `append`, al hacer `lista_a.append(lista_b)`, **se agrega la lista completa `lista_b` como un solo elemento** al final de `lista_a`. Por eso vemos `[4, 5]` como sublista dentro de `lista_a`.
* Con `extend`, al hacer `lista_c.extend(lista_d)`, **se agregan los elementos individuales** de `lista_d` a `lista_c`. El resultado es que `lista_c` contiene `[1,2,3,4,5]`.

En resumen, usa `extend` cuando quieras concatenar listas (u otros iterables) elemento a elemento, y usa `append` cuando quieras añadir un elemento único (que podría ser también una lista anidada, si es lo que deseas).

### Ejercicios

* Crea una lista vacía llamada `resultados`. Luego:

  1. Agrega (usando `append`) los números 10, 20 y 30 a la lista.
  2. Inserta (usando `insert`) el número 15 en la posición 1 de la lista.
  3. Ahora la lista debería ser `[10, 15, 20, 30]`. Elimina el número 20 usando `remove`.
  4. Muestra la lista resultante después de cada operación para verificar los cambios.
* Dada la lista `nombres = ["Ana", "Juan", "Pedro"]`, realiza las siguientes operaciones:

  * Usa `append` para agregar `"Luisa"` al final.
  * Usa `insert` para agregar `"Maria"` al inicio de la lista.
  * Usa `pop` para quitar el último elemento (debería quitar `"Luisa"` que acabas de agregar) y almacénalo en una variable `ultimo_nombre`. Imprime `ultimo_nombre` y también la lista resultante.
  * Usa `index` para encontrar la posición de `"Pedro"` en la lista y muestra ese índice.
* Crea una lista de números desordenados, por ejemplo `nums = [8, 3, 1, 7, 4]`. Luego:

  * Ordena la lista con `sort()` y muéstrala.
  * Invierte el orden de la lista ordenada con `reverse()` y muéstrala de nuevo.
* Dada la lista `valores = [5, 5, 7, 5, 8, 8, 5]`, encuentra cuántas veces aparece el número 5 usando `count()`, y cuántas veces aparece el número 8.
* Crea una lista llamada `original` con algunos elementos (por ejemplo números o cadenas). Luego haz `copia = original.copy()`. Modifica la lista `copia` (por ejemplo, agrega un nuevo elemento con `append` o cambia un valor existente) y luego imprime ambas listas (`original` y `copia`) para verificar que la original no cambió cuando modificaste la copia.
* Crea dos listas de números, por ejemplo `lista1 = [1, 2, 3]` y `lista2 = [4, 5, 6]`. Luego:

  * Usa `extend` para añadir todos los elementos de `lista2` a `lista1`. Muestra el resultado.
  * ¿Qué pasaría si en lugar de `extend` hubieras usado `append` para añadir `lista2` a `lista1`? (Puedes probarlo en código y observar la diferencia).

## Iteracion sobre listas (bucle for y while)

Recorrer o **iterar** sobre una lista significa procesar cada uno de sus elementos, uno tras otro, normalmente utilizando un bucle. En Python, las dos estructuras de bucle más comunes para iterar listas son el **bucle `for`** y el **bucle `while`**.

### Bucle `for`

La sintaxis más sencilla para recorrer una lista es:

```python
for elemento in mi_lista:
    # hacer algo con elemento
```

Esto permitirá que la variable `elemento` tome, en cada iteración, el valor de cada ítem en `mi_lista` en orden. El bucle continuará hasta haber procesado todos los elementos de la lista.

**Ejemplo 1:** Iterar una lista de números e imprimir cada uno:

```python
numeros = [10, 20, 30, 40]
for n in numeros:
    print(n)
```

**Salida:**

```
10
20
30
40
```

En cada iteración del bucle, `n` toma el valor de un elemento de la lista `numeros` y lo imprime. Este código imprime cada número en una línea separada.

**Ejemplo 2:** Sumar todos los números de una lista usando `for`:

```python
suma = 0
for n in numeros:
    suma = suma + n
print("Suma:", suma)  # Imprime: Suma: 100
```

Aquí usamos una variable acumuladora `suma` que se inicia en 0 y en cada iteración agrega el valor de `n`. Al final, `suma` contiene la suma de todos los valores (10+20+30+40 = 100).

**Ejemplo 3:** Iterar una lista de cadenas para mostrar mensajes personalizados:

```python
nombres = ["Ana", "Pedro", "Luis"]
for nombre in nombres:
    print("Hola, " + nombre + "!")
```

**Salida:**

```
Hola, Ana!
Hola, Pedro!
Hola, Luis!
```

Cada nombre de la lista es utilizado dentro del mensaje `"Hola, ...!"`.

**Uso de índices en bucles `for`:** Si necesitas el índice de cada elemento mientras iteras (por ejemplo, para modificarlos o para mostrarlos con su posición), puedes combinar `range()` y `len()`:

```python
frutas = ["manzana", "pera", "uva"]
for i in range(len(frutas)):
    print(f"Fruta {i}: {frutas[i]}")
```

**Salida:**

```
Fruta 0: manzana
Fruta 1: pera
Fruta 2: uva
```

En este caso usamos `range(len(frutas))` para generar la secuencia de índices `0, 1, 2` y acceder a cada elemento por su índice dentro del bucle.

(Python también tiene una función `enumerate` que facilita obtener índice y valor a la vez en un for, pero mantendremos las cosas simples por ahora.)

### Bucle `while`

Un bucle `while` repite un bloque de código **mientras** una condición booleana dada sea verdadera. Para iterar sobre una lista con `while`, usualmente se utiliza un índice que va aumentando manualmente. Por ejemplo:

```python
calificaciones = [85, 90, 72, 88]
i = 0
while i < len(calificaciones):
    print("Calificacion:", calificaciones[i])
    i += 1  # incrementamos el indice manualmente
```

Este bucle `while` iniciará con `i = 0` y seguirá ejecutándose mientras `i` sea menor que `len(calificaciones)` (es decir, mientras haya elementos con ese índice). Dentro del bucle, mostramos la calificación correspondiente y luego incrementamos `i` en 1 para pasar al siguiente índice. Cuando `i` alcance el valor de `len(calificaciones)`, la condición `i < len(calificaciones)` será falsa y el bucle terminará.

**Ejemplo 4:** Buscar un elemento en una lista usando `while`:

```python
objetivo = 72
encontrado = False
i = 0
while i < len(calificaciones):
    if calificaciones[i] == objetivo:
        encontrado = True
        break  # salir del bucle al encontrar
    i += 1

if encontrado:
    print("Valor encontrado en indice", i)
else:
    print("Valor no encontrado")
```

En este ejemplo, recorremos la lista `calificaciones` hasta encontrar el valor 72. Usamos la variable booleana `encontrado` y la instrucción `break` para salir del bucle cuando hallamos el elemento buscado. Al final, informamos si se encontró y en qué índice.

Tanto el bucle `for` como el `while` nos permiten recorrer listas, pero generalmente preferimos `for` para iterar sobre colecciones en Python por ser más simple y menos propenso a errores (no hay que manejar manualmente el índice ni la condición de fin, excepto en casos especiales).

### Ejercicios

* Crea una lista con los números del 1 al 5. Recorre la lista con un bucle `for` y muestra cada número multiplicado por 2.
* Dada la lista `temperaturas = [20, 23, 19, 25, 22]` (que representan temperaturas diarias en grados Celsius), usa un bucle `for` para calcular la temperatura media (promedio) y mostrarla.
* Usa un bucle `for` para recorrer la lista `temperaturas` y contar cuántos valores son mayores o iguales a 23 grados. Muestra el conteo al final.
* Repite los dos ejercicios anteriores (promedio y conteo) usando bucles `while` en lugar de `for`.
* Escribe un programa que, dada una lista de palabras, use un bucle `for` para construir una cadena única con todas las palabras concatenadas con espacios. Por ejemplo, dada `["Hola", "mundo", "!"]` debería producir `"Hola mundo !"`.
* Escribe un bucle `while` que invierta una lista dada. **Pista:** Puedes iterar desde el final hacia el principio usando un índice negativo o decreciendo un índice positivo.

## Comprensiones de listas basicas

Las **comprensiones de listas** (*list comprehensions* en inglés) ofrecen una sintaxis concisa para crear nuevas listas a partir de secuencias o rangos, transformando o filtrando cada elemento. Una comprensión de lista combina en una sola línea la lógica de un bucle `for` (y opcionalmente una condición) para generar una lista de forma compacta.

La sintaxis básica es:

```python
nueva_lista = [ expresión  for elemento in secuencia  if condicion_opcional ]
```

Donde:

* *`expresión`* es la operación o valor que se va a agregar a la nueva lista (posiblemente usando `elemento`).
* *`for elemento in secuencia`* es un bucle que itera sobre cada `elemento` en la `secuencia` dada (que puede ser una lista, rango, etc.).
* *`if condicion_opcional`* es una parte opcional que, si está presente, filtra los elementos: solo los que cumplen la condición se usan para generar la nueva lista.

Veamos algunos ejemplos básicos de comprensiones de lista:

**Ejemplo 1: Crear una lista de cuadrados de números**

Supongamos que queremos una lista con los cuadrados de los números del 1 al 5. Podríamos hacerlo con un bucle `for` tradicional, pero con comprensiones es muy directo:

```python
cuadrados = [x * x for x in range(1, 6)]
print(cuadrados)  # Imprime: [1, 4, 9, 16, 25]
```

Explicación: `range(1, 6)` genera 1,2,3,4,5. Por cada `x` en ese rango, calculamos `x * x` y ese valor se agrega a la lista `cuadrados`. El resultado es la lista de los cuadrados: 1^2, 2^2, ..., 5^2.

**Ejemplo 2: Convertir todos los caracteres de una lista de palabras a mayúsculas**

```python
palabras = ["hola", "mundo", "python"]
mayusculas = [p.upper() for p in palabras]
print(mayusculas)  # Imprime: ["HOLA", "MUNDO", "PYTHON"]
```

Aquí, para cada palabra `p` en la lista original `palabras`, aplicamos `p.upper()` (que convierte la cadena a mayúsculas) y guardamos el resultado en la nueva lista `mayusculas`. Obtenemos una lista equivalente pero con texto en mayúsculas.

**Ejemplo 3: Filtrar con comprensión de listas**

Ahora usemos la cláusula opcional `if` para filtrar elementos. Por ejemplo, obtener solo los números pares de una lista de números:

```python
numeros = [10, 15, 20, 33, 42, 55]
pares = [n for n in numeros if n % 2 == 0]
print(pares)  # Imprime: [10, 20, 42]
```

En este caso, la comprensión `[n for n in numeros if n % 2 == 0]` toma cada `n` de `numeros` y **solo** incluye `n` en la nueva lista si cumple la condición `n % 2 == 0` (es decir, si `n` es divisible por 2, lo que significa que es par). El resultado es que `pares` contiene solo los elementos pares de la lista original.

**Ejemplo 4: Crear una lista a partir de otra transformando los elementos**

Supongamos que tenemos una lista de temperaturas en Celsius y queremos obtener una lista convertida a Fahrenheit. La fórmula para convertir de °C a °F es `F = C * 9/5 + 32`. Podemos hacer:

```python
celsius = [0, 10, 20, 30]
fahrenheit = [ (temp * 9/5) + 32 for temp in celsius ]
print(fahrenheit)  # Imprime: [32.0, 50.0, 68.0, 86.0]
```

La nueva lista `fahrenheit` se construye tomando cada `temp` en la lista `celsius` y aplicando la fórmula dentro de la comprensión de lista.

Las comprensiones de lista hacen el código más corto y a menudo más fácil de leer, pero es importante usarlas en situaciones donde la lógica es simple. Para procesos muy complejos, a veces es más claro usar bucles normales. Sin embargo, para transformaciones y filtrados simples, son una herramienta poderosa.

### Ejercicios

* Dada la lista `numeros = [1, 2, 3, 4, 5]`, usa una comprensión de lista para crear una nueva lista llamada `cuadrados` que contenga los cuadrados de esos números. (Resultado esperado: `[1, 4, 9, 16, 25]`).
* Crea una lista llamada `even_numbers` que contenga solo los números pares del 0 al 20 (incluyendo 20) utilizando una comprensión de lista con `range()` y una condición `if`.
* Supón que tienes una lista de palabras: `palabras = ["sol", "luna", "cielo", "nube"]`. Usa una comprensión de lista para obtener una lista de longitudes de esas palabras. (Por ejemplo, `"sol"` -> 3).
* Dada una lista de números, por ejemplo `valores = [3, -1, 5, 0, -7, 9]`, usa una comprensión de lista para filtrar los números positivos (mayores que 0). El resultado debería ser `[3, 5, 9]`.
* (Desafío adicional) Usa una comprensión de lista anidada para generar la siguiente lista: `[[1, 2, 3], [1, 2, 3], [1, 2, 3]]`. Pista: podría implicar un bucle dentro de otro en la sintaxis de comprensión. (Este es un ejercicio avanzado para pensar creativamente con comprensiones).

## Listas anidadas (matrices)

Una **lista anidada** es una lista que contiene a su vez otras listas como elementos. Esto permite crear estructuras de datos de dos dimensiones (o más), similares a tablas o **matrices**. Por ejemplo, podríamos usar una lista de listas para representar una matriz de números, donde cada sublista es una fila.

**Ejemplo de una matriz 3x3 (3 filas por 3 columnas):**

```python
matriz = [
    [1, 2, 3],    # Fila 0
    [4, 5, 6],    # Fila 1
    [7, 8, 9]     # Fila 2
]
```

Aquí `matriz` es una lista que contiene 3 elementos, y cada uno de esos elementos es a su vez una lista de 3 números. Podemos visualizarla como:

Fila 0: \[1, 2, 3]
Fila 1: \[4, 5, 6]
Fila 2: \[7, 8, 9]

Cada fila es una lista, y todas juntas conforman la matriz. Para referirnos a un elemento específico de la matriz, necesitamos **dos índices**: uno para la fila y otro para la columna. Por ejemplo, `matriz[1][2]` referiría al elemento de la fila 1, columna 2. En la matriz de ejemplo:

* `matriz[1]` es la segunda fila `[4, 5, 6]`.
* `matriz[1][2]` es el tercer elemento de esa fila, que es `6`.

**Creación de listas anidadas:** Se pueden crear escribiendo directamente los corchetes anidados como arriba, o iniciar con listas vacías y agregarlas, etc. Por ejemplo, otra forma de construir la misma matriz:

```python
fila1 = [1, 2, 3]
fila2 = [4, 5, 6]
fila3 = [7, 8, 9]
matriz = [fila1, fila2, fila3]
```

Después de esta construcción, `matriz` resulta igual que en el ejemplo anterior.

También es posible que las sublistas (filas) tengan longitudes diferentes, creando estructuras "irregulares". Por ejemplo `lista_irregular = [[1, 2], [3, 4, 5], [6]]` es una lista anidada de 3 elementos donde la primera sublista tiene 2 elementos, la segunda 3 y la tercera 1. Sin embargo, cuando hablamos de "matrices" solemos referirnos al caso donde todas las sublistas tienen la misma longitud, formando filas y columnas alineadas.

## Como acceder, modificar y recorrer matrices

Trabajar con listas anidadas sigue los mismos principios que con listas simples, solo que ahora manejamos múltiples niveles de indices. Veamos cómo **acceder**, **modificar** y **recorrer** matrices (listas de listas).

### Acceso a elementos en una matriz

Para acceder a un elemento específico dentro de una matriz, utilizamos la notación de **doble índice** `[fila][columna]`. El primer índice selecciona cuál de las sublistas (fila) queremos, y el segundo índice selecciona el elemento dentro de esa sublista (columna).

Sigamos con el ejemplo de matriz 3x3:

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
elemento = matriz[2][1]
print(elemento)  # Imprime: 8
```

Aquí `matriz[2]` es la tercera fila `[7, 8, 9]`, y luego `[2][1]` indica el elemento de índice 1 en esa fila, que es `8` (ya que en la fila `[7, 8, 9]`, los índices 0,1,2 corresponden a 7, 8, 9 respectivamente).

Del mismo modo que con listas simples, podemos usar índices negativos para contar desde el final en cada dimensión:

* `matriz[-1]` sería la última fila (`[7, 8, 9]` en este caso).
* `matriz[0][-1]` sería el último elemento de la primera fila (en el ejemplo, `3`).
* `matriz[-1][-1]` sería el último elemento de la última fila (en el ejemplo, `9`).

### Modificar elementos en una matriz

Para modificar un valor en una lista anidada, accedemos a él con sus dos índices y luego le asignamos un nuevo valor, igual que hacíamos con una lista sencilla pero extendido a dos niveles:

```python
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matriz[0][1] = 99   # Cambiamos el elemento en fila 0, columna 1 (valor original 2) por 99
print(matriz[0])    # Imprime: [1, 99, 3]
matriz[2][2] = 42   # Cambiamos el elemento en fila 2, columna 2 (valor original 9) por 42
print(matriz[2])    # Imprime: [7, 8, 42]
```

Después de estas operaciones, la matriz queda:

```
[
    [1, 99, 3],
    [4, 5, 6],
    [7, 8, 42]
]
```

Hemos modificado exitosamente elementos en la primera y la última fila.

También podríamos reemplazar filas enteras (ya que cada fila es en sí misma una lista). Por ejemplo, `matriz[1] = [10, 11, 12]` sustituiría la fila completa `[4, 5, 6]` por `[10, 11, 12]`. Este tipo de asignación reemplaza toda la sublista de la fila 1.

### Recorrer matrices con bucles anidados

Para procesar todos los elementos de una matriz, es común usar **bucles anidados**: un bucle para las filas y otro para las columnas dentro de cada fila.

**Ejemplo: Imprimir todos los elementos de una matriz, fila por fila:**

```python
matriz = [
    [1, 99, 3],
    [4, 5, 6],
    [7, 8, 42]
]

for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()  # nueva linea al terminar cada fila
```

**Salida:**

```
1 99 3 
4 5 6 
7 8 42 
```

Explicación: El primer `for` itera sobre cada `fila` de la matriz (cada `fila` es una lista). Luego, el segundo `for` recorre cada `elemento` dentro de esa `fila` y lo imprime seguido de un espacio (`end=" "` evita el salto de línea inmediato para que los elementos de la misma fila se impriman en la misma línea). Después de terminar el bucle interno para una fila, usamos `print()` sin argumentos para hacer un salto de línea y empezar a imprimir la siguiente fila en una nueva línea.

**Ejemplo: Calcular la suma de todos los elementos de una matriz:**

```python
suma_total = 0
for fila in matriz:
    for elemento in fila:
        suma_total += elemento
print("Suma total:", suma_total)  # Imprime la suma de todos los numeros de la matriz
```

Este código utiliza dos bucles anidados para recorrer cada número de la matriz y acumular la suma total en `suma_total`.

**Ejemplo: Modificar todos los elementos de una matriz (multiplicar por 2):**

```python
for i in range(len(matriz)):            # recorre indices de filas
    for j in range(len(matriz[i])):     # recorre indices de columnas en la fila i
        matriz[i][j] = matriz[i][j] * 2
print(matriz)
```

Después de este código, cada valor numérico en la matriz `matriz` habrá sido multiplicado por 2. Usamos `range(len(matriz))` para iterar sobre índices de fila, y `range(len(matriz[i]))` para iterar sobre índices de columna en la fila actual.

### Ejercicios

* Crea manualmente una matriz de 3x3 llamada `matriz_3x3` con números de tu elección. Luego:

  * Imprime el elemento de la segunda fila y tercera columna (usar índices `[1][2]` si consideramos la primera fila índice 0).
  * Cambia el valor de la primera fila y primera columna por un nuevo número.
  * Imprime toda la matriz fila por fila para verificar los cambios.
* Dada la siguiente matriz:

  ```python
  tabla = [
      [2, 4, 6],
      [8, 10, 12],
      [14, 16, 18]
  ]
  ```

  Escribe un código que calcule la suma de cada fila por separado y la muestre. El formato de salida podría ser:

  ```
  Suma de fila 0: ...
  Suma de fila 1: ...
  Suma de fila 2: ...
  ```
* Usando la misma `tabla` anterior, recorre todos los elementos y encuentra cuál es el mayor valor en la matriz. Muestra ese valor al final.
* Crea una matriz de 2x3 (2 filas, 3 columnas) que contenga cadenas de texto (por ejemplo, nombres de personas organizados en dos grupos). Recorre la matriz e imprime cada nombre junto con su posición `[fila,columna]` correspondiente.
* **Reto avanzado:** Escribe un programa que verifique si una matriz cuadrada de 3x3 es una **matriz identidad**. Una matriz identidad es aquella que tiene 1 en todos los elementos de la diagonal principal (posición \[0]\[0], \[1]\[1], \[2]\[2]) y 0 en los demás elementos. Por ejemplo, `[[1,0,0],[0,1,0],[0,0,1]]` es identidad. Tu programa debe imprimir "Es identidad" o "No es identidad" según el caso.

---
