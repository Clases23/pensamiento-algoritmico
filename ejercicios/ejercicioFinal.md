
## Cuestionario de Pseudocódigo

### Pregunta 1  
**¿Cuál es el valor de la variable `resultado` al finalizar la ejecución del siguiente pseudocódigo?**

```plaintext
Algoritmo CalculoNuevo
  Variables:
    Entero: A, B, C, resultado
Inicio
  A = 5
  B = 9
  C = 4
  resultado = (B - A) * C div 3 + A
  resultado = resultado * (A - C div 2)
  Mostrar resultado
Fin
````

* A. 30
* B. 29
* C. 31
* D. 32

---

### Pregunta 2

**¿Cuál será el valor de `k` después de la tercera iteración del siguiente ciclo `mientras`?**

```plaintext
Algoritmo AjusteK
  Variables:
    Entero: k, contador
Inicio
  k = 18
  contador = 0
  mientras k > 5 hacer
    si k mod 5 == 0 entonces
      k = k - 3
    sino
      k = k - 2
    fin si
    contador = contador + 1
    si contador == 3 entonces
      salir
    fin si
  fin mientras
  Mostrar k
Fin
```

* A. 12
* B. 15
* C. 10
* D. 9

---

### Pregunta 3

**¿Cuál será el contenido del vector `nums` después de ejecutar el siguiente pseudocódigo?**

```plaintext
Algoritmo GenerarVector
  Variables:
    Entero: i
    Vector nums(5)
Inicio
  para i = 1 hasta 5 hacer
    nums(i) = i * i + 2
  fin para
  Mostrar nums
Fin
```

* A. 3, 6, 11, 18, 27
* B. 1, 4, 9, 16, 25
* C. 2, 5, 10, 17, 26
* D. 4, 8, 15, 24, 35

---

### Pregunta 4

**¿Cuál es el nuevo valor de `Y(5)` después de ejecutar el siguiente pseudocódigo?**

```plaintext
Algoritmo ActualizarY
  Variables:
    Vector Y(6)
    Entero: suma
Inicio
  Y = [2, 5, 8, 11, 14, 17]
  suma = Y(2) + Y(5)
  Y(3) = suma - Y(1)
  Y(6) = Y(4) * 2
  Y(5) = Y(5) + Y(3)
  Mostrar Y(5)
Fin
```

* A. 31
* B. 33
* C. 29
* D. 30

---

### Pregunta 5

**¿Qué valor imprime el siguiente fragmento de pseudocódigo?**

```plaintext
Algoritmo SumarImpares
  Variables:
    Entero: n, x, suma, i
Inicio
  n = 5
  x = 1
  suma = 0
  i = 1
  mientras i <= n hacer
    si x mod 2 == 0 entonces
      suma = suma + x
      i = i + 1
    fin si
    x = x + 1
  fin mientras
  Mostrar suma
Fin
```

* A. 25
* B. 20
* C. 30
* D. 15

---

### Pregunta 6

**¿Con qué valores queda el vector `W` al final del siguiente pseudocódigo?**

```plaintext
Algoritmo GenerarW
  Variables:
    Entero: i
    Vector W(7)
Inicio
  W(1) = 1
  W(2) = 2
  para i = 3 hasta 7 hacer
    si i mod 3 == 0 entonces
      W(i) = W(i-1) + W(i-2)
    sino
      W(i) = W(i-1) + 1
    fin si
  fin para
  Mostrar W
Fin
```

* A. 1, 2, 3, 4, 5, 9, 10
* B. 1, 2, 3, 4, 5, 6, 7
* C. 1, 2, 3, 3, 4, 7, 8
* D. 1, 2, 2, 3, 4, 6, 7

---

### Pregunta 7

**De las siguientes afirmaciones, ¿cuál NO es un principio de la programación modular?**

* A. Permite dividir el problema en partes manejables.
* B. Fomenta la reutilización de código mediante módulos.
* C. Obliga a que todos los módulos compartan el mismo estado global.
* D. Mejora la legibilidad al separar responsabilidades.

---

### Pregunta 8

**¿Qué característica describe mejor una variable local?**

* A. Se define y utiliza únicamente dentro de la función donde está declarada.
* B. Permanece en memoria durante toda la ejecución del programa.
* C. Puede ser accedida directamente desde cualquier otro módulo.
* D. Conservar su valor entre diferentes llamadas a la función.


