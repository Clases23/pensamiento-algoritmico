
# Funciones en Programación (Python)

## Introducción a las funciones

Imagina que debes realizar cierta tarea repetidamente en un programa, como calcular el área de un círculo para distintos radios, o convertir temperaturas de Celsius a Fahrenheit en varios lugares del código. Reescribir las mismas instrucciones una y otra vez no solo es propenso a errores, sino también poco eficiente. Aquí es donde entran en juego las **funciones**. En programación, una función es como una **subrutina** o **subprograma**: un bloque de código independiente diseñado para realizar una tarea específica, que puede recibir **entradas** (datos) y **devolver** un resultado. 

Podemos pensar en una función como en una **máquina o caja negra**: le damos ciertos insumos (parámetros), la máquina realiza un proceso interno (las instrucciones de la función), y nos entrega un producto o resultado (valor de retorno). Al igual que una máquina expendedora de café produce una bebida a partir de ingredientes cuando presionamos un botón, una función ejecuta su código y (opcionalmente) devuelve un resultado cuando la “invocamos” o llamamos. Lo importante es que **sabemos lo que hace** (por su nombre y documentación) y qué esperamos de ella, pero no necesitamos rehacer todo el procedimiento cada vez; simplemente **reutilizamos** esa función.

Las funciones nos permiten organizar el código de forma modular y legible. Algunas ventajas clave de utilizar funciones son:

- **Reutilización de código**: Escribes la lógica una vez y la utilizas múltiples veces, evitando duplicación (siguiendo el principio *No te repitas* o DRY, *Don't Repeat Yourself*).
- **Abstracción**: Puedes “encapsular” detalles complejos dentro de la función y pensar en el programa en términos de tareas de alto nivel. Por ejemplo, en lugar de preocuparte por *cómo* se calcula el área de un círculo cada vez, simplemente llamas a `calcular_area_circulo(radio)` y confías en que hace lo correcto.
- **Mantenibilidad**: Si necesitas cambiar cómo se realiza una tarea, actualizas la función en un solo lugar en lugar de modificar múltiples secciones de código repetido.
- **Claridad**: Un programa organizado en funciones con nombres descriptivos se lee casi como una lista de pasos o subtareas, haciendo más fácil entender la lógica general.

Ya has utilizado funciones sin darte cuenta: por ejemplo, `print()` para mostrar texto en pantalla, `len()` para obtener la longitud de una lista o cadena, etc. Esas son funciones **predefinidas** (*built-in*) que Python ya ofrece. Pero también podemos crear **nuestras propias funciones** para las necesidades específicas de nuestros programas. En estas notas aprenderemos a definir y utilizar funciones en Python, desde lo más básico (declaración, llamada, parámetros, retorno) hasta conceptos más avanzados como ámbito de las variables, recursividad, funciones anónimas (*lambdas*), manejo de errores y buenas prácticas. Al final, incluiremos una introducción a cómo las funciones se utilizan en el contexto de la programación orientada a objetos (POO) en Python (es decir, los **métodos** de clase y el uso del parámetro `self` en instancias).

**Analogía visual**: Piensa en un programa como una receta de cocina larga. Sin funciones, sería como escribir la misma instrucción (por ejemplo, “picar cebolla”) cada vez que se necesita en diferentes partes de la receta. Con funciones, es como tener un sub-procedimiento llamado “picar cebolla” que describes una vez, y luego simplemente dices “ahora picar cebolla” cada vez que se requiera, confiando en que ese paso detallado ya está definido anteriormente.

Antes de sumergirnos en la sintaxis, veamos un panorama general: para usar una función primero hay que **definirla** (escribir el bloque de código que realiza la tarea y asignarle un nombre), y luego se puede **llamar** o invocar en cualquier parte posterior del programa para ejecutar esa tarea. A continuación, exploraremos cómo hacer esto en Python.

**Ejercicio introductorio**: Piensa en al menos tres tareas cotidianas que realices paso a paso (como hacer un sándwich, preparar un café o lavarte las manos). Escribe brevemente los pasos para una de estas tareas como si fuera un algoritmo. Luego, identifica si dentro de esa tarea hay pasos repetitivos o sub-tareas que podrías encapsular como “funciones” (por ejemplo, en hacer un sándwich podría haber una sub-tarea de cortar ingredientes). Esto te ayudará a entender cómo los programadores deciden qué partes del código convertir en funciones.

---

## Definición y llamada de funciones

En Python, para definir una función utilizamos la palabra reservada `def` seguida del **nombre de la función** y paréntesis `()` que pueden incluir una lista de **parámetros** (si la función recibe datos de entrada). Después, se coloca dos puntos `:` y en la línea siguiente (con indentación o sangría) el **cuerpo de la función**, es decir, el bloque de código que se ejecutará cuando llamemos a la función. Opcionalmente, podemos (y es buena práctica) incluir una cadena de documentación (*docstring*) encerrada entre triple comillas `"""` justo debajo de la definición, describiendo brevemente qué hace la función. Dentro del cuerpo, utilizaremos la sentencia `return` si queremos devolver un valor como resultado de la función. Veamos un ejemplo sencillo:

```python
# Definimos la función con def, nombre y parámetro(s)
def saludar(nombre):
    """Imprime un saludo personalizado en pantalla."""
    print(f"Hola, {nombre}! Bienvenido al programa.")

# Hasta aquí solo la hemos definido, no se ha ejecutado nada de su cuerpo.
# Ahora llamamos a la función para que realice su tarea:
saludar("Mariana")
saludar("Carlos")
```

Al ejecutar este código en Visual Studio Code (o cualquier entorno Python), la salida sería:

```
Hola, Mariana! Bienvenida al programa.
Hola, Carlos! Bienvenido al programa.
```

Observa cómo definimos la función `saludar` una vez, pero pudimos llamarla dos veces con distintos argumentos (`"Mariana"` y `"Carlos"`) obteniendo saludos personalizados para cada uno. Si necesitáramos saludar a 100 personas, no tendríamos que escribir la línea `print` 100 veces, bastaría con llamar a `saludar(nombre_persona)` tantas veces como sea necesario.

Vamos a desglosar los componentes de una definición de función con otro ejemplo más completo:

```python
def area_circulo(r):
    """Función que recibe el radio de un círculo y calcula su área."""
    area = 3.1415 * r**2   # calcula el área usando π * r^2
    return area            # devuelve el resultado

# Ejemplo de uso:
diametro = 10
resultado = area_circulo(diametro/2)  # pasamos el radio (mitad del diámetro)
print(f"El área de un círculo de diámetro {diametro} es {resultado}.")
```

Si corremos este código, veremos algo como:

```
El área de un círculo de diámetro 10 es 78.53750000000001.
```

En este ejemplo, la función `area_circulo` está definida con un parámetro `r` (el radio). Dentro, calcula la variable local `area` y luego la retorna. Afuera, calculamos el diámetro 10, y llamamos a `area_circulo(diametro/2)` para obtener el área. Fíjate que en la llamada le pasamos `diametro/2` como argumento, de modo que dentro de la función `r` tomará ese valor.

 ([Funciones — Fundamentos de Programación en Python](https://www2.eii.uva.es/fund_inf/python/notebooks/08_Funciones/Funciones.html)) *Figura: Encabezado y cuerpo de una función, y ejemplo de llamada. En verde se muestra el encabezado (`def` + nombre + parámetros), en naranja el cuerpo indentado (código interno y `return`), y debajo un ejemplo de llamada donde se usa la función definida.*  

Al definir una función, es crucial entender que **solo estamos creando el bloque de código nombrado, pero éste no se ejecuta inmediatamente**. El código dentro de la función se ejecutará **únicamente cuando la función sea llamada**. En el ejemplo anterior, si no hubiéramos escrito `area_circulo(diametro/2)`, nada ocurriría respecto a la función aunque esté definida. Además, como regla general, la definición de la función debe aparecer *antes* de su primera llamada en el código fuente (Python lee de arriba hacia abajo). Si intentas llamar a una función que aún no ha sido definida, obtendrás un error de nombre no definido.

Resumiendo el proceso:

- **Definición**: utilizamos `def nombre_funcion(parametros):` y luego escribimos el algoritmo dentro. En este momento no se ejecuta el algoritmo, solo se “guarda” bajo el nombre dado.
- **Llamada o invocación**: en cualquier parte posterior del código, escribimos `nombre_funcion(argumentos)` para ejecutar el bloque de código de la función. En ese instante Python salta a la función, ejecuta su cuerpo con los datos proporcionados y, si hay un `return`, devuelve el control al lugar de la llamada junto con el valor indicado.

Volviendo a la analogía: definir una función es como diseñar y montar una máquina que hará cierto trabajo; llamarla es como encender esa máquina con ciertos insumos para que realice el trabajo. Una vez construida (definida), podemos encenderla (llamarla) cuantas veces queramos.

**Ejemplo adicional**: Supongamos que estamos escribiendo un programa que analiza textos y queremos contar cuántas veces aparece un carácter específico en una frase. Podríamos crear una función:

```python
def contar_caracter(frase, caracter):
    """Cuenta cuántas veces aparece `caracter` en `frase`."""
    contador = 0
    for c in frase:
        if c == caracter:
            contador += 1
    return contador

# Uso de la función
texto = "programación"
print(contar_caracter(texto, 'o'))  # Debería imprimir 2, ya que "o" aparece dos veces.
print(contar_caracter(texto, 'r'))  # Debería imprimir 1.
print(contar_caracter(texto, 'z'))  # Debería imprimir 0 (no aparece).
```

Cada vez que llamamos `contar_caracter` con diferentes argumentos, la función ejecuta su código internamente y nos entrega el resultado sin que nosotros tengamos que reescribir la lógica del conteo para cada caso.

**Ejercicios prácticos (Definición y llamada)**:
1. *Saludo personalizado:* Escribe una función `bienvenida(usuario)` que tome el nombre de un usuario (string) y le dé la bienvenida imprimiendo un mensaje por pantalla. Por ejemplo, `bienvenida("Ana")` podría imprimir "Hola Ana, ¡que tengas un gran día!".
2. *Conversión de unidades:* Define una función `celsius_a_fahrenheit(grados_c)` que convierta una temperatura dada en grados Celsius a grados Fahrenheit y retorne el resultado. La fórmula es `F = C * 9/5 + 32`. Prueba la función con distintos valores.
3. *Área y perímetro:* Crea dos funciones, `calcular_area_rectangulo(base, altura)` y `calcular_perimetro_rectangulo(base, altura)`. La primera debe devolver el área de un rectángulo (base * altura) y la segunda el perímetro (2*(base+altura)). Luego, escribe código que use ambas funciones para mostrar el área y perímetro de un rectángulo de 5 x 3.

---

## Parámetros y argumentos

Al definir una función, los nombres que colocamos entre paréntesis (si los hay) se denominan **parámetros**. Son variables *locales a la función* que actuarán como “placeholders” o recipientes para los valores que se les pasen. Cuando *llamamos* a la función, los datos reales que proporcionamos en esa llamada se llaman **argumentos**. A veces en el vocabulario cotidiano ambos términos se usan indistintamente, pero técnicamente el parámetro es el nombre dentro de la definición de la función, y el argumento es el valor concreto que se pasa durante la llamada. En otros contextos, se les dice *parámetros formales* (a los de la definición) y *parámetros reales* (a los argumentos).

En Python podemos definir funciones con cualquier cantidad de parámetros, incluyendo cero. Veamos ejemplos:

```python
def anunciar():
    """Función sin parámetros que simplemente imprime un anuncio fijo."""
    print("¡Bienvenidos al sistema XYZ!")

def presentar_persona(nombre, edad):
    """Función con dos parámetros que imprime una presentación."""
    print(f"Me llamo {nombre} y tengo {edad} años.")
```

- `anunciar()` no requiere ningún parámetro; siempre hará lo mismo cada vez que se invoque.
- `presentar_persona(nombre, edad)` necesita que le proporcionemos un nombre y una edad en la llamada: por ejemplo `presentar_persona("Luis", 21)`.

**Argumentos posicionales vs nombrados**: Cuando llamamos a una función, podemos pasar los argumentos en el orden definido (esto se llama **paso posicional**), o especificar el nombre del parámetro seguido de un `=` y el valor (llamados argumentos **nombrados** o keyword arguments). Por ejemplo, con la función `presentar_persona` definida arriba, estas dos llamadas son equivalentes:

```python
presentar_persona("Ana", 30)
presentar_persona(edad=30, nombre="Ana")
```

En la primera usamos la posición: "Ana" va a `nombre` (primer parámetro) y `30` a `edad` (segundo parámetro). En la segunda, sin respetar el orden, indicamos explícitamente qué valor va a cada parámetro por nombre. Los argumentos nombrados aportan claridad y permiten flexibilidad en el orden, pero mezclarlos con posicionales tiene reglas (primero se listan posicionales y luego los nombrados, y cada parámetro solo se puede asignar una vez).

**Parámetros con valores por defecto**: Python permite asignar un valor predeterminado a parámetros en la definición de la función. Así, si al llamar no se provee un argumento para ese parámetro, se usará el valor por defecto indicado. Esto es muy útil para dar **opcionalidad** a ciertos argumentos. Veamos un ejemplo:

```python
def saludar(nombre, lenguaje="es"):
    """
    Saluda al usuario en diferentes idiomas.
    `nombre` es obligatorio, `lenguaje` es opcional con valor por defecto "es" (español).
    """
    if lenguaje == "es":
        print(f"Hola, {nombre}!")
    elif lenguaje == "en":
        print(f"Hello, {nombre}!")
    elif lenguaje == "fr":
        print(f"Bonjour, {nombre}!")
    else:
        print(f"Hola, {nombre}! (Idioma no soportado)")

saludar("Juan")              # Usa el valor por defecto 'es'
saludar("John", lenguaje="en")  # Especificamos inglés
saludar("Marie", "fr")       # Podemos pasar 'fr' posicionalmente también
```

Salida:
```
Hola, Juan!
Hello, John!
Bonjour, Marie!
```

En esta función, el segundo parámetro `lenguaje` tiene como valor por defecto `"es"`. La llamada `saludar("Juan")` no proporcionó `lenguaje`, así que dentro de la función `lenguaje` toma el valor `"es"` automáticamente. En los otros llamados, sobrescribimos el valor por defecto con `"en"` y `"fr"` respectivamente. Este mecanismo nos ahorra tener que definir múltiples funciones casi iguales o manejar argumentos "opcionales" manualmente. Observa que usamos un argumento nombrado en `saludar("John", lenguaje="en")` para mayor claridad, pero podríamos haber escrito `saludar("John", "en")` y habría funcionado por posición.

Otro ejemplo clásico: supongamos una función que valida si un número está dentro de un rango dado, pero queremos que por defecto ese rango sea, digamos, de 0 a 100. 

```python
def esta_en_rango(numero, minimo=0, maximo=100):
    """Devuelve True si numero está entre minimo y maximo (inclusive)."""
    return minimo <= numero <= maximo

print(esta_en_rango(50))        # True, usa rango 0-100
print(esta_en_rango(150))       # False, 150 no está en 0-100
print(esta_en_rango(5, -10, 10))  # True, 5 está entre -10 y 10
```

En la tercera llamada, sobrescribimos ambos valores por defecto. En las primeras dos, usamos el rango por defecto.

**Más sobre cómo se pasan los argumentos**: En algunos lenguajes, se habla de *paso por valor* (donde se copia el valor del argumento) o *paso por referencia* (donde se pasa una referencia al dato original) al invocar funciones. En Python, el modelo es a veces descrito como *paso por asignación de objetos* o *paso por referencia a objeto*. En términos simples, cuando pasamos un argumento a una función en Python, lo que ocurre internamente es similar a una asignación: la variable parámetro dentro de la función se *liga* al mismo objeto que el argumento externo apuntaba. Esto significa que:

- Si el objeto pasado es **inmutable** (número, cadena, tupla, etc.), dentro de la función no podemos modificar ese objeto original; cualquier intento de cambiar el valor realmente hará que la variable local apunte a un nuevo objeto (sin afectar el exterior).
- Si el objeto pasado es **mutable** (lista, diccionario, etc.), la función puede modificar el contenido del objeto y ese cambio se reflejará fuera de la función, porque tanto el argumento externo como el parámetro interno referencian al mismo objeto en memoria.

Veamos un ejemplo para aclarar esto:

```python
def duplica_valor(x):
    x = x * 2
    print(f"Dentro de la función, x = {x}")

valor = 5
duplica_valor(valor)
print(f"Después de llamar, valor = {valor}")
```

Salida:
```
Dentro de la función, x = 10
Después de llamar, valor = 5
```

Aquí `valor` es un entero (inmutable). Dentro de `duplica_valor`, la variable local `x` inicia referenciando el mismo 5 que `valor`. Pero al hacer `x = x * 2`, se crea un *nuevo* objeto entero 10 y `x` pasa a referenciar ese nuevo objeto. La variable global `valor` sigue apuntando al 5 original, por eso fuera de la función no cambió. Ahora intentemos algo similar con una lista (mutable):

```python
def agrega_elemento(lista):
    lista.append(99)
    print(f"Dentro de la función, lista = {lista}")

numeros = [1, 2, 3]
agrega_elemento(numeros)
print(f"Después de llamar, numeros = {numeros}")
```

Salida:
```
Dentro de la función, lista = [1, 2, 3, 99]
Después de llamar, numeros = [1, 2, 3, 99]
```

En este caso, `numeros` y `lista` referencian al mismo objeto lista. La función modifica la lista (le agrega un elemento) y ese cambio persiste fuera porque no se creó un nuevo objeto, sino que se alteró el existente.

Es importante entender este comportamiento para evitar sorpresas, especialmente con parámetros mutables. Una situación clásica a evitar es usar objetos mutables como valores por defecto de parámetros, ya que se evalúan una sola vez (en la definición de la función) y **se comparten entre llamadas**. Por ejemplo:

```python
def agregar_a_lista(n, lista=[]):
    lista.append(n)
    return lista

print(agregar_a_lista(5))   # [5]
print(agregar_a_lista(10))  # [5, 10] <- ¡sorpresa!
```

La segunda llamada mantuvo el 5 previo porque el valor por defecto `[]` se creó una vez y la lista se siguió utilizando. La recomendación es usar `None` como default y dentro de la función crear la lista si es None:

```python
def agregar_a_lista(n, lista=None):
    if lista is None:
        lista = []
    lista.append(n)
    return lista
```

**Resumen**: Los parámetros son variables locales dentro de la función que toman el valor de los argumentos que les pasemos en cada invocación. Podemos tener parámetros opcionales con valores por defecto, y debemos ser conscientes de la mutabilidad de los objetos que pasamos. Entender esto nos ayuda a predecir si un cambio dentro de la función afectará o no los datos externos.

**Ejercicios prácticos (Parámetros y argumentos)**:
1. *Diferencia posicional vs nombrado:* Define una función `potencia(base, exponente)` que eleve la base al exponente (por ejemplo, `potencia(2, 3)` debería devolver 8). Llama a esta función de dos maneras: una usando argumentos posicionales y otra usando argumentos nombrados (por ejemplo `potencia(exponente=3, base=2)`) para verificar que obtienes el mismo resultado.
2. *Valor por defecto:* Escribe una función `calcular_saludo(nombre, formal=True)` donde si `formal` es True, retorne un saludo formal del tipo "Buenos días, [nombre].", y si es False, retorne un saludo casual, por ejemplo "¡Hola [nombre]!". Prueba la función llamándola con y sin especificar el segundo argumento.
3. *Evitar efectos colaterales:* Crea una función `agregar_saludo(lista_nombres, saludo="Hola")` que reciba una lista de nombres y agregue ese saludo a cada nombre, devolviendo una nueva lista con los saludos. Por ejemplo, `agregar_saludo(["Ana", "Luis"], "Hi")` debería retornar `["Hi Ana", "Hi Luis"]`. Asegúrate de **no modificar** la lista original dentro de la función (pista: trabaja sobre una copia). Prueba la función y verifica que la lista original permanece sin cambios tras la llamada.

---

## Valores de retorno (`return`)

Muchas funciones realizan un cálculo o procesamiento y necesitan **devolver un resultado** al punto del código donde fueron invocadas. Para esto sirve la palabra clave `return`. Cuando Python encuentra `return` dentro de una función, **se detiene** la ejecución de la función en ese punto y el valor (o valores) especificado tras `return` es enviado de vuelta al llamador. 

Una función puede tener **cero, uno o múltiples retornos** en su cuerpo, dependiendo de diferentes condiciones lógicas, pero en el momento de ejecutarse solo uno de esos `return` entregará un resultado (y terminará la función). Si una función llega al final de su cuerpo sin ejecutar ningún `return`, Python retorna automáticamente el valor especial `None`, que básicamente significa “nada” o “ausencia de valor”. `None` es un objeto en Python que indica la falta de resultado útil.

Por ejemplo, consideremos una función que decide si un número es par o impar:

```python
def es_par(n):
    if n % 2 == 0:
        return True
    else:
        return False

resultado1 = es_par(4)   # True
resultado2 = es_par(7)   # False
```

Aquí la función `es_par` utiliza dos `return`: uno en el bloque del `if` y otro en el `else`. Según la condición, se ejecutará uno u otro, retornando True o False. Podríamos incluso simplificar esta función retornando directamente la comparación `n % 2 == 0` ya que esa expresión booleana da True/False, pero se muestra con if/else por claridad.

Otra función podría no necesitar retornar nada explícitamente, por ejemplo:

```python
def dibujar_linea():
    print("-----------")

x = dibujar_linea()
print(x)
```

Salida:
```
-----------
None
```

Aquí `dibujar_linea()` imprime una línea de guiones, pero no tiene `return`. Por lo tanto, asignar su resultado a `x` produce `None`. En muchos casos, funciones diseñadas para imprimir o modificar algo no retornan un valor útil, y usar `None` está bien (simplemente podríamos ignorar su retorno). Sin embargo, es importante distinguir **imprimir** de **retornar**. Imprimir es solo una acción que muestra algo en la consola, mientras que retornar es pasar un valor al entorno que llamó a la función. Si quisiéramos **usar** el resultado de una función en cálculos posteriores, esa función debería retornar valores en lugar de solo imprimir. Ejemplo:

```python
def sumar(a, b):
    print(a + b)

def sumar_correcto(a, b):
    return a + b

suma1 = sumar(3, 4)            # imprime 7, pero suma1 será None
suma2 = sumar_correcto(3, 4)   # no imprime nada, pero suma2 recibe 7
print("Resultado:", suma1, suma2)
```

Salida:
```
7
Resultado: None 7
```

Vemos que `sumar(3,4)` realiza la suma pero no la retornó, por lo que `suma1` no capturó ese resultado (quedó como None). En cambio `sumar_correcto` sí retornó el valor.

**Retornando múltiples valores**: En Python, técnicamente toda función retorna un único objeto. Sin embargo, ese objeto puede ser una tupla, lista u otro contenedor que agrupe varios valores. Python tiene una sintaxis conveniente que permite escribir algo como `return a, b, c` (separados por comas), lo cual empaqueta automáticamente `a`, `b` y `c` en una tupla. Esto hace parecer que la función retornó “múltiples valores”. Ejemplo:

```python
def operaciones(a, b):
    suma = a + b
    resta = a - b
    producto = a * b
    return suma, resta, producto

resultado = operaciones(5, 3)
print(resultado)            # (8, 2, 15)
```

Aquí `resultado` será una tupla con los tres cálculos. Podemos incluso hacer *desempaquetado* directamente:

```python
s, r, p = operaciones(5, 3)
print("Suma:", s, "- Resta:", r, "- Producto:", p)
```

Esto asigna cada elemento de la tupla retornada a una variable distinta. Este truco es útil para que una función entregue varios datos relacionados sin requerir estructuras de datos complejas.

**Flujo de ejecución con `return`**: Como mencionamos, en cuanto se ejecuta un `return`, la función termina. Por ello, cualquier código escrito después de un return en la misma suite indentada no se ejecutará (a menos que el return esté dentro de un if y haya otro camino lógico que no lo ejecute). Por ejemplo:

```python
def probar_return():
    print("Antes del return")
    return 42
    print("Esto no se imprime")

probar_return()
```

La segunda `print` nunca llegará a ejecutarse. Este comportamiento también se aprovecha para casos donde queremos “salir” tempranamente de una función si cierto criterio se cumple, evitando procesar más. Por ejemplo:

```python
def encontrar_negativo(lista):
    """Devuelve el primer número negativo en la lista, o None si no hay."""
    for num in lista:
        if num < 0:
            return num  # en cuanto encuentra un negativo, sale y lo retorna
    # Si terminó el for sin retornar:
    return None

print(encontrar_negativo([3, 7, -1, 10]))  # -1
print(encontrar_negativo([5, 8, 12]))      # None, no hay negativos
```

**Documentación del valor de retorno**: En la *docstring* de una función, suele ser útil indicar qué devuelve la función (si es que devuelve algo). Por convención, a veces se incluye una breve nota como “:return: descripción del valor retornado” en documentación más formal, pero en una docstring simple para clase basta con mencionarlo en lenguaje natural. Por ejemplo:

```python
def es_primo(n):
    """Determina si n es un número primo.
    Retorna True si es primo, False en caso contrario.
    """
    # ... (implementación)
    return resultado
```

**Ejercicios prácticos (Valores de retorno)**:
1. *Máximo de tres:* Escribe una función `max_de_tres(a, b, c)` que retorne el mayor de tres números dados. Prueba la función con diferentes tuplas de números (incluyendo algunos negativos).
2. *División segura:* Crea una función `divide(dividendo, divisor)` que retorne el resultado de la división. Si el divisor es 0, en lugar de intentar dividir (lo que causaría un error), que retorne por ejemplo la cadena `"Error: División por cero"` **sin imprimir nada** dentro. (Más adelante veremos otra forma de manejar esto con excepciones, pero por ahora hazlo con una condición).
3. *Conversión múltiple:* Diseña una función `conversor_temperaturas(celsius)` que retorne **dos** valores: la conversión de Celsius a Fahrenheit y a Kelvin. Usa la fórmula `F = C * 9/5 + 32` para Fahrenheit y `K = C + 273.15` para Kelvin. Muestra cómo recoger ambos resultados y mostrar un mensaje del tipo: "`X°C son Y°F o Z°K`".

---

## Ámbito de las variables (Scope)

El **ámbito** o alcance (*scope* en inglés) de una variable se refiere a la región del programa donde dicha variable es **visible** o accesible. En Python, las variables definidas dentro de una función tienen **ámbito local** a esa función, mientras que las definidas fuera de cualquier función tienen **ámbito global** (a todo el código del módulo). Entender el scope es fundamental para evitar confusiones con nombres de variables y para entender cómo se aislan los datos dentro de las funciones.

**Variables locales**: Son las que se crean dentro del cuerpo de una función (incluyendo los parámetros, que se tratan como locales también). Estas variables **solo existen mientras la función se está ejecutando** y no pueden ser accedidas desde fuera de la función. Cuando la función termina (sea por llegar al final o por un `return`), sus variables locales “mueren” y liberan su espacio. Si intentamos usar una variable local fuera de su función obtendremos un error de nombre no definido.

**Variables globales**: Son las definidas en el nivel superior del código (fuera de cualquier función, típicamente al inicio del script o módulo). Estas variables son accesibles por todo el código, incluyendo dentro de las funciones *a menos* que dentro de la función tengamos otra variable local con el mismo nombre, en cuyo caso la local *enmascara* a la global en ese ámbito.

Veamos un ejemplo para ilustrar:

```python
mensaje = "Hola"         # variable global

def cambiar_mensaje():
    mensaje = "Adiós"    # variable local (diferente de la global)
    print("Dentro de la función:", mensaje)

cambiar_mensaje()
print("Fuera de la función:", mensaje)
```

Salida:
```
Dentro de la función: Adiós
Fuera de la función: Hola
```

Dentro de `cambiar_mensaje()`, cuando hacemos `mensaje = "Adiós"`, estamos *creando una variable local* llamada `mensaje` (porque cualquier asignación dentro de la función por defecto crea variables locales). Esta variable local **no es la misma** que la global `mensaje` que vale `"Hola"`. Entonces el `print` interno muestra `"Adiós"`. Al terminar la función, la variable local desaparece. Afuera, la variable global `mensaje` quedó intacta con el valor `"Hola"` y así se imprime. Esto demuestra que las variables de distinto scope pueden tener el mismo nombre sin interferir, pero hay que ser cuidadoso para no confundirnos; usualmente es mejor usar nombres distintos a propósito para variables globales y locales a fin de evitar errores lógicos.

Si en una función **solo leemos** una variable y no la definimos, Python buscará en los scopes exteriores. Por ejemplo:

```python
contador = 10  # global
def ver_contador():
    print("Contador vale:", contador)

ver_contador()  # Imprime 10, accediendo a la global porque no hay una local
```

Esto funciona, pero **¡cuidado!** Si intentamos modificar una variable global dentro de una función, Python creará por defecto una local (como en el ejemplo de `mensaje`). Si nuestra intención realmente es modificar la global desde dentro, necesitamos declararlo explícitamente usando la palabra clave `global`. Por ejemplo:

```python
puntos = 0  # variable global

def anotar():
    global puntos        # indicamos que queremos referirnos a la variable global
    puntos = puntos + 1  # ahora esto suma al global, no crea una local
    print("Puntos dentro de la función:", puntos)

anotar()
print("Puntos global tras llamar función:", puntos)
```

Salida:
```
Puntos dentro de la función: 1
Puntos global tras llamar función: 1
```

Sin la declaración `global puntos` dentro de la función, la línea `puntos = puntos + 1` daría error, porque Python intentaría crear una variable local `puntos` y al mismo tiempo evalúa `puntos + 1` del lado derecho, encontrando que no hay una `puntos` local definida aún. Al usar `global`, le decimos a la función que `puntos` se refiere a la variable global ya existente.

Sin embargo, modificar variables globales dentro de funciones no es considerado una buena práctica en la mayoría de casos, porque tiende a hacer el seguimiento del estado del programa más complicado (las funciones dejan de ser autónomas y dependen de contexto externo). Es preferible **retornar** nuevos valores y asignarlos fuera si hace falta, o pasar la variable como parámetro y recibir el nuevo valor como retorno, en lugar de manipular globales directamente.

**Ámbito anidado (closures)**: Un detalle avanzado, pero lo mencionaremos brevemente: si defines una función *dentro de otra función*, la función interna puede ver las variables locales de la función externa (se dice que hay un scope *nonlocal*). Python tiene la palabra clave `nonlocal` para indicar que quieres asignar a una variable del scope externo inmediato (ni global ni local actual). Este es un concepto más propio de cierres y programación funcional, y quizás escapa al nivel introductorio, pero es bueno saber que existen scopes más allá de solo "global" y "local" en casos de funciones anidadas. Para un primer semestre, probablemente no definirás funciones dentro de funciones con frecuencia, por lo que no profundizaremos aquí.

**Recapitulando**:
- Variables definidas dentro de funciones (incluyendo parámetros) son locales a esa función.
- Variables definidas fuera de funciones son globales al módulo.
- Se puede acceder a globales dentro de funciones para lectura, pero para escribirlas hay que declararlas `global` (lo cual se debe hacer con moderación).
- Es una buena práctica mantener la mayoría de variables dentro de funciones (o pasarlas como parámetros) para evitar dependencias globales, excepto quizá constantes o configuraciones generales.

**Ejercicios prácticos (Scope)**:
1. *Local vs Global:* Escribe una variable global `saldo = 1000`. Luego, define una función `gastar(dinero)` que intente restar ese dinero del saldo. Dentro de la función, imprime el saldo después de gastar, y fuera de la función, imprime el saldo global luego de llamar a la función. Prueba llamar `gastar(100)` y analiza el resultado. Luego modifica la función usando `global saldo` para que la deducción afecte la variable global, y vuelve a probar.
2. *No modificar global:* Supón que tienes una lista global `inventario = ["espada", "escudo", "poción"]`. Crea una función `usar_objeto(objeto)` que elimine (pop) ese objeto de la lista global si existe, y muestre un mensaje del estilo "`Usaste [objeto]`". Dentro de la función, **no** uses la palabra `global` y en su lugar pasa la lista como parámetro para evitar modificar globales impuremente. Es decir, define la función como `usar_objeto(lista, objeto)`, pásale `inventario` al llamarla, y haz que retorne la lista modificada en caso de usar el objeto (o igual si no lo encontró). Muestra el inventario antes y después de usar un objeto.
3. *Funciones anidadas (reto avanzado):* Escribe una función externa `generar_multiplicador(n)` que dentro defina una función interna `multiplicar(x)` que retorne `x * n`. La función externa debe retornar la función interna. Esto crea un cierre (*closure*) donde la interna "recuerda" el valor de `n`. Usa esta técnica para crear, por ejemplo, `duplica = generar_multiplicador(2)` y `triplica = generar_multiplicador(3)`, y prueba `duplica(5)` y `triplica(5)` para ver los resultados (10 y 15, respectivamente). Este ejercicio es para entender ámbitos anidados y es un poco más avanzado.

---

## Recursividad (Funciones recursivas)

La **recursividad** es un concepto especial en el que una función **se llama a sí misma** como parte de su proceso. Una función recursiva soluciona un problema partiéndolo en subproblemas más pequeños del mismo tipo, y aplicándose a sí misma en esos subproblemas. Esto continúa hasta alcanzar una situación tan simple que la función ya no se llame a sí misma, resolviendo directamente ese caso base. 

En términos más simples: una función recursiva es como un martroshka (las muñecas rusas) o un espejo frente a otro espejo (efecto infinito): la definición de la función incluye una versión más pequeña de sí misma. Para que esto no se ejecute infinitamente, **debe haber al menos un caso base que rompa la recursión**. Toda función recursiva tiene dos partes importantes:
- **Caso(s) base**: condición(es) bajo las cuales la función *no* se llama a sí misma, sino que retorna directamente un resultado simple. Esto evita la recursión infinita.
- **Caso recursivo**: parte donde la función se llama a sí misma con argumentos reducidos o más simples, avanzando hacia el caso base.

Veamos un ejemplo clásico: el cálculo del factorial. El factorial de un número entero positivo `n` (escrito como `n!`) se define matemáticamente así:
- Caso base: `0! = 1` (por convenio, el factorial de 0 es 1).
- Caso recursivo: para `n > 0`, `n! = n * (n-1)!`. Es decir, el factorial de `n` es `n` multiplicado por el factorial de `n-1`.

Podemos implementar esto recursivamente en Python:

```python
def factorial(n):
    """Calcula el factorial de n (n!). n debe ser un entero no negativo."""
    if n < 0:
        raise ValueError("El factorial no está definido para números negativos")
    if n == 0 or n == 1:  # caso base: 0! = 1, 1! = 1
        return 1
    else:
        return n * factorial(n - 1)  # caso recursivo
```

Analicemos la función `factorial`:
- Si `n` es 0 o 1, retorna 1 inmediatamente (sin más llamadas).
- Si `n` es mayor, retorna `n * factorial(n-1)`. Aquí se hace la llamada recursiva a sí misma con `n-1`, acercándonos cada vez más a los casos base. Por ejemplo, `factorial(5)` hará `5 * factorial(4)`. A su vez `factorial(4)` hará `4 * factorial(3)`, y así sucesivamente hasta `factorial(1)` que devuelve 1. Luego la cadena de llamadas se resuelve hacia atrás: `factorial(2)` retorna `2 * 1 = 2`, `factorial(3)` retorna `3 * 2 = 6`, `factorial(4)` retorna `4 * 6 = 24`, y finalmente `factorial(5)` retorna `5 * 24 = 120`.

Probemos la función:

```python
print(factorial(5))  # 120
print(factorial(0))  # 1
# print(factorial(-3))  # Descomentar para ver que lanza ValueError
```

Otro ejemplo típico de recursión es la **serie de Fibonacci**: una secuencia donde cada número es la suma de los dos anteriores: 0, 1, 1, 2, 3, 5, 8, 13, ... Matemáticamente:
- Caso base: fib(0) = 0, fib(1) = 1.
- Caso recursivo: fib(n) = fib(n-1) + fib(n-2) para n > 1.

Implementación recursiva:

```python
def fibonacci(n):
    """Retorna el n-ésimo número de Fibonacci (0-indexed: fibonacci(0)=0, fibonacci(1)=1)."""
    if n < 0:
        raise ValueError("Índice de Fibonacci no puede ser negativo")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
```

Esta función llama a sí misma dos veces por cada cálculo (excepto en casos base). Por ejemplo, `fibonacci(4)` internamente hará `fibonacci(3) + fibonacci(2)`, y cada uno de esos hará más llamadas.

**Visualización de la recursividad**: Puede ser un poco desafiante imaginar el flujo de ejecución de una función que se llama a sí misma. Una manera es pensar en la **pila de llamadas**: cada vez que se invoca una función (sea recursiva o no), Python apila un *marco* con las variables locales de esa llamada. En recursividad, muchos marcos de la misma función se apilan. Siguiendo el ejemplo de `factorial(5)`:
- Llamamos `factorial(5)`. (Pila: factorial(5) esperando resultado de 5 * factorial(4))
- Dentro necesita `factorial(4)`. Llamada recursiva: (Pila: factorial(4) esperando 4 * factorial(3); debajo está factorial(5) esperando).
- Llama `factorial(3)`... (se apilan factorial(3), factorial(2), factorial(1) análogamente)
- `factorial(1)` retorna 1 (caso base). Ahora se empieza a “desapilar”:
  - `factorial(2)` que estaba esperando recibe 1 y retorna 2*1 = 2.
  - `factorial(3)` recibe 2 y retorna 3*2 = 6.
  - `factorial(4)` recibe 6 y retorna 4*6 = 24.
  - `factorial(5)` recibe 24 y retorna 5*24 = 120.
- Pila vacía; ya tenemos el resultado final.

Cada llamada recursiva tiene sus propias variables (en este caso su propia `n`). En ningún momento las `n` de distintas llamadas chocan, porque viven en diferentes “instancias” de la función.

**Cuándo usar recursividad**: Cualquier algoritmo recursivo se puede transformar en uno iterativo (por ejemplo, factorial se puede calcular con un loop for fácilmente). Sin embargo, hay problemas que se describen de forma más natural recursivamente, como el recorrido de estructuras jerárquicas (árboles, gráficos), fractales, operaciones en listas enlazadas, etc. Python permite recursividad, pero a diferencia de algunos lenguajes, **no optimiza la recursividad de cola** (tail recursion), lo que significa que si la recursión es muy profunda (muchas llamadas anidadas), se puede agotar la pila (StackOverflow). Existe un límite predeterminado de recursión en Python (generalmente 1000 llamadas recursivas de profundidad) para proteger de bucles infinitos. Este límite se puede cambiar, pero en general si necesitas más profundidad es señal de que tal vez se requiera un enfoque iterativo.

Para primeros semestres, recursividad es un concepto importante más por el desarrollo de la logica de programación de cada persona que por su uso inmediato. Es valioso practicarlo para entender nuevas formas de pensar algoritmos.

**Ejercicios prácticos (Recursividad)**:
1. *Cuenta regresiva:* Escribe una función recursiva `cuenta_regresiva(n)` que imprima del n hasta 0. Por ejemplo, `cuenta_regresiva(5)` imprimiría 5, 4, 3, 2, 1, 0 en líneas separadas. Define el caso base cuando `n < 0` (por ejemplo, que no haga nada o imprima "Despegue!" al llegar a -1, como si fuera un lanzamiento cohete).
2. *Sumatoria recursiva:* Crea una función recursiva `sumatoria(n)` que calcule la suma de todos los números enteros de 1 a n. (La sumatoria de 5 sería 1+2+3+4+5 = 15). Define el caso base apropiado.
3. *Invertir cadena:* Implementa una función recursiva `invertir_cadena(texto)` que retorne la cadena al revés. Por ejemplo `invertir_cadena("hola")` debe dar `"aloh"`. Pista: el caso base puede ser la cadena vacía o de longitud 1 (que se devuelve igual), y el caso recursivo tomar el primer carácter y colocarlo al final de la recursión de lo restante.

---

## Funciones anónimas (expresiones *lambda*)

En Python, además de definir funciones de la forma tradicional con `def` y un nombre, existe la posibilidad de crear **funciones anónimas**, también conocidas como **funciones lambda**. Se les llama “anónimas” porque, a diferencia de las funciones normales, estas no requieren un nombre explícito al ser definidas; son esencialmente expresiones que generan una función *sin* declarar un `def` estándar.

La sintaxis básica de una función lambda es:
```python
lambda parametros: expresion
```
Por ejemplo, una función normal para sumar dos números podría ser:
```python
def suma(a, b):
    return a + b
```
Equivalente en lambda:
```python
lambda a, b: a + b
```
Esta expresión produce una función que toma `a` y `b` y retorna `a+b`. Pero nota algo: esa función no tiene nombre. Si queremos usarla, tendríamos que asignarla a una variable o llamarla inmediatamente. Por ejemplo:

```python
# Asignándola a una variable
mi_suma = lambda a, b: a + b
print(mi_suma(3, 4))  # 7

# Llamándola al vuelo
print((lambda a, b: a + b)(5, 6))  # 11
```

¿Por qué existen las lambdas? Principalmente, para casos donde se necesita una función pequeña y simple *sólo una vez*, típicamente como argumento para otra función. Son útiles para escribir código más compacto en situaciones como:
- Sortear (ordenar) una lista de objetos basado en una clave, usando el parámetro `key` de la función `sorted` o `.sort()`.
- Aplicar una función a cada elemento de una lista con funciones como `map` o filtrar elementos con `filter`.
- En interfaces gráficas o callbacks, donde quieres definir la acción a realizar en el momento sin crear una función separada con nombre.

**Ejemplo práctico**: Supongamos que tenemos una lista de palabras y queremos ordenarlas por longitud en lugar de alfabéticamente. Podemos usar `sorted(lista, key=funcion)` donde `funcion` calcule la clave de ordenamiento para cada elemento. En este caso, la clave es la longitud de la palabra, que podríamos obtener con una lambda:

```python
palabras = ["zanahoria", "sol", "elefante", "luz"]
ordenadas = sorted(palabras, key=lambda palabra: len(palabra))
print(ordenadas)  # ['sol', 'luz', 'zanahoria', 'elefante']
```

Aquí la lambda `lambda palabra: len(palabra)` actúa como una función que recibe cada palabra y devuelve su longitud. `sorted` utiliza esos resultados para ordenar.

Otro ejemplo con `map`: digamos que tenemos una lista de números y queremos obtener una nueva lista con el doble de cada número. Sin lambda haríamos:

```python
def doble(x):
    return x * 2

numeros = [1, 2, 3, 4]
dobles = list(map(doble, numeros))
print(dobles)  # [2, 4, 6, 8]
```

Con lambda, podemos no definir `doble` por separado:

```python
numeros = [1, 2, 3, 4]
dobles = list(map(lambda x: x * 2, numeros))
print(dobles)  # [2, 4, 6, 8]
```

Es exactamente lo mismo pero ahorrando algo de espacio. 

**Limitaciones de lambdas**: En Python, una lambda **solo puede contener una expresión**, no varias líneas de código ni declaraciones complejas. Esto significa que no puedes hacer asignaciones, ni usar `while`, `try`, etc., dentro de una lambda. Solo cosas que produzcan un valor en una sola expresión. Por esta razón, las lambdas suelen ser para lógica sencilla. Si la operación es compleja o requiere varias etapas, es más claro usar una función normal con `def`.

También, como no tienen nombre, las lambdas aparecen en los errores o *tracebacks* de forma anónima (`<lambda>`), lo que puede ser menos claro al depurar. Un dicho popular (incluso reflejado en la documentación oficial de Python) es: *"Las lambdas de Python son solo una notación abreviada si te da pereza definir una función"*. Es decir, son azúcar sintáctico para casos simples.

**Cuando usar lambda vs def**:
- Si necesitas una función reutilizable, bien documentada, y quizás más larga que una simple expresión, usa `def` y dale un nombre y docstring.
- Si necesitas una función muy breve para pasarla como argumento y probablemente no la volverás a usar, lambda puede ser conveniente.
- Evita hacer lambdas demasiado complicadas; podrían restar legibilidad.

**Ejercicios prácticos (Lambdas)**:
1. *Ordenamiento custom:* Tienes la lista `frutas = ["manzana", "kiwi", "banana", "cereza"]`. Usa `sorted` con una lambda para ordenarlas alfabéticamente **por la última letra** de cada palabra.
2. *Filtro:* Dada la lista `numeros = list(range(1, 21))` (números del 1 al 20), usa `filter` con una lambda para obtener solo los números pares de esa lista. (Recuerda envolver con `list(...)` el resultado de filter para obtener una lista final).
3. *Map combinado:* Dada una lista de nombres en minúscula, por ejemplo `nombres = ["ana", "CARLOS", "Pedro", "maria"]`, usa `map` con una lambda para normalizar los nombres de manera que queden con la primera letra mayúscula y el resto minúsculas (tip: puedes usar `str.capitalize()` o manipular con slices). Combina esto quizás con otra función o lista por comprensión, pero intenta con lambda dentro de map.

---

## Manejo de errores y excepciones en funciones

Cuando escribimos funciones, no solo debemos pensar en la *lógica ideal* (lo que debe hacer con datos válidos), sino también en cómo manejar situaciones inesperadas o **errores**. Por ejemplo, si escribimos una función que divida dos números, ¿qué pasa si el divisor es cero? O si tenemos una función que abre un archivo, ¿qué pasa si el archivo no existe? En programación, los errores en tiempo de ejecución producen **excepciones**. Una excepción es un evento que interrumpe el flujo normal del programa, generalmente acompañada de un mensaje de error y un tipo (ej: `ZeroDivisionError`, `TypeError`, `FileNotFoundError`, etc.).

**Lanzar excepciones (`raise`)**: Dentro de nuestras funciones, podemos detectar condiciones inválidas y lanzar una excepción manualmente usando la palabra clave `raise`. Ya vimos un ejemplo en la función factorial donde hacíamos:
```python
if n < 0:
    raise ValueError("El factorial no está definido para números negativos")
```
Aquí se lanza una excepción `ValueError` con un mensaje explicativo. Lanzar nuestras propias excepciones es útil para **asegurar la validez de los datos**. Equivale a decir: "mi función no sabe manejar este caso, así que le informo al llamador de que hubo un problema". Al lanzar, la función termina inmediatamente (similar a un return, pero señalando un error).

Python tiene muchas excepciones predefinidas (ValueError, TypeError, ZeroDivisionError, FileNotFoundError, etc.), y también puedes definir excepciones propias (clases que heredan de Exception), pero para empezar es suficiente reutilizar las existentes.

**Capturar excepciones (`try/except`)**: Por otro lado, cuando llamamos funciones que pueden fallar, podemos **capturar** esas excepciones para manejar el error en lugar de que el programa se detenga abruptamente. La sintaxis es:

```python
try:
    # código que puede lanzar excepciones
except TipoDeExcepcion as e:
    # código para manejar esa excepción
```

Podemos tener múltiples except para distintos tipos de error, un except genérico para cualquier excepción, un bloque `else` que se ejecuta si no hubo errores, y un bloque `finally` que se ejecuta siempre (haya o no error), generalmente usado para liberar recursos.

Veamos un ejemplo de función robusta que maneja sus errores internamente:

```python
def divide_seguro(a, b):
    """Intenta dividir a/b y manejar errores comunes."""
    try:
        resultado = a / b
    except ZeroDivisionError:
        print("Error: no se puede dividir por cero.")
        return None  # retornamos None o podríamos retornar un indicador de error
    except TypeError:
        print("Error: ambos argumentos deben ser números.")
        return None
    else:
        # Si no hubo excepción
        return resultado
    # (Opcionalmente, finally: aquí no lo necesitamos)
```

Probemos distintos casos:

```python
print(divide_seguro(10, 2))    # 5.0 (caso normal)
print(divide_seguro(5, 0))     # Maneja división por cero
print(divide_seguro("5", 2))   # Maneja tipo incorrecto
```

Salida:
```
5.0
Error: no se puede dividir por cero.
None
Error: ambos argumentos deben ser números.
None
```

En esta función, en lugar de propagar las excepciones, decidimos atraparlas (`except`) y manejarlo imprimiendo un mensaje y devolviendo `None`. Dependiendo del diseño, podríamos optar por simplemente `raise` de nuevo la excepción después de loguear, o retornar un valor especial. Lo importante es que **identificamos el problema y no dejamos que la función se estrelle sin control**. Sin el try/except, una división por cero habría causado un error que si no es capturado, detiene el programa.

Otra filosofía es no atrapar las excepciones dentro de la función, sino documentar que la función puede lanzar tal o cual excepción, y que sea responsabilidad del *caller* usar try/except al llamarla si desea manejarlo. Por ejemplo, podríamos haber escrito `divide(a, b)` sin try/except, pero sabiendo que Python lanzará ZeroDivisionError o TypeError automáticamente, y dejar que quien llame decida qué hacer. En una aplicación real, a veces tiene más sentido capturar excepciones en niveles superiores (por ejemplo, en la interfaz de usuario, para mostrar un error de forma amigable), en lugar de enterrar prints dentro de la lógica.

**Bloque `finally`**: Se usa para tareas de limpieza. Por ejemplo, si tu función abre un archivo o adquiere algún recurso externo (conexión de red, etc.), debes asegurarte de liberarlo aunque ocurra un error. Un ejemplo hipotético:

```python
def leer_lineas_archivo(nombre_archivo):
    try:
        f = open(nombre_archivo, 'r')
        lineas = f.readlines()
    except FileNotFoundError:
        print("No se encontró el archivo", nombre_archivo)
        return []
    finally:
        # Este bloque se ejecutará siempre, ocurra o no error
        try:
            f.close()
        except NameError:
            # Si f nunca se definió porque no se pudo abrir
            pass
    return lineas
```

En este ejemplo, usamos `finally` para cerrar el archivo pase lo que pase. (En código moderno usaríamos el contexto `with open(...) as f:` para no preocuparnos de cerrar, pero es ilustrativo del uso de finally).

**Manejo de errores como buena práctica**: Es importante tener en cuenta que no debemos atrapar excepciones indiscriminadamente sin procesarlas. Por ejemplo, hacer:

```python
try:
    algo_peligroso()
except Exception:
    pass  # silencia todo error
```

Es mala práctica a menos que *sepamos exactamente* por qué queremos ignorar cualquier error. Silenciar errores puede ocultar bugs serios. Lo preferible es capturar únicamente las excepciones que esperamos y sabemos manejar, y dejar que otras inesperadas suban (o al menos loguearlas). En resumen, **sé específico en las excepciones que manejas**.

También, si tu función detecta un problema en la entrada, a veces es mejor **lanzar una excepción** que retornar silenciosamente un resultado incorrecto. Por ejemplo, si escribes una función `calcular_raiz_cuadrada(x)` y alguien le pasa `x` negativo, quizás lo más claro es lanzar `ValueError("No se puede calcular raíz cuadrada de número negativo")` en lugar de retornar algo arbitrario. Así el usuario de la función sabe que usó mal la función.

**Ejercicios prácticos (Manejo de errores)**:
1. *Validación de entrada:* Crea una función `calcular_promedio(numeros)` que reciba una lista de números y retorne el promedio. Debe lanzar una excepción `ValueError` si la lista está vacía (con un mensaje tipo "lista vacía, no se puede calcular promedio"). Escribe código que llame a esta función con una lista vacía dentro de un bloque try/except para capturar el error y mostrar un mensaje de aviso al usuario.
2. *Conversion segura:* Escribe una función `a_int(cadena)` que intente convertir una cadena a entero usando `int(cadena)`. Si la conversión lanza `ValueError` (por ejemplo al pasar "abc"), captura esa excepción y retorna `None`. Prueba la función con varias entradas: "123" (válido), "3.14" (no válido para int), "abc" (no válido).
3. *Rethrow (avanzado):* Supón una función `procesar_dato(x)` que debe cumplir que x sea positivo. Implementa dentro un try/except que capture si x es negativo lanzando un `ValueError` con `raise` (lo vimos), pero luego de capturarlo, realiza alguna acción de limpieza (por ejemplo imprimir "se recibió un número negativo") y **vuelve a lanzar** la excepción para que el llamador principal la trate. En el llamador, maneja esa excepción con except mostrando "Error en procesar_dato: ..." junto con el mensaje de la excepción.

---

## Buenas prácticas al escribir funciones

Ya conocemos la teoría y práctica de cómo funcionan las funciones en Python. Ahora abordemos algunas **buenas prácticas** que nos ayudarán a escribir funciones más claras, útiles y mantenibles:

- **Responsabilidad única**: Una función debe idealmente encargarse de *una sola cosa o tarea específica*. Si empiezas a escribir una función y ves que hace demasiadas cosas, considera separarla en funciones más pequeñas. Esto sigue el principio de responsabilidad única y favorece la reutilización y pruebas. Además, funciones más pequeñas son más fáciles de entender y depurar.

- **Nombres descriptivos**: El nombre de la función debe indicar claramente qué hace. Use verbos si la función realiza una acción (ej: `calcular_total`, `obtener_usuario`, `imprimir_reporte`). Evita nombres vagos como `procesar_datos` a menos que el contexto sea obvio. Prefiere `suma_enteros` sobre `func1`, por ejemplo. En Python, los nombres de funciones se escriben en minúsculas y con palabras separadas por guiones bajos (snake_case), según la guía de estilo PEP8.

- **Documentación (docstrings)**: Siempre que una función no sea totalmente trivial, añade una docstring breve pero útil. Indica **qué hace** la función, qué significan sus parámetros (si no es obvio), y qué retorna o efectos secundarios tiene. Esto es invaluable para otros (y para ti mismo en el futuro) al usar la función sin tener que leer su implementación. Por ejemplo:
  ```python
  def convertir_mayusculas(texto):
      """Devuelve el texto dado con todas sus letras en mayúsculas."""
      return texto.upper()
  ```
  Es breve pero deja claro el propósito.

- **Evitar efectos secundarios inesperados**: Las funciones *pueden* modificar variables globales o estructuras mutables pasadas como argumentos, pero esto debe ser consciente. Si tu función modifica algo externo (por ejemplo, altera una lista pasada por referencia), debería quedar claro en el nombre o documentación, o mejor aún, evítalo si puedes y trabaja retornando nuevos valores. Las funciones llamadas **puras** (sin efectos secundarios, que solo usan sus parámetros y retornan algo sin cambiar nada fuera) son más seguras y fáciles de testear. Por ejemplo, es mejor que una función `duplicar_lista(lista)` retorne una nueva lista duplicada en lugar de modificar la lista original in-place, a menos que el propósito explícito sea modificarla.

- **Tamaño y complejidad**: Si una función supera ~50 líneas, podría ser señal de que hace demasiado. Intenta dividir código complejo en sub-funciones. También evita anidar demasiados niveles de control dentro de una función (por legibilidad).

- **Manejo de errores**: Valida los parámetros de entrada de la función si es probable que se usen incorrectamente, y proporciona mensajes de error claros ya sea vía `raise` o retornos especiales. Ejemplo: en una función `buscar_elemento(lista, objetivo)`, podrías decidir qué hacer si la lista es None o si el objetivo no está; quizás retornar -1 o None, pero documenta esa decisión.

- **Uso de funciones integradas**: A veces antes de escribir una función, piensa si Python ya provee algo similar. Por ejemplo, antes de escribir tu propia función para ordenar, considera `sorted`; antes de escribir para longitud, `len`; etc. Reusar librerías estándar es bueno.

- **No repetir código (DRY)**: Si encuentras que ciertas líneas se repiten en varios lugares, conviene agruparlas en una función. Por ejemplo, si en varias partes del programa formateas una cadena de cierta manera compleja, haz una función `formatear_cadena(x)`.

- **Organización**: En un archivo Python (script o módulo), suele ponerse las definiciones de funciones al inicio (tras imports y constantes globales), y luego una sección principal que use esas funciones. Alternativamente, para proyectos más grandes, se pueden agrupar funciones relacionadas en módulos (archivos) separados.

- **Testing unitario**: Aunque quizás en primer semestre no se vea a profundidad, es muy útil escribir pequeñas pruebas para cada función (incluso manualmente en un `main` o usando asserts) para verificar que con entradas conocidas sale lo esperado. Esto asegura que tu función cumple lo que promete. Más adelante aprenderás frameworks como `unittest` o `pytest` para automatizar pruebas.

- **Comentarios y legibilidad**: Dentro de la función, comenta secciones complicadas o poco obvias. Pero evita comentar lo evidente. Por ejemplo, un comentario `# sumo 1 a i` sobre la línea `i += 1` no agrega valor; sin embargo, un comentario `# usando fórmula de Bhaskara para resolver cuadrática` antes de un cálculo matemático sí ayuda. Y usa espacios y saltos de línea para separar lógica en bloques digestibles.

- **Retorno consistente**: Si tu función retorna en algunos casos un tipo de dato y en otros casos otro, documentalo bien. Por ejemplo, Python permite retornar `None` o un número; eso está bien, pero asegúrate de dejar claro cuándo ocurre cada caso. Una mala práctica es por error no retornar nada en algún camino lógico, provocando un None inesperado.

- **Evita variables globales dentro de funciones**: A menos que sea necesario, no te apoyes en variables globales dentro de la función. Pásalas como argumentos. Esto hace la función más general y fácil de testear (porque no depende de contexto externo).

- **Optimización vs claridad**: Es tentador a veces hacer funciones muy compactas (especialmente con lambdas o comprensiones de lista), pero prioriza la claridad sobre la micro-optimización. Solo optimiza (por ejemplo, usando recursividad vs iteración, o viceversa) si descubres que es un cuello de botella real en tu programa.

**Ejemplo integrador**: Vamos a escribir una función que aplique varias de estas buenas prácticas. Supongamos un requerimiento: necesitamos una función que dado un texto, cuente cuántas letras de cada tipo contiene (frecuencia de caracteres), ignorando espacios y convirtiendo todo a minúsculas para agrupar mayúsculas con minúsculas. Además, queremos que opcionalmente imprima un gráfico sencillo de barras con el resultado. Esto suena como varias tareas: limpiar el texto, contar, y posiblemente graficar. Aplicando responsabilidad única, podemos separar en subfunciones.

```python
def limpiar_texto(texto):
    """Devuelve el texto solo con letras minúsculas, sin espacios ni caracteres especiales."""
    filtrado = []
    for ch in texto.lower():
        if 'a' <= ch <= 'z':  # si es letra alfabética
            filtrado.append(ch)
    return "".join(filtrado)

def contar_letras(texto):
    """Devuelve un diccionario con el conteo de cada letra en el texto."""
    conteo = {}
    for ch in texto:
        conteo[ch] = conteo.get(ch, 0) + 1
    return conteo

def mostrar_histograma(conteo):
    """Imprime un histograma de frecuencias dado un diccionario {letra: conteo}."""
    for letra, freq in sorted(conteo.items()):
        barras = '#' * freq
        print(f"{letra}: {barras}")

def analizar_texto(texto, graficar=False):
    """
    Analiza un texto y devuelve la frecuencia de cada letra.
    Si graficar=True, también imprime un histograma de barras.
    Ignora espacios y no distingue mayúsculas/minúsculas.
    """
    texto_limpio = limpiar_texto(texto)
    frecuencias = contar_letras(texto_limpio)
    if graficar:
        mostrar_histograma(frecuencias)
    return frecuencias

# Ejemplo de uso:
resultado = analizar_texto("Hola Mundo", graficar=True)
print(resultado)
```

Si ejecutamos lo anterior, `analizar_texto("Hola Mundo", graficar=True)` podría imprimir algo como:
```
a: ##
d: #
h: #
l: #
m: #
n: #
o: ##
u: #
{'h': 1, 'o': 2, 'l': 1, 'a': 2, 'm': 1, 'u': 1, 'n': 1, 'd': 1}
```

Aquí aplicamos:
- Funciones pequeñas: `limpiar_texto`, `contar_letras`, `mostrar_histograma` cumplen tareas individuales. Esto facilita probar cada una por separado.
- Nombres descriptivos y docstrings explicativos.
- `analizar_texto` combina todo y ofrece la opción de graficar con un parámetro booleano (valor por defecto False, implícito).
- Usamos estructuras de datos (diccionario) y métodos apropiados (`dict.get` para conteo).
- La salida del histograma está ordenada alfabéticamente por letra usando `sorted(conteo.items())`, para consistencia.

**Ejercicios prácticos (Buenas prácticas)**:
1. *Refactorización:* Toma uno de los ejercicios anteriores que hayas resuelto (por ejemplo, la sumatoria recursiva o el conversor de temperaturas) e intenta refactorizarlo si es posible para mejorar su claridad o dividirlo en funciones más pequeñas. Compara la versión original y la refactorizada y nota si es más legible.
2. *Documentar y probar:* Escribe una función `calcular_mediana(numeros)` que calcule la mediana de una lista de números. Documenta la función adecuadamente en la docstring (definiendo qué es mediana si es necesario). Luego, escribe algunas pruebas manuales: listas con cantidad par de elementos, impar de elementos, lista vacía (¿qué debería hacer en este caso? quizás lanzar ValueError). Asegúrate de manejar ordenamiento de la lista dentro de la función sin alterar la lista original (podrías usar sorted en lugar de sort).
3. *Pensar en reusabilidad:* Imagina que tienes que escribir una función `imprimir_cuadrado(n)` que imprime un cuadrado de asteriscos de n por n. Por ejemplo, `imprimir_cuadrado(3)` imprime:
   ```
   ***
   ***
   ***
   ```
   Ahora, piensa si pudieras hacer esa función más flexible: tal vez que por defecto use `*` pero que puedas pasar opcionalmente otro carácter para los bordes, o que puedas elegir si el interior está relleno o vacío (solo bordes). Sin implementar todo, diseña la firma de la función (los parámetros necesarios con defaults) siguiendo buenas prácticas, y describe cómo organizarías la lógica interna. Esto es más un ejercicio de diseño que de código.

---

## Funciones y métodos en Programación Orientada a Objetos (POO) en Python

Hasta ahora hemos hablado de funciones *libres*, es decir, definidas de manera independiente. En la programación orientada a objetos, las funciones asociadas a una **clase** (y por tanto a sus instancias) se denominan **métodos**. En el fondo, un método no es más que una función definida dentro de la sintaxis de una clase, pero tiene algunas particularidades en Python.

Veamos una breve introducción práctica a POO para entender los métodos:

Una **clase** es como un molde o modelo que define atributos (datos) y métodos (comportamiento) que tendrán los objetos creados a partir de esa clase (llamados instancias). Cuando definimos un método dentro de una clase en Python, debemos incluir siempre un primer parámetro que por convención se llama `self`. Este `self` representa la instancia sobre la que el método será llamado. Python lo maneja automáticamente: tú escribes `objeto.metodo(arg1, arg2)`, y Python detrás de escena convierte eso en `Clase.metodo(objeto, arg1, arg2)` pasando la instancia como `self`.

Miremos un ejemplo concreto:

```python
class Persona:
    def __init__(self, nombre, edad):
        # Método constructor, inicializa la instancia
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        # Método de instancia que usa el atributo self.nombre
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Crear instancias (objetos) de la clase Persona
p1 = Persona("Alice", 20)
p2 = Persona("Bob", 25)

# Llamar al método saludar en cada instancia
p1.saludar()  # Hola, mi nombre es Alice y tengo 20 años.
p2.saludar()  # Hola, mi nombre es Bob y tengo 25 años.
```

Aquí definimos la clase `Persona` con:
- Un método especial `__init__` (constructor) que se ejecuta al crear una nueva Persona, encargado de asignar el nombre y la edad al nuevo objeto (`self.nombre = nombre` crea un atributo en la instancia).
- Un método regular `saludar(self)` que al ser llamado, accede a `self.nombre` y `self.edad` para imprimir un mensaje.

Notemos varias cosas:
- No llamamos `__init__` directamente; Python lo llama cuando hacemos `Persona("Alice", 20)`. Ese constructor recibe los argumentos y los asigna a la instancia `self`.
- Al llamar `p1.saludar()`, no pasamos ningún argumento entre paréntesis, pero internamente `p1` se pasa como `self` automáticamente. Por eso definimos `saludar` con `self` aunque no le enviemos nada explícito al llamarlo.
- Dentro de `saludar`, usamos `self.nombre` y `self.edad` que fueron establecidas durante la construcción del objeto. Cada instancia tiene sus propios atributos, así `p1.nombre` es "Alice" y `p2.nombre` es "Bob", y el método saludar usa el valor correspondiente según la instancia que invoca.

En la terminología:
- `__init__` y `saludar` son métodos **de instancia** porque operan sobre una instancia (`self`) y pueden acceder/modificar su estado.
- `nombre` y `edad` son atributos de instancia.

En Python también existen métodos de clase y estáticos:
- **Métodos de clase** (`@classmethod`): reciben la clase como parámetro (convención: `cls` en lugar de `self`). Se definen con un decorador `@classmethod` encima. Sirven para operaciones relacionadas con la clase en sí, no con instancias individuales (por ejemplo, construir un objeto de formas alternativas, contadores de instancias, etc.).
- **Métodos estáticos** (`@staticmethod`): no reciben ni instancia ni clase automáticamente. Son básicamente funciones normales que se incluyen dentro de la clase por organización lógica. Se definen con `@staticmethod`. Útiles cuando el método no necesita acceder a nada de la instancia ni de la clase, pero tiene relación temática con la clase.
  
Ejemplo breve de estos (sin profundizar demasiado):

```python
class Circulo:
    PI = 3.14159  # atributo de clase (constante compartida)

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return Circulo.PI * (self.radio ** 2)  # usar atributo de clase

    @classmethod
    def unitario(cls):
        # Método de clase para crear un círculo de radio 1
        return cls(1)

    @staticmethod
    def descripcion():
        return "Un círculo es una figura geométrica en 2D donde todos los puntos están a la misma distancia del centro."
```

Uso:
```python
c = Circulo(5)
print(c.area())                # calcula área con radio 5
c_unit = Circulo.unitario()    # crea un círculo de radio 1 usando método de clase
print(c_unit.area())           # área con radio 1
print(Circulo.descripcion())   # llamar método estático desde la clase
```

Notar:
- `area` es de instancia: usa `self.radio`. 
- `unitario` es de clase: recibe `cls` (la propia clase Circulo) y retorna `cls(1)` que equivale a `Circulo(1)`, un nuevo círculo.
- `descripcion` es estático: no usa self ni cls, se puede llamar como `Circulo.descripcion()` sin necesidad de instancia.

La introducción a POO suele ser un tema extenso, pero para nuestro enfoque en funciones, lo importante es:
- Los métodos se definen igual que funciones pero dentro de una clase, y llevan `self` como primer parámetro (en métodos de instancia). 
- Cuando creas un objeto e invocas un método, no pasas self; Python lo hace.
- Puedes pensar en `obj.metodo(arg1, arg2)` como sintaxis azucarada para la función `Clase.metodo(obj, arg1, arg2)`.

También, los métodos pueden retornar valores, aceptar parámetros adicionales aparte de self, lanzar excepciones, etc., igual que funciones normales.

**`self` en analogía**: Piensa en `self` como el pronombre "yo" dentro de la clase. Cuando escribes un método, estás describiendo qué hace "yo" (la instancia) cuando se le pide esa acción. Por ejemplo, en `saludar(self)`, decimos "yo saludo diciendo mi nombre". Cada objeto cuando ejecuta ese método, `self` es él mismo, así que efectivamente dice su nombre.

**Relación con instancias**: Si tienes múltiples instancias, cada llamada a un método opera sobre los datos de esa instancia. En una función normal, las variables locales se crean en cada llamada; en un método, además tienes el contexto del objeto (sus atributos). Por eso métodos son muy útiles: combinan lógica (código) con datos (atributos), que es la esencia de la POO.

**Ejercicios prácticos (POO y métodos)**:
1. *Clase simple:* Crea una clase `CuentaBancaria` con atributo `saldo`. Implementa un método `depositar(self, monto)` que sume al saldo, un método `retirar(self, monto)` que reste al saldo (si hay fondos suficientes, si no que imprima un mensaje de fondos insuficientes) y un método `mostrar_saldo(self)` que imprima o retorne el saldo actual. Luego crea una instancia de `CuentaBancaria`, realiza algunas operaciones y verifica que el saldo sea correcto.
2. *Rectángulo:* Define una clase `Rectangulo` con atributos `base` y `altura`. Añade un método `area(self)` que calcule el área (base*altura) y un método `perimetro(self)` que calcule el perímetro (2*(base+altura)). Crea un rectángulo de 4x3 y comprueba que `area()` devuelve 12 y `perimetro()` 14.
3. *Uso de @classmethod:* Añade a la clase `Rectangulo` un método de clase `cuadrado(cls, lado)` que retorne una instancia de `Rectangulo` donde base y altura sean iguales (usando `lado`). Prueba crear un "cuadrado" de lado 5 usando `Rectangulo.cuadrado(5)` y verifica sus métodos.

---

## Conclusión

En estas notas de clase hemos recorrido un amplio espectro de conceptos relacionados con las funciones en programación utilizando Python como lenguaje de práctica. Comenzamos con la motivación de por qué usar funciones y cómo definirlas y llamarlas, pasando por detalles como parámetros (y su comportamiento interno), valores de retorno y alcance de las variables, para luego sumergirnos en temas más avanzados como la recursividad, las funciones lambda y el manejo adecuado de errores mediante excepciones. También dedicamos atención a las buenas prácticas, porque escribir código funcional no es suficiente: hay que apuntar a código limpio, legible y robusto. Finalmente, dimos un vistazo a cómo las funciones se integran en la programación orientada a objetos a través de métodos de instancia, de clase y estáticos, entendiendo el rol de `self` y cómo Python maneja estos "azúcares sintácticos" por nosotros.

Como estudiante de primer semestre de Ingeniería de Sistemas, es normal sentirse abrumado al principio con tantos detalles. **Recomendación**: práctica constante. Toma cada sección y experimenta escribiendo tus propios ejemplos, modificando los que se mostraron, y resolviendo los ejercicios propuestos. Prueba a escribir pequeños programas en Visual Studio Code, ejecutarlos, depurarlos (VS Code tiene un depurador que puedes usar para hacer seguimiento paso a paso, muy útil para entender recursión o flujo de llamadas). 

No dudes en introducir errores adrede para ver cómo se comportan (por ejemplo, llama a una función antes de definirla para ver el error, o provoca una excepción de tipo para ver el mensaje). Cada error es una oportunidad de aprendizaje para entender mejor la máquina de Python.

Conforme avances, verás que las funciones se vuelven la piedra angular de programas más complejos, y combinarlas con la POO te permitirá estructurar soluciones elegantes y potentes. Estas notas pueden servirte de referencia rápida más adelante; incluso podrías ampliarlas con tus propias observaciones o ejemplos descubiertos.

¡Sigue practicando y disfrutando del viaje en la programación! Cada concepto afianzado es una nueva herramienta en tu cinturón de desarrollador. 🛠️🚀
