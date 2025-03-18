
---

# **🔄 Ciclos Anidados en Programación**  

## **📌 ¿Qué son los ciclos anidados?**  

Un **ciclo anidado** es una estructura de control donde un **bucle se encuentra dentro de otro bucle**. Esto permite ejecutar un conjunto de instrucciones **múltiples veces dentro de cada iteración del ciclo externo**.  

Se pueden anidar ciclos **FOR dentro de FOR**, **WHILE dentro de WHILE**, o combinar **FOR con WHILE**.  

---

## **📌 Sintaxis de Ciclos Anidados**  

### **🔹 FOR dentro de FOR**
```python
for i in range(3):  # Ciclo externo
    for j in range(2):  # Ciclo interno
        print(f"Iteración externa {i}, interna {j}")
```

### **🔹 WHILE dentro de WHILE**
```python
i = 0
while i < 3:  # Ciclo externo
    j = 0
    while j < 2:  # Ciclo interno
        print(f"Iteración externa {i}, interna {j}")
        j += 1
    i += 1
```

### **🔹 FOR con WHILE**
```python
for i in range(3):  # Ciclo externo
    j = 0
    while j < 2:  # Ciclo interno
        print(f"Iteración externa {i}, interna {j}")
        j += 1
```

---

## **📌 ¿Cuándo usar ciclos anidados?**  

✅ Para recorrer **tablas de datos** (filas y columnas).  
✅ Para generar **patrones y figuras** con asteriscos o números.  
✅ Para manejar **múltiples condiciones y validaciones**.  
✅ Para trabajar con **coordenadas y combinaciones**.  

---

### **Ejercicio 1: Tabla de Multiplicar (WHILE anidado) 🎯**  
📌 **Enunciado:**  
Escribe un programa que muestre las **tablas de multiplicar del 1 al 5**, donde cada tabla muestre los resultados del `1 al 10`.  

✍ **Ejemplo de salida:**  
```
Tabla del 1  
1 x 1 = 1  
1 x 2 = 2  
...  
Tabla del 5  
5 x 1 = 5  
5 x 2 = 10  
...
```

---

### **Ejercicio 2: Pirámide de Números (WHILE anidado) 🔺**  
📌 **Enunciado:**  
Solicita al usuario un número `N` y muestra una pirámide de números hasta `N`.  

✍ **Ejemplo (`N = 5`):**  
```
1  
1 2  
1 2 3  
1 2 3 4  
1 2 3 4 5  
```

---

### **Ejercicio 3: Cuadrado de Asteriscos (WHILE anidado) 🔳**  
📌 **Enunciado:**  
Pide al usuario ingresar un número `N` y muestra un cuadrado de `N x N` con asteriscos.  

✍ **Ejemplo (`N = 4`):**  
```
****
****
****
****
```

---

### **Ejercicio 4: Tablero de Ajedrez (WHILE anidado) ♟️**  
📌 **Enunciado:**  
Muestra un tablero de ajedrez de tamaño `8x8`, representando con `#` y espacios en blanco alternados.  

✍ **Ejemplo de salida:**  
```
# # # #  
 # # # #  
# # # #  
 # # # #  
```

---

### **Ejercicio 5: Validar Ingreso de Notas (WHILE anidado) ✅**  
📌 **Enunciado:**  
Un profesor ingresa notas de `N` estudiantes en `M` materias. Si la nota está fuera de `0-100`, debe pedirse nuevamente.  

✍ **Ejemplo:**  
```
Ingrese nota del estudiante 1 en materia 1: 110 ❌ (inválido)  
Ingrese nota del estudiante 1 en materia 1: 85 ✅  
```

---

### **Ejercicio 6: Pirámide Invertida (WHILE anidado) 🔻**  
📌 **Enunciado:**  
Solicita un número `N` y muestra una pirámide invertida con asteriscos.  

✍ **Ejemplo (`N=5`):**  
```
*****
****
***
**
*
```
---

### **Ejercicio 7: Números Primos en un Rango (WHILE anidado) 🔢**  
📌 **Enunciado:**  
Muestra los números **primos** entre `1 y N`, verificando en cada número si es primo.  

✍ **Ejemplo (`N = 10`):**  
```
2 3 5 7  
```
---
