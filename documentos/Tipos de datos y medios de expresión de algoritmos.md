---

# 📌 Introducción a la Programación y Algoritmos

## 🤔 ¿Qué es la programación?

La **programación** es el proceso de diseñar y construir soluciones a problemas mediante un conjunto de instrucciones lógicas y secuenciales. Permite a las computadoras ejecutar tareas de manera eficiente y automática.

## 🔄 ¿Qué es un algoritmo?

Un **algoritmo** es un conjunto de pasos ordenados y definidos que describen la solución a un problema. Son independientes del lenguaje de programación y pueden representarse de diferentes maneras.

### 📌 Características de un algoritmo:

✅ Preciso: Define cada paso con claridad.  
✅ Definido: Si se ejecuta más de una vez con los mismos datos, el resultado siempre es el mismo.  
✅ Finito: Debe tener un número limitado de pasos.

Ejemplo de algoritmo para sumar dos números:

1. Leer dos números.  
2. Sumar los números.  
3. Mostrar el resultado.  

Representación en pseudocódigo:
```
Inicio
    Leer num1, num2
    resultado = num1 + num2
    Escribir resultado
Fin
```

---

# 📌 Medios de Expresión de un Algoritmo, Programas y Lenguajes de Programación

Los algoritmos pueden expresarse de diferentes formas:

## 1️⃣ **Lenguaje Natural**

Expresión en palabras comunes. Ejemplo:
> "Para sumar dos números, pide los valores al usuario, realiza la suma y muestra el resultado."

## 2️⃣ **Diagrama de Flujo**

Representación gráfica con símbolos para cada tipo de acción (inicio, proceso, decisión, fin).  
Ejemplo de diagrama de flujo para la suma de dos números: 🖼️

## 3️⃣ **Pseudocódigo**

Descripción en un lenguaje intermedio entre natural y programación.

Ejemplo de pseudocódigo para calcular el área de un triangulo:
```
Inicio
    real area
    Leer altrua,base
    area = base * altura / 2
    mostrar area
Fin
```

Otro ejemplo de pseudocódigo para calcular la suma de dos numeros:
```
Inicio
    real suma
    Leer numero1,numero2
    suma = numero1 + numero2
    mostrar suma
Fin
```

## 4️⃣ **Lenguaje de Programación**

Es la implementación del algoritmo en un lenguaje específico. Ejemplo en Python:
```python
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
print("La suma es:", num1 + num2)
```

---

# 📌 Tipos de Datos y Tipos de Identificadores

## 📊 **Tipos de Datos**

Los lenguajes de programación manejan diferentes tipos de datos, que pueden clasificarse en **primitivos** y **no primitivos**.

### 🔹 **Tipos de Datos Primitivos**

Son los tipos básicos que los lenguajes de programación proporcionan por defecto y que almacenan un solo valor.

| Tipo                | Descripción                    |
| ------------------- | ------------------------------ |
| Enteros (`int`)     | Números sin decimales          |
| Flotantes (`float`) | Números con decimales          |
| Cadenas (`string`)  | Texto o caracteres             |
| Booleanos (`bool`)  | Valores de verdad (True/False) |

Ejemplo de uso:
```python
edad = 25  # Entero
pi = 3.1416  # Flotante
nombre = "Ana"  # Cadena
es_estudiante = True  # Booleano
```

### 🔹 **Tipos de Datos No Primitivos**

Son estructuras más complejas que pueden contener múltiples valores y permiten organizar mejor la información.

| Tipo                  | Descripción                               |
| --------------------- | ----------------------------------------- |
| Listas (`list`)       | Conjunto ordenado de elementos            |
| Tuplas (`tuple`)      | Conjunto ordenado de elementos inmutables |
| Diccionarios (`dict`) | Estructuras de clave-valor                |

Ejemplo de uso:
```python
notas = [90, 85, 88]  # Lista
colores = ("rojo", "verde", "azul")  # Tupla
datos = {"nombre": "Carlos", "edad": 22}  # Diccionario
```

---

## 🔠 **Tipos de Identificadores**

Un **identificador** es el nombre que se le da a variables, funciones, clases, etc.

### ✅ Reglas para identificadores:

1. Debe comenzar con una letra o guion bajo (`_`).  
2. No puede contener espacios ni caracteres especiales (`+`, `-`, `@`, etc.).  
3. Distingue entre mayúsculas y minúsculas (`nombre` ≠ `Nombre`).  
4. No debe ser una palabra reservada (como `if`, `for`, `def`).  

### 🔹 **Estilos de escritura para identificadores**

Existen diferentes convenciones para nombrar identificadores en programación:

- **Camel Case:** La primera palabra comienza en minúscula, y las siguientes inician con mayúscula.
  ```python
  nombreUsuario = "Carlos"
  ```
- **Pascal Case:** Similar a Camel Case, pero la primera letra también es mayúscula.
  ```python
  NombreUsuario = "Carlos"
  ```
- **Snake Case:** Todas las palabras en minúsculas separadas por guiones bajos (`_`).
  ```python
  nombre_usuario = "Carlos"
  ```

Python recomienda el uso de **Snake Case** para variables y funciones, y **Pascal Case** para nombres de clases.

### ❌ **Ejemplos de identificadores incorrectos**

Estos son ejemplos de identificadores que no cumplen con las reglas y convenciones de nombrado:
```python
2variable = "Inválido"  # No puede comenzar con un número
mi variable = 10  # No puede contener espacios
@nombre = "Error"  # No puede contener caracteres especiales
for = 5  # No puede ser una palabra reservada
```
---
# 📌 Estructuras de Programación Secuencial

Las **estructuras de programación secuencial** son aquellas donde las instrucciones se ejecutan una tras otra en el mismo orden en el que aparecen en el código. No hay bifurcaciones ni repeticiones, solo un flujo continuo de ejecución.

### ✅ Características:
- Se ejecutan **línea por línea** de arriba hacia abajo.
- No hay condiciones (`if`) ni ciclos (`while`, `for`).
- Son la base de cualquier programa antes de introducir estructuras de control.

### 📌 Ejemplo en pseudocódigo:
```
Inicio
    Leer nombre
    Escribir "Hola, ", nombre
    Leer edad
    Escribir "Tienes ", edad, " años"
Fin
```

### 📌 Ejemplo en Python:
```python
nombre = input("Ingrese su nombre: ")
print("Hola,", nombre)

edad = int(input("Ingrese su edad: "))
print("Tienes", edad, "años")
```

✅ En este caso, las instrucciones se ejecutan en orden, sin saltos ni repeticiones.

---
