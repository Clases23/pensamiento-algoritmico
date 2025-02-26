
---

# **📌 Ejercicios de Práctica - Condicionales**
🎯 **Objetivo:** Aplicar el uso de **condicionales simples, dobles y múltiples** en problemas de dificultad progresiva.  

✅ **Tipos de Condicionales Cubiertos:**  
1️⃣ **Condicional Simple (`Si... Entonces`)**  
2️⃣ **Condicional Doble (`Si... Entonces... SiNo`)**  
3️⃣ **Condicional Múltiple (`Si... Entonces... SinoSi`)**  

Cada ejercicio debe resolverse en **pseudocódigo y Python**.  

---

## **1️⃣ Ejercicios de Condicional Simple (`Si... Entonces`)**
📌 **Concepto:** Se ejecuta **una acción** solo si la condición se cumple.  

### **Ejercicio 1 - Verificar Número Positivo** ✅ *(Fácil)*
📜 **Instrucciones:**  
1. Pedir al usuario un número.  
2. Si el número es mayor que **0**, mostrar `"El número es positivo."`.  

---

### **Ejercicio 2 - Mayor de Edad** ✅ *(Fácil)*
📜 **Instrucciones:**  
1. Pedir la **edad del usuario**.  
2. Si tiene **18 años o más**, mostrar `"Eres mayor de edad."`.  

---

### **Ejercicio 3 - Múltiplo de 5** ✅ *(Intermedio)*
📜 **Instrucciones:**  
1. Pedir un número.  
2. Si el número **es múltiplo de 5**, mostrar `"El número es múltiplo de 5."`.  

---

### **Ejercicio 4 - Descuento por Compra** ✅ *(Intermedio)*
📜 **Instrucciones:**  
1. Pedir el **monto total de la compra**.  
2. Si el monto es **mayor o igual a $1000**, mostrar `"Descuento aplicado: 10%."`.  

---

### **Ejercicio 5 - Evaluación de un Examen** ✅ *(Difícil)*
📜 **Instrucciones:**  
1. Pedir la **nota del estudiante**.  
2. Si la nota es **mayor o igual a 60**, mostrar `"Aprobado."`.  

---

## **2️⃣ Ejercicios de Condicional Doble (`Si... Entonces... SiNo`)**
📌 **Concepto:** Se ejecuta **una acción si la condición se cumple** y **otra si no se cumple**.  

### **Ejercicio 1 - Número Par o Impar** ✅ *(Fácil)*
📜 **Instrucciones:**  
1. Pedir un número.  
2. Si es **par**, mostrar `"El número es par."`.  
3. Si no, mostrar `"El número es impar."`.  

---

### **Ejercicio 2 - Determinar Mayor o Menor** ✅ *(Fácil)*
📜 **Instrucciones:**  
1. Pedir dos números.  
2. Mostrar cuál es el **mayor** y cuál es el **menor**.  

---

### **Ejercicio 3 - Temperatura** ✅ *(Intermedio)*
📜 **Instrucciones:**  
1. Pedir la **temperatura en grados Celsius**.  
2. Si es **mayor o igual a 30°C**, mostrar `"Hace calor."`.  
3. Si es **menor a 30°C**, mostrar `"El clima es fresco."`.  

---

### **Ejercicio 4 - Comparación de Números** ✅ *(Intermedio)*
📜 **Instrucciones:**  
1. Pedir **dos números**.  
2. Mostrar `"El primer número es mayor."`, `"El segundo número es mayor."` o `"Son iguales."`.  

---

### **Ejercicio 5 - Determinar si un Año es Bisiesto** ✅ *(Difícil)*
📜 **Instrucciones:**  
1. Pedir un **año**.  
2. Si es divisible entre 4 y **no es divisible entre 100**, o **es divisible entre 400**, mostrar `"El año es bisiesto."`.  
3. Si no, mostrar `"El año no es bisiesto."`.  

---

## **3️⃣ Ejercicios de Condicional Múltiple (`Segun... Hacer`)**
📌 **Concepto:** Se evalúan **varios casos posibles** y se ejecuta una acción según el caso.  

### **Ejercicio 1 - Días de la Semana** ✅ *(Fácil)*
📜 **Instrucciones:**  
1. Pedir un número del **1 al 7**.  
2. Mostrar el **día de la semana correspondiente** (`1 = Lunes`, `2 = Martes`, etc.).  

---

### **Ejercicio 2 - Evaluación de Notas** ✅ *(Intermedio)*
📜 **Instrucciones:**  
1. Pedir la **nota del estudiante**.  
2. Clasificar la nota en:  
   - `0-5`: `"Reprobado."`  
   - `6-7`: `"Regular."`  
   - `8-9`: `"Bueno."`  
   - `10`: `"Excelente."`  

---

### **Ejercicio 3 - Tipo de Triángulo** ✅ *(Intermedio)*
📜 **Instrucciones:**  
1. Pedir **tres lados** de un triángulo.  
2. Determinar si es:  
   - `"Equilátero"` (todos los lados iguales).  
   - `"Isósceles"` (dos lados iguales).  
   - `"Escaleno"` (todos diferentes).  

---

### **Ejercicio 4 - Clasificación de Números** ✅ *(Difícil)*
📜 **Instrucciones:**  
1. Pedir un número.  
2. Clasificarlo en:  
   - `"Positivo y Par"`  
   - `"Positivo e Impar"`  
   - `"Negativo y Par"`  
   - `"Negativo e Impar"`  
   - `"Cero"`  

---

### **Ejercicio 5 - Conversión de Notas a Letras** ✅ *(Difícil)*
📜 **Instrucciones:**  
1. Pedir una **nota numérica**.  
2. Convertirla en una **calificación con letras** según esta tabla:  
   - `90-100 → "A"`  
   - `80-89 → "B"`  
   - `70-79 → "C"`  
   - `60-69 → "D"`  
   - `<60 → "F"`  

---

# **📌 Ejercicios de Lectura de Pseudocódigo**  
📜 **Instrucciones:**  
1️⃣ Analiza el pseudocódigo presentado en cada ejercicio.  
2️⃣ Predice la salida del programa para los datos de entrada indicados.  
3️⃣ Escribe tu respuesta basándote en la lógica del código.  

---


## **2️⃣ Ejercicio 1 - Cálculo de Descuento**
📌 **Pseudocódigo:**  
```pseudocode
Inicio
    Real totalCompra, totalPagar
    Escribir "Ingrese el total de la compra:"
    Leer totalCompra

    Si totalCompra > 1000 entonces
        totalPagar = totalCompra * 0.9
    Sino entonces
        totalPagar = totalCompra
    FinSi

    Escribir "Total a pagar:", totalPagar
Fin
```
📌 **Preguntas:**  
1️⃣ ¿Cuál será la salida si el usuario ingresa `totalCompra = 1200`?  
2️⃣ ¿Cuál será la salida si `totalCompra = 800`?  

✍️ **Respuestas:** **___**

---

## **3️⃣ Ejercicio 2 - Clasificación de Números**
📌 **Pseudocódigo:**  
```pseudocode
Inicio
    Entero numero
    Escribir "Ingrese un número:"
    Leer numero

    Si numero > 0 entonces
        Mostrar "Positivo"
    SinoSi numero < 0 entonces
        Mostrar "Negativo"
    Sino entonces
        Mostrar "Cero"
    FinSi
Fin
```
📌 **Preguntas:**  
1️⃣ ¿Cuál será la salida si el usuario ingresa `numero = -5`?  
2️⃣ ¿Qué mostrará si `numero = 0`?  

✍️ **Respuestas:** **___**

---

## **5️⃣ Ejercicio 3 - Comparación de Tres Números**
📌 **Pseudocódigo:**  
```pseudocode
Inicio
    Entero a, b, c
    Escribir "Ingrese el primer número:"
    Leer a
    Escribir "Ingrese el segundo número:"
    Leer b
    Escribir "Ingrese el tercer número:"
    Leer c

    Si a > b Y a > c entonces
        Mostrar "El mayor es:", a
    SinoSi b > a Y b > c entonces
        Mostrar "El mayor es:", b
    Sino entonces
        Mostrar "El mayor es:", c
    FinSi
Fin
```
📌 **Preguntas:**  
1️⃣ ¿Qué mostrará el programa si `a = 7`, `b = 10`, `c = 3`?  
2️⃣ ¿Qué mostrará si los tres números son iguales (`a = b = c = 5`)?  

✍️ **Respuestas:** **___**

---
