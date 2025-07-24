
# Medios de Expresión de Algoritmos, Programas y Lenguajes de Programación

## 1. Medios de expresión de un algoritmo

### 1.1 ¿Qué es un algoritmo?

Un **algoritmo** es un conjunto ordenado y finito de instrucciones o pasos que permite resolver un problema o realizar una tarea de manera precisa y sin ambigüedades. En otras palabras, un algoritmo toma una **entrada** (datos iniciales) y, a través de pasos definidos, produce una **salida** o resultado. Por ejemplo, una receta de cocina puede verse como un algoritmo: comienza con ingredientes (entrada), sigue pasos específicos, y termina con un plato preparado (salida).

Un mismo algoritmo puede expresarse de diferentes formas o **medios de representación**, dependiendo de nuestro propósito y audiencia. Los principales medios para representar algoritmos incluyen:

* **Lenguaje natural (escrito u oral)**: Descripción con palabras comunes (por ejemplo, instrucciones paso a paso en español).
* **Pseudocódigo**: Descripción textual estructurada, parecida a un lenguaje de programación simplificado.
* **Diagramas de flujo**: Representación gráfica mediante símbolos conectados por flechas, mostrando el flujo de pasos.
* **Código en un lenguaje de programación**: Implementación del algoritmo usando la sintaxis de un lenguaje particular para que pueda ser **ejecutado** en una computadora.

Los algoritmos pueden expresarse en cualquiera de estos medios, aunque cada uno tiene sus ventajas y desventajas. A continuación, exploraremos cada forma de expresión con detalles y ejemplos.

### 1.2 Lenguaje natural

Describir un algoritmo en **lenguaje natural** significa explicarlo con palabras comunes, tal como lo haríamos al dar instrucciones a una persona. Este es el medio más intuitivo para comenzar, ya que no requiere conocer notación especial. Por ejemplo, podemos describir en lenguaje natural un algoritmo para determinar si un número entero es par o impar así:

* *Algoritmo (descripción en lenguaje natural)*: "Para saber si un número es par, primero toma el número y **divídelo por 2**. Si el residuo de esa división es 0, entonces el número es par; de lo contrario, es impar."

Este tipo de descripción es fácil de entender porque utiliza palabras cotidianas. Sin embargo, el lenguaje natural tiende a ser **ambiguo y extenso**. Diferentes personas podrían interpretar las mismas instrucciones de formas ligeramente distintas si no se formulan con cuidado. Por ejemplo, la instrucción "divídelo por 2" podría suscitar la pregunta: ¿debo considerar decimales o solo la división exacta? Por ello, aunque el lenguaje común es un buen punto de partida para explicar la idea general de un algoritmo, no siempre es la mejor opción cuando se necesita precisión absoluta.

**Ejemplo (lenguaje natural)**: Supongamos que queremos un algoritmo para encontrar el mayor de dos números. Una descripción en lenguaje natural podría ser: *"Dado dos números, compara ambos. Si el primer número es mayor que el segundo, entonces ese primer número es el mayor. En caso contrario, el segundo número será el mayor. Si son iguales, puedes decir que ambos son iguales."* Esta descripción, aunque comprensible, podría volverse más complicada si extendemos el problema a una lista de muchos números o si incluimos muchos detalles excepcionales.

### 1.3 Pseudocódigo

El **pseudocódigo** es una forma intermedia de expresar algoritmos, combinando la facilidad de las frases en lenguaje común con la estructura lógica de un lenguaje de programación. En pseudocódigo se usan palabras y símbolos parecidos a los de la programación (por ejemplo, *Para*, *Si..., Entonces..., Fin Si*, *mientras*, etc.), pero sin atarse a la sintaxis estricta de ningún lenguaje específico. Esto permite describir algoritmos de forma concisa y clara, evitando muchas de las ambigüedades del lenguaje natural y sin el nivel de detalle que exige escribir código real.

Un punto importante es que **no existe un estándar universal de pseudocódigo**; su escritura puede variar ligeramente según el autor o el contexto. Aun así, la idea es siempre la misma: representar la lógica del algoritmo paso a paso de manera estructurada. El pseudocódigo suele ser más **compacto** que un diagrama de flujo equivalente, especialmente para algoritmos complejos, y es independiente de cualquier lenguaje de programación en particular.

**Ejemplo (pseudocódigo)**: Retomemos el ejemplo de encontrar el número mayor en una lista de números (para ilustrar un caso con más pasos). En lenguaje natural dijimos cómo hacerlo; en pseudocódigo podemos expresarlo de forma más estructurada:

```
Algoritmo EncontrarMaximo
    // Supongamos que tenemos una lista C de n números:
    definir C = [c0, c1, ..., c_{n-1}] 
    max = c0                    // inicializar el máximo con el primer elemento
    Para i desde 1 hasta n-1 hacer:
        Si C[i] > max Entonces:
            max = C[i]          // actualizar el máximo
        Fin Si
    Fin Para
    devolver max                // el valor almacenado en max es el mayor
Fin Algoritmo
```

En este pseudocódigo, usamos una notación intuitiva: `←` indica **asignación** (dar un valor a una variable), la estructura `Para ... hacer` indica un bucle, y la construcción `Si ... Entonces ... Fin Si` representa una decisión condicional. Observa que no tenemos que preocuparnos por detalles como la sintaxis exacta de un lenguaje real (comas, puntos y comas, tipos de datos, etc.), sino solo enfocarnos en la **lógica**. Como resultado, el pseudocódigo es fácil de leer y escribir para cualquier persona familiarizada con conceptos básicos de programación, incluso si no conoce un lenguaje específico.

*Ventajas:* El pseudocódigo evita la ambigüedad del lenguaje natural al usar estructuras lógicas claras. Al mismo tiempo, al no ser código real, es más sencillo de elaborar y modificar durante la etapa de diseño de un algoritmo (no es necesario que compile ni se ajuste a reglas sintácticas rígidas). También ocupa menos espacio que dibujar un diagrama de flujo equivalente para el mismo algoritmo.

*Desventajas:* Dado que no es un estándar formal, dos personas pueden escribir pseudocódigos algo diferentes para el mismo problema. Además, el pseudocódigo **no se puede ejecutar directamente** en la computadora (debe primero traducirse a un lenguaje de programación real). Aun así, es una herramienta excelente para planificar la solución antes de programarla.

### 1.4 Diagramas de flujo

Un **diagrama de flujo** (o flujograma) es una representación **gráfica** de un algoritmo. En un diagrama de flujo, cada paso del algoritmo se dibuja dentro de una figura (generalmente cajas de distintos tipos), y estas figuras se conectan con flechas que indican el **orden de ejecución** de los pasos. Por convención, se utilizan diferentes símbolos normalizados para distintos tipos de operaciones: por ejemplo, óvalos para inicio/fin, paralelogramos para entrada/salida de datos, rectángulos para procesos (cálculos o acciones), rombos para decisiones (preguntas de sí/no), etc. Existe un estándar ISO que regula estos símbolos para asegurar uniformidad.

Los diagramas de flujo son muy útiles para **visualizar** la lógica de un algoritmo. Al ver un proceso dibujado, es fácil seguir el camino de la ejecución con la vista e identificar dónde ocurren bifurcaciones (decisiones) o bucles. Por esta razón, suelen emplearse como introducción al pensamiento algorítmico y también para comunicar procesos a personas no técnicas de forma comprensible.

&#x20;Un ejemplo típico se muestra en la imagen: un diagrama de flujo sencillo con los pasos a seguir si una lámpara no funciona (una situación de la vida cotidiana). Cada figura representa una pregunta o acción: se comienza en el óvalo de "Inicio", luego se verifica la condición "¿La lámpara está enchufada?" (rombo de decisión). Dependiendo de la respuesta (Sí/No), el flujo sigue por una u otra flecha hacia el siguiente paso (por ejemplo, enchufar la lámpara, o cambiar la bombilla si ya estaba enchufada). Finalmente, se llega a una solución o a un punto final del proceso. Este ejemplo ilustra cómo un algoritmo no tiene que ver solo con matemáticas o computación, sino que puede describir cualquier procedimiento lógico paso a paso.

A pesar de su claridad, los diagramas de flujo pueden volverse **engorrosos** para algoritmos muy extensos o complejos, ya que el dibujo puede ocupar mucho espacio y volverse difícil de seguir. Por eso, en la práctica se usan más para problemas pequeños, para la etapa de planificación inicial, o para documentar procesos de forma general. Cuando se trabaja en algoritmos grandes, suele preferirse pseudocódigo u otras herramientas, ya que un diagrama complejo podría ser menos práctico de manejar.

En resumen, el diagrama de flujo ofrece una perspectiva visual fácil de entender de un algoritmo, ideal para asegurarse de que la secuencia de pasos es correcta y para comunicar la idea a otros. Sin embargo, no es directamente **editable por la máquina** (no podemos "ejecutar" un diagrama de flujo en la computadora), por lo que eventualmente tendremos que traducir ese flujo en código.

### 1.5 Implementación en un lenguaje de programación (código)

La forma más concreta de expresar un algoritmo es escribiéndolo en un **lenguaje de programación**, es decir, convertirlo en un **programa** de computadora. A diferencia del pseudocódigo, aquí debemos respetar estrictamente la sintaxis y reglas del lenguaje elegido, porque el objetivo es que el algoritmo pueda ser **ejecutado automáticamente por la computadora**.

Cada lenguaje de programación (Java, C++, Python, etc.) tiene su propia sintaxis, pero la mayoría comparte conceptos básicos (variables, operaciones, estructuras de control como bucles y condicionales). Al implementar un algoritmo en código, obtenemos **paso a paso exactos** que una máquina puede seguir. El código es completamente no ambiguo: cada instrucción tiene un significado preciso definido por el lenguaje.

Sigamos con el ejemplo del algoritmo para encontrar el máximo de una lista de números, implementándolo ahora en Python (un lenguaje de programación popular para principiantes):

```python
# Lista de ejemplo
C = [10, 7, 22, 15, 3]

# Implementación para encontrar el máximo
maximo = C[0]                   # tomar el primer elemento como máximo inicial
for i in range(1, len(C)):      # recorrer desde el segundo elemento hasta el final
    if C[i] > maximo:
        maximo = C[i]           # actualizar el valor máximo
print("El valor máximo es:", maximo)
```

Si ejecutamos este código con la lista de ejemplo `[10, 7, 22, 15, 3]`, mostrará `El valor máximo es: 22` por pantalla, pues `22` es el número mayor de esa lista. Obsérvese cómo la estructura del código Python refleja el pseudocódigo que escribimos antes: un bucle `for` que recorre la lista, una condición `if` que compara y actualiza el máximo, etc. La principal diferencia es que en Python debemos utilizar la sintaxis correcta (por ejemplo, `for i in range(1, len(C)):` en lugar de "Para i desde 1 hasta n-1") y respetar la indentación que define los bloques de código.

**Ventajas del código (implementación real):** es **ejecutable**, lo que significa que podemos probar el algoritmo con datos reales y obtener resultados automáticamente. Además, una vez en código, el algoritmo puede ser utilizado dentro de un sistema mayor, reutilizado y compartido fácilmente. El código en un lenguaje de programación es la forma que entiende la computadora, aunque primero suele requerir una traducción a código máquina (veremos ese proceso más adelante en la sección de programas).

**Desafíos:** escribir en un lenguaje de programación requiere conocer sus reglas y muchas veces es menos intuitivo para alguien no entrenado, comparado con leer pseudocódigo o diagramas. Un error pequeño de sintaxis (por ejemplo, olvidar dos puntos `:` en Python o una llave `{}` en C++) puede impedir que el programa funcione. Por ello, en la fase inicial de diseño de algoritmos es común empezar en pseudocódigo o lenguaje natural, y luego traducir a código cuando ya se tiene claro el procedimiento.

### 1.6 Comparación de formas de expresar algoritmos

En resumen, los distintos medios de expresión de algoritmos se distinguen por su grado de formalidad y cercanía al lenguaje humano o a la máquina:

* **Lenguaje natural:** Muy fácil de entender por personas, pero propenso a ambigüedades y a malinterpretaciones. Útil para describir problemas en términos generales o comunicar la idea básica sin tecnicismos.
* **Pseudocódigo:** Equilibrio entre legibilidad y precisión. Evita muchas ambigüedades del lenguaje natural usando una estructura similar a la programación, pero sin detalles técnicos. No es ejecutable directamente, pero sí fácil de traducir luego a cualquier lenguaje de programación.
* **Diagrama de flujo:** Representación visual que clarifica la secuencia y la estructura del algoritmo (decisiones, bucles). Es excelente para comprender y discutir la lógica, especialmente con principiantes o equipos, aunque puede ser impráctico para algoritmos muy grandes.
* **Código en lenguaje de programación:** Forma 100% precisa y ejecutable del algoritmo. Requiere conocimientos del lenguaje (sintaxis, semántica) y atención al detalle. Es la versión final que correrá en la computadora. A diferencia de las otras representaciones, el código está **atado a un lenguaje específico** (un algoritmo implementado en Python tendrá que reescribirse en Java si quisiéramos usarlo en Java, por ejemplo).

En la práctica, muchas veces se combinan estos medios durante el desarrollo. Por ejemplo, un ingeniero puede **describir el problema** en lenguaje natural, diseñar la **solución en pseudocódigo o diagrama de flujo**, discutir y refinar la lógica, y finalmente **codificar** el algoritmo en el lenguaje de programación de su preferencia. Lo importante es entender que, aunque el algoritmo subyacente (la secuencia lógica) es el mismo, la forma de expresarlo cambia quién puede interpretarlo directamente: personas, diagramas para comunicar ideas, o máquinas.

## 2. Programas

Ahora que sabemos cómo expresar algoritmos, demos el siguiente paso: ¿qué es exactamente un **programa** de computadora? En términos simples, un programa informático es la **materialización** de uno o varios algoritmos en un código ejecutable por la máquina. Es decir, un programa es un **conjunto de instrucciones** que, al ser ejecutadas, realizan una o varias tareas en una computadora. Sin programas, la computadora no haría nada útil por sí sola, ya que el hardware necesita instrucciones lógicas para saber qué acciones realizar.

Cuando escribimos un algoritmo en un lenguaje de programación y lo guardamos, obtenemos un **programa fuente** (el código escrito por el programador). Este código fuente suele pasar por un proceso para convertirse en algo que la computadora pueda ejecutar directamente. Hay dos mecanismos principales para **ejecutar un programa** escrito en un lenguaje de alto nivel:

1. **Interpretación:** Un programa llamado *intérprete* lee el código fuente y lo va **ejecutando línea por línea** en tiempo real. Es decir, traduce e interpreta las instrucciones sobre la marcha conforme el programa corre. Lenguajes como Python utilizan este enfoque; el intérprete de Python toma las instrucciones (por ejemplo, `print("Hola")`) y realiza la acción inmediata (mostrar el texto en pantalla). La ventaja es que no se necesita un paso de compilación previo y facilita la prueba rápida de fragmentos de código. La desventaja es que la ejecución puede ser un poco más lenta, ya que la traducción ocurre sobre la marcha cada vez que se ejecuta el programa.

2. **Compilación:** Un programa llamado *compilador* **traduce el código fuente completo** a otro lenguaje más bajo nivel (por lo general, el código máquina específico de la computadora o un código intermedio) antes de ejecutar nada. Este proceso genera un archivo ejecutable (por ejemplo, un `.exe` en Windows) que ya contiene las instrucciones en el único lenguaje que entiende la máquina: ceros y unos (código binario). Lenguajes como C, C++ o Java (en este último caso compila a bytecode, que luego es interpretado por una máquina virtual) funcionan así. La ventaja es que el programa compilado suele correr más rápido nativamente y no requiere del código fuente para ejecutarse (solo se distribuye el ejecutable). La desventaja es que cada vez que modificamos el código fuente, tenemos que compilar de nuevo, y el proceso de compilación puede detectar errores de sintaxis antes de correr el programa, lo que aunque beneficioso, añade un paso adicional en el ciclo de desarrollo.

En ambos casos, el fin último es que las instrucciones escritas por el programador (en una forma entendible por humanos) se conviertan a instrucciones máquina entendibles por la computadora. En sistemas Unix/Linux a los programas ejecutables a veces se les llama **“binarios”**, precisamente porque están en código binario listo para la CPU.

**Definición formal:** Un **programa** puede referirse tanto al código fuente que el programador escribe, como al archivo ejecutable final resultante de compilarlo. En muchos casos, cuando decimos "ejecutar el programa", nos referimos a correr el ejecutable. Cuando decimos "leer el programa", podemos referirnos a leer el código fuente que lo genera. En cualquier caso, ambos (fuente y ejecutable) son manifestaciones del mismo conjunto de pasos lógicos.

Además, los programas forman la base del **software**. Todo el conjunto de programas de una computadora se denomina software, en contraste con el hardware (las partes físicas de la máquina). Hay programas de **sistema** (por ejemplo, sistemas operativos, que gestionan los recursos de la computadora) y programas de **aplicación** (por ejemplo, procesadores de texto, navegadores web, calculadoras, juegos, etc., que realizan tareas para el usuario). Independientemente de su tipo, todos son esencialmente colecciones de algoritmos implementados.

**Ejemplo ilustrativo:** Consideremos un programa sencillo escrito en BASIC (un lenguaje de programación antiguo pero sencillo). En la siguiente imagen, se muestra una captura de pantalla de un microordenador Commodore corriendo un programa en BASIC bajo un emulador:

&#x20;*Captura de pantalla de un computador Commodore PET-32 mostrando un programa en el lenguaje BASIC.* En este programa (apreciable en la pantalla verde con texto), cada línea numerada contiene una instrucción. Por ejemplo, una línea podría ser `10 PRINT "HELLO"` (que imprimiría “HELLO” en pantalla). Este es un ejemplo de **programa** completo: un conjunto de líneas de código que la computadora interpreta y ejecuta secuencialmente para realizar alguna tarea (en BASIC, las líneas se numeraban para indicar el orden de ejecución). Aunque BASIC es un lenguaje muy diferente de Python o C, la idea subyacente es la misma: tenemos un algoritmo (en este caso, quizá mostrar texto o pedir datos) plasmado en instrucciones precisas.

En resumen, **programar** es el proceso de **escribir un algoritmo en forma de programa**, probándolo y depurándolo hasta que funcione correctamente para todos los casos previstos. Un programa correctamente escrito lleva a cabo las acciones previstas por el algoritmo original de manera fiel. Para los ingenieros de primer semestre, es crucial comprender esta relación: *un programa es a un algoritmo lo que una receta concreta es a la idea general de un platillo*. Primero se idea la solución (algoritmo), luego se codifica esa solución en una "receta" precisa que la computadora pueda "cocinar" (programa).

## 3. Lenguajes de programación

Un **lenguaje de programación** es un **lenguaje formal** diseñado para describir algoritmos y permitir que seres humanos instruyan a una computadora a realizar tareas específicas. A diferencia de un lenguaje natural (como el español o el inglés), los lenguajes de programación tienen reglas **sintácticas** y **semánticas** estrictamente definidas, de modo que cada instrucción escrita tenga un significado único y no ambiguo para la máquina. Usando un lenguaje de programación, un programador puede escribir una serie de pasos (instrucciones) que la computadora seguirá para manipular datos, hacer cálculos, tomar decisiones lógicas y comunicar resultados.

Cuando un programador escribe código en un lenguaje de programación, lo que en realidad está haciendo es expresar algoritmos de forma **precisa y estructurada**. Todo el conjunto de instrucciones escritas en ese lenguaje constituye un programa (como vimos en la sección anterior). Por ejemplo, Python, C++, Java, JavaScript, C#, Ruby, etc., son todos lenguajes de programación, cada uno con su sintaxis y usos particulares, pero todos sirven al mismo propósito fundamental: **decirle al computador qué hacer**.

**Características de los lenguajes de programación:**

* Son *formales y artificiales*: esto significa que sus reglas no evolucionaron naturalmente como en los idiomas humanos, sino que fueron **diseñadas**. Cada símbolo, palabra reservada (palabras especiales del lenguaje como `if`, `while`, `print`, etc.) y estructura tiene un propósito definido. Por ejemplo, en Python la palabra clave `if` indica el inicio de una condición, y siempre debe ir seguida de una condición lógica y dos puntos. Estas reglas evitan ambigüedad (la computadora no "adivina" intenciones; todo debe estar claro en el código).

* Tienen **vocabulario (alfabeto) y gramática**: igual que un idioma, un lenguaje de programación define qué símbolos se pueden usar (letras, dígitos, signos) y cómo pueden combinarse correctamente (sintaxis). Si el código viola la sintaxis (gramática), un compilador o intérprete dará errores y no ejecutará el programa hasta que se corrija. Además, existe la **semántica**, que es el significado de las estructuras; por ejemplo, la sintaxis podría permitir cierta instrucción, pero si semánticamente no tiene sentido (como tratar de sumar un número con un texto), el programa tampoco funcionará correctamente.

* **Imperativos vs Declarativos:** Muchos lenguajes son de tipo *imperativo*, es decir, el programador indica paso a paso lo que se debe hacer (por ejemplo, "primero calcula A, luego si A > 0 haz B, sino haz C, luego repite esto 5 veces..."). Otros lenguajes son *declarativos*, donde el programador más bien declara qué desea obtener o las reglas del resultado, y el *cómo* se logra queda en manos del sistema. Un ejemplo de declarativo es SQL (para bases de datos) donde uno declara "selecciona todos los registros donde X sea mayor que Y" y no indica exactamente cómo buscar, o lenguajes funcionales donde se declaran relaciones matemáticas. En general, los lenguajes que veremos al inicio (Python, C, Java, etc.) son imperativos (también llamados *procedimentales* u orientados a objetos), donde se proporciona un conjunto de órdenes secuenciales.

* **Nivel de abstracción:** Existen **lenguajes de bajo nivel** y **de alto nivel**. Los de *bajo nivel* (como el lenguaje ensamblador) están más cerca del código máquina; son instrucciones muy simples y detalladas que la CPU entiende casi directamente (por ejemplo, mover datos de un registro a otro, sumar registros, etc.). Son rápidos y eficientes, pero difíciles de leer para humanos. Los de *alto nivel* (como Python, Java, etc.) están más cerca del lenguaje humano; introducen abstracciones para facilitar la programación (por ejemplo, operaciones aritméticas con notación usual, bucles `for` en vez de gestionar saltos de memoria, manejo automático de la memoria, etc.). Son más fáciles de usar y entender, aunque la computadora necesita más trabajo para traducirlos a su lenguaje máquina (justamente mediante intérpretes o compiladores). Hoy en día la mayoría de la programación aplicada se hace en lenguajes de alto nivel, porque aumentan la **productividad** del desarrollador y el código tiende a ser más **portable** (puede ejecutarse en diferentes sistemas con pocos o ningún cambio).

* **Paradigmas de programación:** Un paradigma es un estilo o enfoque de programación. Los principales paradigmas incluyen la programación **procedimental/estructurada**, la **orientada a objetos**, la **funcional**, la **lógica**, entre otros. Python, por ejemplo, soporta varios paradigmas (puedes programar de forma estructurada o orientada a objetos, incluso usar estilos funcionales). Este tema es más avanzado, pero es bueno saber que existen distintas formas de pensar la solución de un problema en código, y ciertos lenguajes favorecen un paradigma u otro. En el primer semestre típicamente nos enfocamos en la programación estructurada (secuencias de instrucciones, condicionales, bucles y subdividir problemas en funciones).

Es importante **no confundir** los lenguajes de programación con otros tipos de lenguajes informáticos. Por ejemplo, HTML es un lenguaje de marcado para estructurar documentos web, no es un lenguaje de programación propiamente (no describe algoritmos, sino la apariencia/estructura de la información). Similarmente, JSON o XML son lenguajes de formato de datos, tampoco son "para programar". Un lenguaje de programación siempre nos permite especificar **algoritmos** y controlar la *lógica* (ramificaciones, iteraciones, cálculos). Si un "lenguaje" no permite estas cosas, es más bien un esquema de datos o de configuración.

**Ejemplo y primer programa en Python:** Tradicionalmente, el primer programa que se escribe al aprender un lenguaje es el famoso **"Hola Mundo"**, que simplemente muestra en pantalla esa frase. Veamos cómo es en Python:

```python
print("¡Hola Mundo!")
```

Así de sencillo: usamos la función incorporada `print()` para imprimir un texto en la salida. Al ejecutar este programa, la computadora mostrará en pantalla la frase ¡Hola Mundo!. Aunque es un ejemplo trivial, nos permite verificar que tenemos un entorno funcionando y entender la estructura básica (en Python, una sola línea puede ser un programa completo). En otros lenguajes, el "Hola Mundo" puede requerir más código, por ejemplo en C:

```c
#include <stdio.h>
int main() {
    printf("Hola Mundo!\n");
    return 0;
}
```

Aquí vemos la diferencia de sintaxis: en C debemos incluir librerías, definir una función `main` y usar `printf` con un formato específico. Cada lenguaje tiene su *forma de decir las cosas*, pero la intención final es la misma.

**Otro ejemplo (interacción con el usuario):** A continuación, un pequeño programa en Python que combina varios elementos: pide un dato al usuario, realiza una operación y muestra el resultado. Este ejemplo ilustra cómo un lenguaje de programación nos permite implementar un algoritmo completo con entrada, proceso y salida:

```python
# Programa que convierte una temperatura de Celsius a Fahrenheit
c = float(input("Ingrese temperatura en grados Celsius: "))  # leer entrada del usuario
f = (c * 9/5) + 32  # proceso: fórmula de conversión
print("Equivale a", f, "grados Fahrenheit.")  # salida
```

Si ejecutamos este programa, veremos algo como:

```
Ingrese temperatura en grados Celsius: 100
Equivale a 212.0 grados Fahrenheit.
```

Aquí usamos `input()` para leer del teclado (siendo `c` una **variable**) y luego aplicamos la fórmula matemática. Este algoritmo de conversión podría haberse descrito en lenguaje natural ("multiplica por 9/5 y suma 32") o en pseudocódigo, pero en código Python se vuelve inmediatamente algo que la computadora puede usar para hacer cálculos reales y producir una respuesta.

**Lenguajes de programación y algoritmos:** Para concluir, destacar que el estudio de algoritmos y el estudio de lenguajes de programación van de la mano. Un buen programador primero piensa en el **algoritmo** (el *qué hacer*), y luego decide el **lenguaje** (el *cómo hacerlo entendible para la máquina*). Aprender a programar implica tanto aprender la lógica algorítmica como aprender la sintaxis de uno o más lenguajes. En primer semestre, Python es a menudo elegido por su sintaxis simple y legibilidad, lo que nos permite centrarnos en entender la lógica de los algoritmos sin perdernos en demasiados detalles de sintaxis.

## 4. Ejercicios prácticos en Python

A continuación se proponen algunos ejercicios básicos para poner en práctica estos conceptos. Están pensados para estudiantes **principiantes** (sin experiencia previa), utilizando el lenguaje Python por su simplicidad. Cada ejercicio requiere diseñar un algoritmo (puedes comenzar escribiéndolo en español o pseudocódigo) y luego implementar ese algoritmo como un programa en Python. ¡Intenta resolverlos y probar tus programas!:

1. **Mayor de dos números:** Escribe un programa que pida al usuario ingresar **dos números** y que muestre en pantalla cuál de los dos es mayor. (Pista: necesitarás usar una estructura condicional `if` para comparar los números, y la función `input()` para leer los valores ingresados por el usuario).

2. **Número par o impar:** Escribe un programa que lea un número entero desde el teclado e indique si el número es **par** o **impar**. (Recuerda: un número es par si el resto de dividirlo por 2 es 0. En Python el operador módulo `%` puede servirte para obtener el residuo de una división).

3. **Suma de los primeros N números:** Pídele al usuario un número entero positivo `N` y luego calcula la **suma de todos los números del 1 al N**. Por ejemplo, si `N = 5`, el programa debería calcular `1+2+3+4+5` y dar como resultado 15. (Este ejercicio se puede hacer de dos maneras: usando una fórmula matemática directa o usando un bucle `for` para sumar repetitivamente. Intenta primero con el bucle para practicar las estructuras de repetición).

4. **Conversión de temperatura:** Implementa el ejemplo visto de conversión de grados Celsius a Fahrenheit. Es decir, lee una temperatura en grados Celsius y muéstrala convertida a Fahrenheit usando la fórmula `F = C * 9/5 + 32`. Luego extiende el programa para que también convierta de Fahrenheit a Celsius (solicitando al usuario qué conversión desea hacer).

5. **Encontrar el máximo en una lista:** Pide al usuario que ingrese una lista de números (puedes solicitar que los ingrese separados por espacio, luego usar `split()` para obtenerlos, por ejemplo) y encuentra el **número mayor** de la lista. Este ejercicio pone en práctica la idea del algoritmo "encontrar máximo" que discutimos en la teoría. Intenta primero diseñar el algoritmo (posiblemente similar al pseudocódigo dado en la sección 1.3) y luego implementarlo en Python. *(Extra:* Python tiene la función incorporada `max()` que hace esto directamente, ¡pero aquí queremos que practiques el algoritmo, así que no la uses y hazlo manualmente).\*

**Consejos para resolver los ejercicios:** Comienza determinando el algoritmo en papel o en palabras. Identifica qué datos de entrada necesitas (usas `input()` para obtenerlos), qué proceso realizarás (cálculos, comparaciones, bucles, etc.), y qué salida esperas obtener (`print()` para mostrar resultados). Si te atascas, vuelve a expresar la solución en lenguaje natural o pseudocódigo, asegúrate de comprender la lógica, y luego tradúcela a código poco a poco. Prueba tu programa con distintos valores para verificar que funciona en todos los casos esperados (por ejemplo, prueba números positivos, negativos, cero, etc., en los ejercicios que aplique).

**Resuelve estos ejercicios y revisa los resultados**: la mejor forma de aprender a programar es **programando**. Equivócate, depura, y vuelve a intentar; con la práctica irás entendiendo mejor tanto los algoritmos como la sintaxis de Python. ¡Mucho ánimo en tu inicio del camino en la programación y la ingeniería!

