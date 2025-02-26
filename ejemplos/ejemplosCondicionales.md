 
---

# **📌 Ejemplos de Condicionales en Pensamiento Algorítmico**

## **1️⃣ Condicional Simple (`Si... Entonces`)**
📌 **Ejemplo 1: Verificar si un número es mayor que 100**
### **📜 Pseudocódigo**
```pseudocode
Inicio
    Entero numero
    Escribir "Ingrese un número:"
    Leer numero

    Si numero > 100 Entonces
       Mostrar "El número es mayor que 100."
    FinSi
Fin
```
### **🐍 Código en Python**
```python
numero = int(input("Ingrese un número: "))

if numero > 100:
    print("El número es mayor que 100.")
```

📌 **Ejemplo 2: Comprobar si una palabra tiene más de 5 caracteres**
### **📜 Pseudocódigo**
```pseudocode
Inicio
    Caracter palabra
    Escribir "Ingrese una palabra:"
    Leer palabra

    Si Longitud(palabra) > 5 Entonces
        Mostrar "La palabra tiene más de 5 caracteres."
    FinSi
Fin
```
### **🐍 Código en Python**
```python
palabra = input("Ingrese una palabra: ")

if len(palabra) > 5:
    print("La palabra tiene más de 5 caracteres.")
```

📌 **Ejemplo 3: Verificar si un número es negativo**
### **📜 Pseudocódigo**
```pseudocode
Inicio
    Entero numero
    Escribir "Ingrese un número:"
    Leer numero

    Si numero < 0 Entonces
        Mostrar "El número es negativo."
    FinSi
Fin
```
### **🐍 Código en Python**
```python
numero = int(input("Ingrese un número: "))

if numero < 0:
    print("El número es negativo.")
```

---

## **2️⃣ Condicional Doble (`Si... Entonces... SiNo`)**
📌 **Ejemplo 1: Determinar si un número es par o impar**
### **📜 Pseudocódigo**
```pseudocode
Inicio
    Entero numero
    Escribir "Ingrese un número:"
    Leer numero

    Si numero MOD 2 == 0 Entonces
        Mostrar "El número es par."
    SiNo
        Mostrar "El número es impar."
    FinSi
Fin
```
### **🐍 Código en Python**
```python
numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
```

📌 **Ejemplo 2: Verificar si un usuario tiene acceso según su edad**
### **📜 Pseudocódigo**
```pseudocode
Inicio
    Entero edad
    Escribir "Ingrese su edad:"
    Leer edad

    Si edad >= 18 Entonces
        Mostrar "Acceso permitido."
    SiNo
        Mostrar "Acceso denegado."
    FinSi
Fin
```
### **🐍 Código en Python**
```python
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Acceso permitido.")
else:
    print("Acceso denegado.")
```

📌 **Ejemplo 3: Comparar dos números y decir cuál es mayor**
### **📜 Pseudocódigo**
```pseudocode
Inicio
    Entero num1, num2
    Escribir "Ingrese el primer número:"
    Leer num1
    Escribir "Ingrese el segundo número:"
    Leer num2

    Si num1 > num2 Entonces
        Mostrar "El primer número es mayor."
    SiNo
        Mostrar "El segundo número es mayor o son iguales."
    FinSi
Fin
```
### **🐍 Código en Python**
```python
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 > num2:
    print("El primer número es mayor.")
else:
    print("El segundo número es mayor o son iguales.")
```

---

## **3️⃣ Condicional Múltiple (`Si...Entonces...SinoSi`)**
📌 **Ejemplo 1: Evaluar la calificación de un estudiante**
### **📜 Pseudocódigo**
```pseudocode
Inicio
    Real nota
    Escribir "Ingrese la calificación:"
    Leer nota

    Si 0 <= nota < 3 entones
        Mostrar "Reprobo"
    SinoSi 3 <= nota < 4 entoneces
        Mostrar "Aprobo"
    SinoSi 4 <= nota <= 5 entonces
        Mostrar "Aprobo con honores"
    Sino entonces
        Mostrar "Ingrese una nota en el rango adecuado"
    FinSi
Fin
```
### **🐍 Código en Python**
```python
nota = int(input("Ingrese la calificación: "))

if 0 <= nota < 3:
    print("Reprobo")
elif 3 <= nota < 4:
    print("Aprobo")
elif 4 <= nota <= 5:
    print("Aprobo con honores")
else:
    print("Ingrese una nota en el rango adecuado")
```

📌 **Ejemplo 2: Determinar el tipo de figura según el número de lados**
### **📜 Pseudocódigo**
```pseudocode
Inicio
    Entero lados
    Escribir "Ingrese el número de lados de la figura:"
    Leer lados

    Si lados == 3 entonces
        Mostrar "Es un triángulo"
    SinoSi lados == 4 entonces
        Mostrar "Es una cuadrado o un rectángulo
    SinoSi lados == 5 entonces
        Mostrar "Es un pentágono"
    SinoSi lados == 6 entonces
        Mostrar "Es un hexágono"
    Sino entonces
        Mostrar "No se reconoce la figura"
    FinSi
Fin
```
### **🐍 Código en Python**
```python
lados = int(input("Ingrese el número de lados de la figura: "))

if lados == 3:
    print("Es un triángulo")
elif lados == 4:
    print(" Es un cuadrado o un rectángulo")
elif lados == 5:
    print("Es un pentágono")
elif lados == 6:
    print("Es un hexágono")
else:
    print("No se reconoce la figura")
```

📌 **Ejemplo 3: Determinar el tipo de día de la semana**
### **📜 Pseudocódigo**
```pseudocode
Inicio
    Definir dia Como Entero
    Escribir "Ingrese un número del 1 al 7:"
    Leer dia

    Si 1 <= dia <= 5 entonces
        Mostrar "Día laboral"
    SinoSi 6 <= dia <= 7 entonces
        Mostrar "Fin de semana"
    Sino entonces
        Mostrar "Numero inválido"
    FinSi
Fin
```
### **🐍 Código en Python**
```python
dia = int(input("Ingrese un número del 1 al 7: "))

if 1 <= dia <= 5:
    print("Día laboral")
elif 6 <= dia <= 7:
    print("Fin de semana")
else:
    print("Número inválido")
```

---
