
# Arreglos en Programación: Listas, Tuplas y Arrays en Python

Los **arreglos** son estructuras de datos que nos permiten almacenar colecciones de valores bajo una sola variable. En la vida cotidiana podemos pensar en una lista de compras o una agenda telefónica: en lugar de manejar cada dato por separado, los agrupamos en una estructura ordenada. En programación, los arreglos facilitan el manejo de conjuntos de datos cuando no sabemos cuántos elementos tendremos o necesitamos procesar muchos valores de forma eficiente. 

En Python, contamos con varias estructuras de datos para manejar colecciones, entre las más importantes: **listas**, **tuplas** y **diccionarios** (estos últimos como estructura asociativa). Además, para cálculos numéricos eficientes, usamos los **arrays de NumPy**. A continuación, presentaremos cada una de estas estructuras, desde conceptos básicos hasta aspectos avanzados, acompañando la teoría con ejemplos prácticos en Python (usando Visual Studio Code como editor) y ejercicios al final de cada sección. 

## Listas en Python

Una **lista** es una secuencia **ordenada** de elementos donde cada elemento tiene una posición (índice) definida. Las listas en Python son extremadamente versátiles: permiten almacenar *múltiples valores en una sola variable*. Esto resuelve problemas donde necesitamos manejar muchos datos sin crear innumerables variables individuales. Por ejemplo, si queremos almacenar los nombres de 100 estudiantes, no tendría sentido crear 100 variables distintas; en lugar de eso, podemos guardarlos en una sola lista ([Listas (arreglos o vectores) en Python: Uso y creación](https://www.programarya.com/Cursos/Python/estructuras-de-datos/listas#:~:text=No%20tendr%C3%ADa%20sentido%20crear%20100,Mira%20a%20continuaci%C3%B3n%20un%20ejemplo)). Las listas nos permiten agrupar todos esos valores y manejarlos cómodamente.

**Definición y características:** Las listas en Python son similares a los "arreglos" o "vectores" de otros lenguajes. Sus propiedades principales son: 

- **Ordenadas:** mantienen el orden en que agregamos los elementos.  
- **Indexadas:** podemos acceder a cada elemento por su posición numérica (comenzando desde 0).  
- **Heterogéneas:** pueden contener elementos de distintos tipos de datos (enteros, cadenas, booleanos, incluso otras listas).  
- **Mutables:** se pueden modificar; sus elementos pueden cambiarse, agregarse o eliminarse después de creada ([ Listas en Python | El Libro De Python](https://ellibrodepython.com/listas-en-python#:~:text=,pueden%20a%C3%B1adir%20o%20eliminar%20elementos)).  
- **Dinámicas:** pueden crecer o reducirse en tamaño según agreguemos o quitemos elementos (no es necesario declarar un tamaño fijo).  

En resumen, una lista es un contenedor flexible y dinámico. Veamos cómo se utilizan en la práctica.

### Creación de listas

En Python, una lista se define usando corchetes `[]` y separando sus elementos con comas. Por ejemplo:

```python
# Creamos listas vacías de dos formas equivalentes
mi_lista = [] 
otra_lista = list()

# Creamos listas con elementos iniciales
numeros = [1, 2, 3, 4]               # lista de enteros
mezclada = [1, "Hola", 3.67, True]   # lista con diferentes tipos
```

En el código anterior, `mi_lista` y `otra_lista` son listas vacías (sin elementos). Luego definimos `numeros` con cuatro enteros, y `mezclada` con elementos de distinto tipo (un entero, una cadena, un flotante y un booleano). Python nos permite incluso crear una lista a partir de otro iterable usando la función `list()`, por ejemplo `list("ABC")` produciría `['A', 'B', 'C']`. 

También es posible *imprimir* o visualizar listas directamente. Si ejecutamos `print(numeros)`, obtendremos la representación de la lista:

```python
print(numeros)  # Imprime: [1, 2, 3, 4]
```

### Acceso a elementos por índice

Cada elemento en una lista tiene un índice según su posición. **El primer elemento tiene índice 0**, el segundo índice 1, y así sucesivamente. Podemos acceder a los elementos usando la sintaxis `lista[indice]`. Veamos un ejemplo:

```python
frutas = ["Manzana", "Banana", "Cereza", "Durazno"]
print(frutas[0])   # Manzana (primer elemento, índice 0)
print(frutas[2])   # Cereza  (tercer elemento, índice 2)
```

La salida será:

```
Manzana  
Cereza
```

Es importante notar que si intentamos acceder a un índice que no existe (por ejemplo `frutas[10]` en la lista anterior), obtendremos un error `IndexError` porque estamos fuera del rango de la lista.

**Índices negativos:** Python ofrece una característica útil: los índices negativos para contar desde el final de la lista. El índice `-1` refiere al **último** elemento, `-2` al penúltimo, y así sucesivamente. Por ejemplo:

```python
print(frutas[-1])  # Durazno (último elemento)
print(frutas[-2])  # Cereza  (penúltimo elemento)
```

Esto nos permite acceder fácilmente al final de la lista sin saber exactamente su longitud.

### Modificar elementos de una lista

Debido a que las listas son mutables, podemos cambiar sus elementos después de creadas. Para asignar un nuevo valor a una posición, usamos nuevamente la notación de índices en el lado izquierdo de una asignación:

```python
numeros = [10, 20, 30, 40]
numeros[2] = 99            # Cambiamos el tercer elemento (índice 2) a 99
print(numeros)             # Imprime: [10, 20, 99, 40]
```

En este ejemplo, la lista original `[10, 20, 30, 40]` se modifica reemplazando el `30` por `99`. Al imprimir la lista, vemos el nuevo contenido con el cambio aplicado.

También podemos **agregar** o **eliminar** elementos usando métodos incorporados de las listas:

- `append(x)`: Agrega el elemento `x` al **final** de la lista.  
- `insert(i, x)`: Inserta el elemento `x` en la posición `i`, desplazando los demás a la derecha.  
- `pop(i)`: Elimina y devuelve el elemento en la posición `i` (por defecto, el último si no se especifica `i`).  
- `remove(x)`: Busca y elimina la **primera** ocurrencia del valor `x` en la lista.  

Por ejemplo:

```python
# Empezamos con una lista inicial
letras = ["a", "b", "c"]
letras.append("d")           # Añadimos "d" al final -> ["a","b","c","d"]
letras.insert(1, "z")        # Insertamos "z" en índice 1 -> ["a","z","b","c","d"]
print(letras)                # Imprime: ['a', 'z', 'b', 'c', 'd']

letras.remove("z")           # Quitamos el elemento "z" -> ["a","b","c","d"]
ultimo = letras.pop()        # Quitamos el último elemento ("d"), lo guardamos en 'ultimo'
print(letras, ultimo)        # Imprime: ['a', 'b', 'c'] d
```

Como vemos, tras usar `append` y `insert`, la lista creció incorporando nuevos elementos. Luego, con `remove` eliminamos el valor `"z"`, y con `pop()` (sin índice) quitamos el último elemento `"d"`, obteniendo la lista final `['a','b','c']`. El método `pop` además nos devuelve el elemento eliminado, que guardamos en la variable `ultimo` (en este caso, `"d"`). 

Otra forma de eliminar elementos es con la instrucción `del lista[i]`, que borra el elemento en la posición `i`. Por ejemplo, `del letras[0]` eliminaría `"a"` de la lista. Después de cualquier eliminación o adición, los índices de los elementos posteriores pueden cambiar (ya que la lista se reordena automáticamente).

### Slicing (rebanado) de listas

El *slicing* es una operación que nos permite extraer una **sublista** de una lista original, especificando un rango de índices. Utiliza la sintaxis `lista[inicio:fin:paso]` donde:  
- `inicio` es el índice donde comienza el slice (incluido, por defecto 0 si se omite),  
- `fin` es el índice donde termina el slice **sin incluir** ese índice (por defecto, el final de la lista si se omite),  
- `paso` es el intervalo de salto entre índices (opcional, por defecto 1).

Por ejemplo, dada la lista:

```python
numeros = [10, 20, 30, 40, 50, 60]
```

Podemos obtener diferentes slices: 

```python
print(numeros[1:4])    # Elementos de índice 1 a 3 -> [20, 30, 40]
print(numeros[:3])     # Desde el inicio hasta índice 2 -> [10, 20, 30]
print(numeros[4:])     # Desde índice 4 hasta el final -> [50, 60]
print(numeros[::2])    # Toda la lista, saltando de 2 en 2 -> [10, 30, 50]
print(numeros[::-1])   # Paso negativo invierte la lista -> [60, 50, 40, 30, 20, 10]
```

Analicemos cada caso: `numeros[1:4]` toma los elementos de las posiciones 1, 2 y 3 (el índice 4 no se incluye). `numeros[:3]` toma del inicio hasta el índice 2. `numeros[4:]` toma desde el índice 4 hasta el final. `numeros[::2]` toma todos los elementos pero con paso 2 (es decir, índices 0,2,4,...). Finalmente, `numeros[::-1]` utiliza un paso negativo de -1, que produce una copia de la lista invertida (muy útil para invertir la lista rápidamente).

El resultado impreso de las operaciones anteriores sería:

```
[20, 30, 40]  
[10, 20, 30]  
[50, 60]  
[10, 30, 50]  
[60, 50, 40, 30, 20, 10]
```

### Listas anidadas (listas de listas)

Las listas pueden contener a su vez otras listas como elementos. A esto le llamamos **listas anidadas**. Esto nos permite representar estructuras de múltiples dimensiones, como matrices (tablas de valores en filas y columnas). Por ejemplo, pensemos en una tabla de calificaciones de alumnos por materia:

```python
# Lista de listas: cada sub-lista corresponde a [nota_matematicas, nota_historia, nota_lengua] de un alumno
calificaciones = [
    [85, 90, 78],   # Notas del alumno 1
    [72, 88, 91],   # Notas del alumno 2
    [90, 95, 94]    # Notas del alumno 3
]
```

En `calificaciones`, tenemos una lista principal con 3 elementos, y cada elemento es a su vez una lista de 3 notas. Podemos imaginar esta estructura como una tabla de 3 filas por 3 columnas. Para acceder, por ejemplo, a la nota de Historia del alumno 2, identificamos que es fila 2, columna 2 (considerando índice base 0: alumno 2 tiene índice 1, Historia es la segunda materia con índice 1): 

```python
nota_historia_alum2 = calificaciones[1][1]
print("La nota de Historia del alumno 2 es:", nota_historia_alum2)
# Imprime: La nota de Historia del alumno 2 es: 88
```

Aquí usamos dos índices: `[1][1]` primero accede al segundo elemento de `calificaciones` (que es `[72, 88, 91]`) y luego al segundo elemento de esa sublista (que es `88`). Podemos anidar tantos índices `[]` como niveles de anidación tenga la estructura.

Las listas anidadas nos permiten manejar datos tabulares. Sin embargo, manipular estructuras multidimensionales manualmente puede volverse complejo; más adelante veremos cómo la biblioteca NumPy facilita estas operaciones.

### Operaciones comunes con listas

Podemos realizar diversas operaciones con listas que hacen nuestro código más conciso:

- **Concatenación:** usando el operador `+` podemos unir dos listas en una sola. Ejemplo: `[1,2] + [3,4]` produce `[1,2,3,4]`.  
- **Repetición:** usando el operador `*` con un número entero, repetimos la lista ese número de veces. Ejemplo: `["Hola"] * 3` produce `["Hola", "Hola", "Hola"]`.  
- **Pertenencia:** podemos verificar si un elemento está en la lista con el operador `in`. Ejemplo: `5 in [1,2,3,4]` devuelve `False` (porque 5 no está en la lista).  
- **Longitud:** la función incorporada `len(lista)` devuelve la cantidad de elementos de la lista. 

Ejemplo rápido de estas operaciones:

```python
a = [1, 2, 3]
b = [4, 5]
c = a + b
print(c)              # Imprime: [1, 2, 3, 4, 5]
print(b * 3)          # Imprime: [4, 5, 4, 5, 4, 5]
print(3 in a, 6 in a) # Imprime: True False  (3 sí está en a, 6 no)
print(len(c))         # Imprime: 5  (número de elementos en c)
```

**Comprensión de listas (List comprehensions):** Es una sintaxis avanzada y poderosa para crear listas derivadas de otras de forma concisa. Una comprensión de lista combina bucles y condiciones en una sola expresión dentro de corchetes. Por ejemplo, supongamos que queremos generar una lista con los cuadrados de los números del 1 al 5. Podemos hacerlo con un bucle tradicional o usando comprensión:

```python
# Usando un bucle for tradicional:
cuadrados = []
for n in range(1, 6):
    cuadrados.append(n**2)
print(cuadrados)  # [1, 4, 9, 16, 25]

# Usando comprensión de lista:
cuadrados_v2 = [n**2 for n in range(1, 6)]
print(cuadrados_v2)  # [1, 4, 9, 16, 25]
```

Ambos métodos producen el mismo resultado `[1, 4, 9, 16, 25]`. La segunda forma es más compacta. La sintaxis `[expr for item in iterable if condicion]` nos permite incluso filtrar con una condición opcional. Por ejemplo, `[n**2 for n in range(1, 6) if n % 2 == 0]` generaría los cuadrados solo de los números pares del 1 al 5 (es decir `[4, 16]`). Esta técnica mejora la legibilidad y reduce líneas de código, pero es recomendable usarla con moderación y solo cuando hace el código más claro.

> **Nota:** Cuando asignamos una lista a otra variable con `=`, ambas variables referencian la *misma* lista en memoria. Si modificamos una, la otra también verá el cambio. Para copiar una lista independiente podemos usar `lista.copy()` o `lista[:]`. Es un detalle importante para evitar efectos inesperados al manipular listas.

### Ejercicios prácticos (Listas)

Para reforzar estos conceptos, intenta realizar los siguientes ejercicios con listas:

1. **Listado de números impares:** Crea una lista con los números del 1 al 10. Utilizando slicing o métodos, muestra por pantalla los números en orden inverso separados por comas. *(Pista: puedes usar `lista[::-1]` para invertir la lista, o métodos como `reverse()`.)*

2. **Notas de exámenes:** Imagina que tienes una lista de calificaciones de un examen: `notas = [58, 96, 72, 85, 90]`. Escribe código para calcular la nota máxima, la mínima y el promedio de las calificaciones. *(Pista: Python ofrece las funciones `max()`, `min()` y `sum()` que pueden ser útiles.)*

3. **Actualización de inventario:** Supón que tienes una lista `inventario = ["espada", "escudo", "poción"]` que representa objetos en un juego. Realiza las siguientes operaciones:  
   a) Agrega un nuevo objeto `"casco"` al final de la lista.  
   b) Inserta `"armadura"` al inicio de la lista.  
   c) Elimina `"poción"` de la lista.  
   Después de cada operación, imprime la lista para verificar el resultado.

4. **Filtrado de palabras:** Dada una lista de palabras, por ejemplo `palabras = ["sol", "sombra", "amarillo", "sal", "rojo"]`, construye una nueva lista que contenga solo aquellas palabras que empiezan con la letra "s". *(Pista: utiliza una comprensión de listas con una condición.)*

---

## Tuplas en Python

Una **tupla** es muy similar a una lista en cuanto a que es una secuencia ordenada de elementos. La diferencia clave es que las tuplas son **inmutables**, es decir, **no pueden modificarse** una vez creadas. Si las listas eran como hojas de cálculo en las que podemos borrar o agregar filas, las tuplas son como registros escritos en piedra: una vez definidos sus valores, no podemos cambiarlos.

**Definición y sintaxis:** Las tuplas se denotan usando paréntesis `()` en lugar de corchetes. Por ejemplo:

```python
punto = (3, 5)               # Tupla con dos elementos
valores = ("alto", True, 7.5)  # Tupla con distintos tipos
```

También es posible omitir los paréntesis y separarlos solo por comas, aunque por legibilidad generalmente se usan. **Importante:** Para crear una tupla de un solo elemento, se debe incluir una coma final, de lo contrario Python la interpretará como un valor entre paréntesis. Por ejemplo, `tupla1 = (5,)` crea una tupla que contiene el número 5, mientras que `tupla2 = (5)` simplemente es el número 5 entre paréntesis (no una tupla).

**Acceso por índice:** Al igual que las listas, las tuplas están indexadas desde 0 y podemos acceder a sus elementos con la sintaxis `tupla[indice]`. También soportan índices negativos para contar desde el final y la función `len()` para conocer su longitud. Ejemplo:

```python
dias_semana = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo")
print(dias_semana[0])    # Lunes
print(dias_semana[-1])   # Domingo
print(len(dias_semana))  # 7
```

**Inmutabilidad:** Intentar modificar una tupla después de creada provocará un error. Por ejemplo:

```python
numeros = (1, 2, 3)
numeros[0] = 99  # intentar cambiar el primer elemento
```

Si ejecutamos este código, Python lanzará un `TypeError` indicando que `'tuple' object does not support item assignment`. Esta inmutabilidad tiene algunas implicaciones: por un lado, las tuplas son más seguras cuando queremos asegurarnos de que ciertos datos no cambien accidentalmente; por otro lado, no podemos usar métodos como `append` o `remove` en tuplas (ya que no se pueden agregar ni quitar elementos).

**¿Para qué usamos tuplas?** A pesar de no poder modificarse, las tuplas son muy útiles en ciertas situaciones:

- **Datos constantes:** Cuando tenemos un conjunto de valores que conceptualmente no deben cambiar, por ejemplo las coordenadas de un punto `(x, y)`, los días de la semana, los meses del año, etc. Usar tupla comunica la intención de inmutabilidad.  
- **Retornos múltiples de funciones:** En Python, una función puede devolver varios valores empaquetándolos en una tupla. Ej: `return (x, y)` devuelve dos valores. Al usarla, podemos hacer `a, b = funcion()` para *desempaquetar* la tupla en variables separadas.  
- **Claves de diccionario:** Las tuplas (al ser inmutables) pueden usarse como claves en diccionarios, a diferencia de las listas. Por ejemplo, un diccionario podría mapear coordenadas (tupla) a un valor: `registro[(fila,columna)] = "Ocupado"`.

**Desempaquetado de tuplas:** Python permite asignar los elementos de una tupla directamente a varias variables, lo que se denomina *desempaquetado*. Por ejemplo:

```python
persona = ("Alice", 30, "Colombia")
nombre, edad, pais = persona
print(nombre)  # Alice
print(edad)    # 30
print(pais)    # Colombia
```

Aquí, la tupla `persona` contiene tres elementos, y podemos asignarlos de una vez a `nombre`, `edad` y `pais` respectivamente. Esta técnica hace el código más limpio cuando sabemos que la tupla tiene exactamente el número de elementos que vamos a capturar. Incluso se puede usar para intercambiar valores entre variables de forma sucinta: `a, b = b, a` (Python creará una tupla `(b,a)` en la asignación, logrando el swap de valores en una sola línea).

> **Nota:** Aunque no podemos modificar una tupla en sí, si una tupla contiene un elemento mutable (como una lista interna), ese elemento interno sí podría modificarse. Por ejemplo, `tupla = (1, [2,3])` es válida; no podemos cambiar el 1 por otro valor, pero sí podríamos hacer `tupla[1].append(4)` para modificar la lista contenida. Este es un caso especial a tener en cuenta.

### Ejercicios prácticos (Tuplas)

1. **Tupla de coordenadas:** Crea una tupla llamada `coord` que represente la coordenada (x,y) de un punto, por ejemplo `(4, 7)`. Luego, escribe código para imprimir por separado el valor de `x` y `y` desempaquetando la tupla. Intenta modificar el valor `x` de la tupla para ver qué error ocurre.

2. **Información personal:** Supón que tienes una tupla `persona = ("Carlos", 22, "Perú")` con nombre, edad y país. Escribe una línea de código que desempaquete estos valores en variables individuales `nombre, edad, pais`. Luego imprime un mensaje usando esas variables, por ejemplo: `"Carlos tiene 22 años y es de Perú"`.

3. **Un solo elemento:** Define una tupla de un solo elemento con el valor `100`. Comprueba el tipo de esta tupla con `type()` para asegurarte de que es de tipo `tuple` y no un entero. *(Pista: recuerda la coma final en la sintaxis de tupla unitaria.)*

---

## Diccionarios: Estructuras asociativas en Python

Los **diccionarios** son otro tipo de estructura de datos en Python, también conocidos como *arreglos asociativos* o *mapas*. A diferencia de listas y tuplas (que utilizan índices numéricos), los diccionarios almacenan pares **clave-valor**. Esto significa que cada valor almacenado en el diccionario se asocia a una clave única, que sirve para recuperarlo. 

Podemos imaginar un diccionario como un **diccionario de idioma** tradicional: tenemos una palabra (clave) y su definición (valor). O pensemos en una agenda telefónica: el nombre de la persona es la clave y el número de teléfono es el valor. Con un diccionario, en lugar de buscar por posición numérica, buscamos por la clave.

**Creación de un diccionario:** Se utilizan llaves `{}`. Dentro, definimos cada par en la forma `clave: valor`, separados por comas. Ejemplo:

```python
# Diccionario de ejemplo: país -> capital
capitales = {
    "Colombia": "Bogotá",
    "Francia": "París",
    "Japón": "Tokio"
}
```

Aquí hemos creado un diccionario llamado `capitales` con 3 entradas. Las claves son nombres de países y los valores sus capitales. Las claves suelen ser de tipo cadena (str) o números, y **deben ser inmutables** (por eso las listas no pueden ser claves, pero las tuplas sí). 

**Acceso a valores:** Para obtener el valor asociado a una clave, usamos la sintaxis `diccionario[clave]`. Siguiendo el ejemplo:

```python
print(capitales["Francia"])   # Imprime: París
```

Si la clave no existe en el diccionario, Python lanzará una excepción `KeyError`. Para evitar errores, podemos usar el método `get`: `capitales.get("Italia")` devolvería `None` (o un valor por defecto que podemos proporcionar) en lugar de error si la clave no está.

**Agregar y modificar elementos:** Los diccionarios son mutables. Podemos asignar una nueva entrada simplemente usando una nueva clave:

```python
capitales["Italia"] = "Roma"       # Agrega una nueva pareja clave-valor
capitales["Colombia"] = "Medellín" # Modifica el valor asociado a Colombia
```

En la primera línea agregamos la capital de Italia, en la segunda modificamos la capital de Colombia (supongamos que por error). Tras esto, el diccionario `capitales` tendría `"Italia": "Roma` añadido y `"Colombia": "Medellín"` actualizado.

**Eliminar elementos:** Podemos usar la instrucción `del` para eliminar una clave y su valor:

```python
del capitales["Japón"]
print(capitales)
```

Esto eliminaría la entrada de Japón. También existe el método `pop(clave)` que elimina la clave dada y devuelve su valor, o `popitem()` que elimina y devuelve el último par insertado (en Python 3.7+ los diccionarios mantienen el orden de inserción).

**Recorrer un diccionario:** Podemos iterar por sus elementos de varias formas:
- Por claves: `for pais in capitales: print(pais)` (iterar sobre el diccionario itera por sus claves por defecto).
- Por valores: `for capital in capitales.values(): print(capital)`.
- Por ambos: `for pais, capital in capitales.items(): print(pais, "->", capital)`.

Esto último aprovecha que `items()` devuelve pares `(clave, valor)` que podemos desempaquetar en dos variables dentro del loop.

**Ejemplo práctico sencillo:**

```python
# Recorrido de diccionario
for pais, capital in capitales.items():
    print(f"La capital de {pais} es {capital}")
```

Salida esperada:

```
La capital de Colombia es Medellín  
La capital de Francia es París  
La capital de Italia es Roma
```

**Breve mención de utilidad:** Los diccionarios son muy eficientes para buscar valores a partir de una clave. Internamente usan una técnica de *hashing*, por lo que las búsquedas, inserciones y eliminaciones suelen ser muy rápidas (en promedio tiempo constante, O(1)). Son ideales para representar conjuntos de datos donde podemos identificar cada elemento con una llave única (por ejemplo, un registro de estudiantes identificado por matrícula, un inventario identificado por código de producto, etc.).

### Ejercicios prácticos (Diccionarios)

1. **Agenda de contactos:** Crea un diccionario llamado `contactos` que contenga nombres de personas como claves y sus números de teléfono como valores (por ejemplo, `"Ana": 123456, "Luis": 789012`). Luego:  
   a) Imprime el número de teléfono de "Ana".  
   b) Agrega un nuevo contacto `"Pedro": 345678`.  
   c) Actualiza el número de "Luis".  
   d) Elimina el contacto "Ana".  
   Finalmente, imprime el diccionario resultante.

2. **Contando palabras:** Dada la frase `"hola hola adiós hola adiós"`, cuenta cuántas veces aparece cada palabra usando un diccionario para almacenar las frecuencias. (Pista: puedes usar el método `split()` de las cadenas para separarlas por espacios, luego iterar y usar un diccionario donde las claves sean palabras y los valores contadores que incrementas).

3. **Diccionario de cuadrados:** Crea un diccionario que mapee números del 1 al 5 con sus cuadrados. Es decir, que quede `{1:1, 2:4, 3:9, 4:16, 5:25}`. Puedes hacerlo usando un bucle o comprensión de diccionario.

---

## Arrays con NumPy (Arreglos N-dimensionales eficientes)

Cuando trabajamos con **datos numéricos** en grandes cantidades o con múltiples dimensiones (matrices, vectores, etc.), las listas de Python pueden volverse ineficientes o incómodas de manejar. Aquí es donde entra en juego **NumPy**, una biblioteca especializada que introduce el tipo de dato **array** (ndarray) para computación numérica eficiente.

Un **array de NumPy** es similar a una lista, pero con importantes diferencias:
- Todos sus elementos son del **mismo tipo** (por ejemplo, todos enteros, o todos flotantes).  
- Ocupa un bloque contiguo de memoria, lo que hace las operaciones matemáticas mucho más rápidas al aprovechar eficientemente la CPU (incluso utilizando código optimizado en C bajo el capó).  
- Puede ser **multidimensional** nativamente, facilitando el trabajo con matrices y tensores.  

En términos prácticos, usar arrays de NumPy nos permite realizar operaciones vectoriales y matriciales de forma concisa y rápida, sin tener que escribir bucles explícitos en Python. De hecho, para cálculos numéricos intensivos, los arrays de NumPy pueden ser **hasta decenas de veces más rápidos** que las listas de Python equivalentes ([La librería Numpy | Aprende con Alf](https://aprendeconalf.es/docencia/python/manual/numpy/#:~:text=La%20ventaja%20de%20Numpy%20frente,y%20matrices%20de%20grandes%20dimensiones)).

### Preparación: importando NumPy

NumPy no es una parte built-in del lenguaje, así que para usarlo primero debemos importarlo. Convencionalmente, se importa con el alias `np`:

```python
import numpy as np
```

Asegúrate de tener instalado NumPy (`pip install numpy`) si trabajas en tu entorno (en muchas distribuciones de Python viene preinstalado, especialmente si usas Anaconda). En Visual Studio Code, puedes escribir el import al inicio de tu script de Python.

### Creación de arrays de NumPy

Existen varias formas de crear arrays:

- **A partir de una lista (o tupla) de Python:** utilizando `np.array(lista)`. El array resultante tendrá el tipo de datos inferido a partir de la lista. Podemos opcionalmente especificar el tipo con el parámetro `dtype`.  
- **Usando funciones de NumPy para generar datos**: por ejemplo, `np.zeros(shape)` crea un array de la forma dada lleno de ceros, `np.ones(shape)` igual con unos, `np.full(shape, valor)` con un valor constante, `np.arange(inicio, fin, paso)` crea una secuencia (similar a `range` pero devuelve un array), `np.linspace(inicio, fin, num)` genera `num` valores equidistantes entre inicio y fin, `np.random.random(shape)` genera valores aleatorios entre 0 y 1, etc. Estas funciones evitan tener que crear primero una lista en Python y luego convertirla.

Veamos ejemplos:

```python
import numpy as np

# 1D arrays (vectores)
lista = [1, 2, 3, 4]
a = np.array(lista)               # crea un array [1 2 3 4] de tipo int
b = np.array([1.2, 3.5, 5.1])     # array de floats [1.2 3.5 5.1]

# 2D array (matriz) a partir de lista de listas
matriz = np.array([[1, 2, 3],
                   [4, 5, 6]])    # 2 filas x 3 columnas

# Arrays generados con funciones
zeros = np.zeros((2, 3))          # matriz 2x3 de ceros
unos = np.ones((3, 3), dtype=int) # matriz 3x3 de unos enteros
secuencia = np.arange(0, 10, 2)   # array [0 2 4 6 8]
espaciados = np.linspace(0, 1, 5) # array [0.   0.25 0.5  0.75 1.  ] (5 puntos entre 0 y 1)
aleatorios = np.random.random((2,2))  # matriz 2x2 con valores aleatorios entre 0 y 1
```

Al imprimir estos arrays, veríamos algo como:

```python
print(a)         # [1 2 3 4]
print(matriz)    # [[1 2 3]
                #  [4 5 6]]
print(zeros)     # [[0. 0. 0.]
                #  [0. 0. 0.]]
print(secuencia) # [0 2 4 6 8]
print(aleatorios) # por ejemplo [[0.615 0.428]
                 #             [0.649 0.135]]
```

Observemos varias cosas:
- Cuando Python muestra un array, lo hace sin comas entre los elementos y con una representación ligeramente distinta a las listas (por ejemplo, `matriz` se muestra en formato 2D). 
- `zeros` muestra `0.` indicando que son flotantes (por defecto np.zeros produce floats). En cambio `unos` tiene dtype int, así que se mostrarían como enteros sin decimal.
- `aleatorios` contiene números decimales aleatorios distintos cada vez que se ejecuta.

**Dimensión y forma (shape):** Cada array tiene atributos que describen su estructura. El más importante es `shape`, que es una tupla de enteros indicando el tamaño en cada dimensión. Por ejemplo:
```python
print(matriz.shape)   # (2, 3) -> 2 filas, 3 columnas
print(a.shape)        # (4,)   -> una dimensión de longitud 4
```
Otros atributos útiles:
- `ndim`: número de dimensiones (ej: matriz.ndim sería 2, a.ndim es 1).  
- `size`: número total de elementos (ej: matriz.size = 6).  
- `dtype`: tipo de dato de los elementos (ej: matriz.dtype, a.dtype).  

### Operaciones vectorizadas con arrays

Una de las mayores ventajas de los arrays de NumPy es poder realizar **operaciones matemáticas** elemento a elemento (*element-wise*) de forma directa, sin bucles explícitos. Con las listas de Python, si queríamos sumar 2 a cada elemento de una lista, tendríamos que iterar o usar comprensión de listas; con NumPy, simplemente hacemos `mi_array + 2`. 

Veamos comparaciones concretas entre listas y arrays:

```python
valores = [1, 2, 3, 4]
# Sumar 10 a cada elemento usando lista -> necesitamos un bucle o comprensión
resultado_lista = [x + 10 for x in valores]
print(resultado_lista)  # [11, 12, 13, 14]

# Convertimos a array de NumPy
arr = np.array(valores)
resultado_arr = arr + 10
print(resultado_arr)    # [11 12 13 14]
```

En el caso del array, `arr + 10` automáticamente creó un **nuevo array** sumando 10 a cada componente de `arr` (el array original `arr` permanece sin cambios a menos que asignemos el resultado de vuelta). Esta capacidad de operar con constantes o entre arrays del mismo tamaño se extiende a otras operaciones: resta (`-`), multiplicación (`*`), división (`/`), potencia (`**`), etc., todas aplicadas elemento por elemento. 

**Ejemplo de multiplicación:**

```python
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
# Multiplicación elemento a elemento con listas requiere recorrer
producto_lista = [x*y for x, y in zip(lista1, lista2)]
print(producto_lista)  # [4, 10, 18]

arr1 = np.array(lista1)
arr2 = np.array(lista2)
producto_arr = arr1 * arr2
print(producto_arr)    # [ 4 10 18 ]
```

Nótese que usar `*` con listas de Python no hace multiplicación elemento a elemento sino **repetición**. Por ejemplo `lista1 * 2` produciría `[1,2,3,1,2,3]` (duplica la lista). En cambio con arrays de NumPy, `arr1 * 2` produce `[2, 4, 6]` (multiplica cada elemento por 2). Esta es una distinción importante: los operadores aritméticos están **sobrecarcados** en NumPy para realizar cálculos matemáticos con arrays, mientras que en las listas siguen siendo concatenación o repetición.

Además de los operadores, NumPy provee muchas **funciones matemáticas** universales (*ufuncs*) que operan elemento a elemento: por ejemplo `np.sqrt(arr)`, `np.sin(arr)`, `np.log(arr)`, etc., aplican la función matemática correspondiente a cada elemento del array. Por ejemplo:

```python
valores = np.array([1, 4, 9, 16])
raices = np.sqrt(valores)
print(raices)  # [1.  2.  3.  4.]
```

Calculó la raíz cuadrada de cada elemento del array de entrada.

**Funciones de agregación:** Para operaciones como suma de todos los elementos, valor mínimo, máximo, promedio, etc., NumPy también ofrece funciones optimizadas:
- `np.sum(arr)` suma todos los elementos (también `arr.sum()` como método).
- `np.min(arr)`, `np.max(arr)` para mínimo y máximo.
- `np.mean(arr)` para el promedio (media) aritmética.
- `np.std(arr)` desviación estándar, etc.

Estas funciones pueden trabajar **por eje** en arrays multidimensionales (veremos esto en breve con *broadcasting* y *multidimensionalidad*).

### Indexado y slicing en arrays NumPy

El acceso por índices en arrays NumPy 1D es igual que en las listas. En arrays **multidimensionales**, se usa una coma para separar los índices de cada dimensión. Dado un array 2D (matriz), tenemos `array2d[fila, columna]`. Por ejemplo:

```python
mat = np.array([[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]])
print(mat[0, 2])  # Elemento fila 0, col 2 -> 30
print(mat[2, 1])  # Elemento fila 2, col 1 -> 80
```

También podemos usar notación `[i][j]` separada como con listas anidadas (`mat[0][2]` también daría 30), pero la sintaxis con coma es preferida por ser más compacta.

El slicing igualmente se extiende a múltiples dimensiones. La sintaxis general es `array[inicio:fin, inicio2:fin2]` para 2D (y se puede ampliar a más dimensiones separadas por comas). Por ejemplo, tomando la matriz `mat` definida arriba:

```python
submat = mat[0:2, 1:3]
print(submat)
```

Esto tomaría las filas desde 0 hasta 1 (0:2 toma 0 y 1) y las columnas desde 1 hasta 2 (1:3 toma 1 y 2), resultando en la sub-matriz de tamaño 2x2:

```
[[20 30]
 [50 60]]
```

Podemos mezclar índices específicos con slices usando coma. Por ejemplo `mat[ :, 0]` significa "todas las filas, columna 0", resultando en el primer column vector `[10, 40, 70]`. O `mat[1, :]` significa "fila 1, todas las columnas" -> `[40, 50, 60]`. El concepto es similar al slicing de listas pero aplicado en cada dimensión.

> **Atención:** En NumPy, a diferencia de las listas, los slices **no copian** los datos sino que producen una **vista** de la misma matriz. Es decir, `submat` en el ejemplo anterior referencia los mismos datos que `mat`. Si modificamos `submat[0,0]`, también cambiará `mat[0,1]` correspondiente. Si necesitas una copia independiente, debes usar `.copy()`. Este detalle es relevante para ahorrar memoria y tiempo cuando se manipulan subarrays grandes, pero hay que ser cuidadoso.

### Broadcasting en NumPy

**Broadcasting** es un concepto avanzado pero fundamental en NumPy que permite realizar operaciones aritméticas con arrays de diferente forma (dimensiones), expandiendo automáticamente uno de ellos para que coincidan las dimensiones necesarias ([Broadcasting y Operaciones Lógicas en NumPy - Platzi](https://platzi.com/clases/10365-python-data-science/70743-broadcasting-y-operaciones-logicas-en-numpy/#:~:text=Broadcasting%20es%20una%20funcionalidad%20poderosa,tambi%C3%A9n%20acelera%20significativamente%20las%20operaciones)). En términos simples, el broadcasting hace posible operaciones entre arrays de tamaños no idénticos, siempre que sus formas sean **compatibles**.

Por ejemplo, supongamos que tenemos un array 2D de forma (3x3) y un array 1D de longitud 3, y queremos sumarlos. NumPy *broadcasting* extenderá (replicará virtualmente) el array de menor dimensión para que la operación tenga sentido. Veamos un caso concreto:

```python
import numpy as np
A = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([10, 20, 30])
print("A:\n", A)
print("b:", b)
C = A + b  # Sumamos array 2x3 con array de longitud 3
print("A + b:\n", C)
```

Salida:

```
A:
 [[1 2 3]
  [4 5 6]]
b: [10 20 30]
A + b:
 [[11 22 33]
  [14 25 36]]
```

¿Cómo se logró esta suma? `b` tiene shape (3,) mientras `A` tiene shape (2,3). El mecanismo de broadcasting replicó implícitamente `b` en cada fila de `A` para hacer la suma fila por fila. Es decir, conceptualmente trató `b` como si fuera:

```
[[10 20 30],
 [10 20 30]]
```

y luego sumó elemento a elemento con `A`. Lo importante es que NumPy **no crea realmente** dos filas extras en memoria, sino que calcula la operación como si `b` estuviera alineado sobre cada fila de `A`. Esto hace las operaciones muy eficientes en tiempo y memoria.

El broadcasting aplica cuando las dimensiones de los arrays involucrados cumplen ciertas reglas: básicamente, desde la última dimensión hacia atrás, los tamaños de cada dimensión deben ser iguales o uno de ellos debe ser 1 (o inexistente, que se trata como 1). Si una dimensión es 1, se puede estirar (replicar) para que coincida con la otra. Si alguna dimensión no coincide y ninguna es 1, la operación no es posible.

Ejemplos comunes de broadcasting:
- Sumar o multiplicar un escalar (un número) a un array: el escalar se considera de shape compatible en todas las dimensiones (como 1x1x...x1), se extiende a la forma del array. Ej: `arr * 5` multiplica cada elemento por 5.
- Operar un array 1D con un 2D como vimos (longitudes compatibles).
- Operar un array de shape (n,1) con otro de shape (n,m): el de (n,1) se extenderá por columnas, o viceversa.

Un caso de uso práctico: supongamos que tenemos un array de temperaturas en grados Celsius y queremos convertirlo a Fahrenheit. Podemos aplicar la fórmula elemento a elemento con broadcasting:

```python
temp_c = np.array([0.0, 20.0, 37.0, 100.0])    # Celsius
temp_f = temp_c * 9/5 + 32
print(temp_f)  # [ 32.   68.  98.6 212. ]
```

Aquí multiplicamos `temp_c` por `9/5` (escalar) y sumamos 32 (escalar). Ambos escalar se difunden a cada elemento del array.

En resumen, **broadcasting** nos permite escribir código matemático muy conciso y cercano a la notación matemática, sin bucles explícitos. Debemos, eso sí, entender qué está haciendo para evitar confusiones. Si se intenta hacer operaciones con formas incompatibles, obtendremos un error de *ValueError* indicando que las formas no se pueden broadcastear juntas.

### Arreglos multidimensionales: Listas anidadas vs Arrays de NumPy

Ya hemos visto que se pueden crear estructuras de múltiples dimensiones tanto con listas anidadas como con arrays de NumPy. Resumamos las diferencias y ventajas de cada enfoque:

- **Estructura fija vs flexible:** Un array de NumPy n-dimensional es esencialmente un bloque de memoria *rectangular* (todas las filas del mismo tamaño, etc.), mientras que una lista de listas en Python podría ser irregular (cada sublista de distinto tamaño). Para matrices matemáticas regulares, NumPy es más adecuado.
- **Operaciones elemento a elemento:** Con listas anidadas, si deseamos sumar dos "matrices" tenemos que iterar manualmente o anidar comprensiones. Con NumPy, la suma `A + B` funciona directamente si ambos son arrays de la misma shape. Por ejemplo:

```python
# Usando listas anidadas
A_list = [[1,2,3],[4,5,6]]
B_list = [[10,20,30],[40,50,60]]
# Sumar manualmente elemento a elemento
resultado = []
for filaA, filaB in zip(A_list, B_list):
    nueva_fila = []
    for x, y in zip(filaA, filaB):
        nueva_fila.append(x + y)
    resultado.append(nueva_fila)
print("Suma con listas:", resultado)

# Usando NumPy
import numpy as np
A_arr = np.array(A_list)
B_arr = np.array(B_list)
print("Suma con arrays:", A_arr + B_arr)
```

La primera parte con listas es más verbose y propensa a errores, mientras que la segunda es directa. La salida sería:

```
Suma con listas: [[11, 22, 33], [44, 55, 66]]  
Suma con arrays: [[11 22 33]
 [44 55 66]]
```

- **Rendimiento:** Para tamaños grandes, los arrays de NumPy son mucho más rápidos y usan menos memoria debido a su implementación en C optimizada ([La librería Numpy | Aprende con Alf](https://aprendeconalf.es/docencia/python/manual/numpy/#:~:text=La%20ventaja%20de%20Numpy%20frente,y%20matrices%20de%20grandes%20dimensiones)). Las listas son más lentas para operaciones numéricas masivas porque implican bucles en Python (interpretados). Si vas a realizar cálculos matemáticos con miles o millones de elementos, NumPy es la elección obligada.
- **Comodidad de utilidades:** NumPy ofrece gran cantidad de funciones para manipular arrays: cambiar de forma (`reshape`), trasponer matrices, calcular estadísticas por ejes (`arr.sum(axis=0)` por columnas, etc.), generar datos aleatorios, realizar álgebra lineal (multiplicación de matrices, descomposiciones), entre otras. Con listas nativas tendríamos que implementar manualmente muchas de esas funcionalidades o usar bucles.

**Conclusión en esta comparación:** Para datos tabulares o vectoriales donde se requieran operaciones matemáticas, los arrays de NumPy proporcionan claridad y eficiencia. Las listas nativas quedan para tareas más generales o donde se mezclen tipos de datos, operaciones de lista no numéricas, etc. En muchos proyectos de ciencia de datos o ingeniería, es común convertir las listas a arrays lo antes posible para aprovechar estas ventajas.

### Visualización de datos con arrays (matplotlib)

Aprovechemos el uso de arrays de NumPy para realizar algunas visualizaciones simples con la biblioteca **matplotlib**. Esta biblioteca nos permite crear gráficos de todo tipo. Aquí veremos dos ejemplos sencillos: representar una matriz como una imagen de colores, y graficar la distribución (histograma) de un conjunto de datos.

#### Representación gráfica de una matriz (imagen de calor)

Supongamos que tenemos una matriz de valores y queremos visualizarla gráficamente. Podemos usar `matplotlib.pyplot.imshow` para mostrar la matriz como una imagen de calor (heatmap), donde cada valor se representará con un color. 

Como ejemplo, crearemos un array 5x5 donde el valor en la posición (i,j) sea la suma de sus índices (esto produce una matriz con un patrón creciente hacia la esquina inferior derecha):

```python
import numpy as np
import matplotlib.pyplot as plt

# Crear matriz 5x5 donde elemento [i,j] = i + j
matriz = np.zeros((5,5), dtype=int)
for i in range(5):
    for j in range(5):
        matriz[i,j] = i + j

# Mostrar la matriz numéricamente
print(matriz)
# [[0 1 2 3 4]
#  [1 2 3 4 5]
#  [2 3 4 5 6]
#  [3 4 5 6 7]
#  [4 5 6 7 8]]

# Graficar la matriz como imagen de calor
plt.imshow(matriz, cmap="viridis")
plt.colorbar(label="Valor")
plt.title("Heatmap de matriz 5x5 (valores = i+j)")
plt.show()
```

 ([image]()) *Representación de una matriz 5x5 cuyos valores son la suma de sus índices (i+j). Cada color corresponde a un rango de valores según la barra de color de la derecha. Podemos ver que el valor mínimo 0 (esquina superior izquierda) se muestra en color oscuro, y el valor máximo 8 (esquina inferior derecha) en color claro.* 

En el código, usamos `cmap="viridis"`, que es una paleta de color. La barra de color (`colorbar`) nos permite interpretar los valores. Este tipo de visualización podría ser útil, por ejemplo, para ver patrones en una matriz de datos o incluso para mostrar imágenes en escala de grises si el array representara pixeles.

#### Visualización de una distribución de datos (histograma)

Ahora, generemos datos aleatorios con NumPy y representemos su distribución mediante un **histograma**. Un histograma agrupa los valores en rangos (bins) y muestra cuántos valores caen en cada rango.

Hagamos un ejemplo: supongamos que generamos 1000 números aleatorios siguiendo una distribución normal (también llamada campana de Gauss, centrada en 0). Luego, construimos el histograma de esos valores:

```python
import numpy as np
import matplotlib.pyplot as plt

# Generar 1000 datos aleatorios con distribución normal (media=0, desv=1)
datos = np.random.randn(1000)

# Graficar histograma de los datos
plt.hist(datos, bins=30, edgecolor='black')
plt.title("Histograma de 1000 valores aleatorios (dist. normal)")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()
```

 ([image]()) *Histograma de 1000 valores generados aleatoriamente con una distribución normal estándar. Se observa la clásica forma de campana: la mayoría de los valores se concentran alrededor de 0 (centro) y menos frecuencia hacia los extremos. El eje horizontal representa el valor y el vertical la cantidad de ocurrencias en cada intervalo.* 

En este código, `np.random.randn(1000)` nos dio un array de 1000 valores distribuidos normalmente con media 0 y desviación estándar 1. Usamos `plt.hist` con 30 bins (barras) para ver la distribución. La forma aproximada debería ser simétrica centrada en 0. Cada ejecución variará un poco porque los datos son aleatorios, pero con 1000 puntos la tendencia se mantiene.

Estos ejemplos combinan NumPy y matplotlib: NumPy nos facilitó generar y manipular los datos, y matplotlib nos permitió visualizarlos. En problemas de la vida real, este dúo es muy poderoso, por ejemplo para visualizar series temporales (primero generar con NumPy una escala de tiempo y datos, luego graficar) o imágenes (que son arrays 2D de pixeles) entre otros.

### Ejercicios prácticos (Arrays con NumPy)

1. **Operaciones con vectores:** Crea un array de NumPy llamado `valores` con los números del 1 al 10. Calcula y muestra:
   - La suma de todos los elementos (usa `np.sum`).
   - El promedio de los elementos (`np.mean`).
   - Un nuevo array resultante de multiplicar por 2 cada elemento de `valores` (operación vectorizada).

2. **Datos aleatorios y estadísticas:** Genera un array de 20 números aleatorios enteros entre 1 y 100 (puedes usar `np.random.randint`). Con ese array, calcula el valor máximo, el mínimo y la desviación estándar (`np.std`). Luego ordena el array de menor a mayor y muéstralo. *(Pista: `np.sort` puede ayudarte a ordenar fácilmente un array.)*

3. **Temperaturas diarias:** Supón que tienes un array con las temperaturas promedio de cada día de una semana en grados Celsius, por ejemplo `temp_c = np.array([18.5, 20.1, 22.8, 21.0, 19.5, 17.2, 16.8])`. Calcula un nuevo array con estas temperaturas convertidas a grados Fahrenheit usando la fórmula `F = C * 9/5 + 32` (aplicada elemento a elemento). Muestra el resultado formateando la salida para que se vea algo como: "Temperaturas en Fahrenheit: [65.3 68.2 ...]".

4. **Matriz y suma de columnas:** Crea una matriz (array 2D) de shape 3x3 con números enteros a tu elección. Escribe código para calcular la suma de cada columna de la matriz. *(Pista: puedes usar `sum(axis=0)` en el array, o bien sumar manualmente utilizando slicing o bucles.)* Comprueba que los resultados son correctos.

5. **Broadcasting en práctica:** Tienes dos arrays `precios = np.array([100, 200, 300])` (precios en dólares) y `descuento = 0.1` (10% de descuento). Calcula un nuevo array `precios_desc` que sea el resultado de aplicar el descuento a cada precio. Luego redondea los precios resultantes a 2 decimales. *(Pista: multiplicar el array por (1 - descuento) dará los precios con descuento. Para redondear, puedes usar `np.round`.)*

---

## Conclusiones y consejos finales

Hemos abarcado un amplio espectro de **arreglos en programación con Python**, desde las básicas listas y tuplas, pasando por diccionarios (arreglos asociativos) y llegando a los potentes arrays de NumPy para computación numérica. En resumen:

- **Listas**: ideales para colecciones ordenadas y mutables, útiles en infinidad de problemas. Recuerda sus métodos útiles y la flexibilidad que brindan.
- **Tuplas**: similares a las listas pero inmutables; úsalas cuando necesites garantizar que los datos no cambien (o como claves en diccionarios).
- **Diccionarios**: permiten mapear claves a valores, ofreciendo búsquedas rápidas y una forma natural de representar relaciones (como nombre->dato). Son fundamentales para datos etiquetados.
- **NumPy Arrays**: llevan los arreglos al siguiente nivel, con eficiencia y herramientas matemáticas. Son el estándar para cálculos científicos, procesamiento de imágenes, análisis de datos, etc.

Finalmente, siempre es bueno reforzar estos conceptos con práctica. ¡No dudes en experimentar en tu editor (por ejemplo, VS Code) creando tus propios ejemplos y resolviendo los ejercicios propuestos! Conforme te familiarices con cada estructura, podrás elegir la adecuada para cada problema y aprovechar al máximo sus capacidades. ¡Happy coding!
