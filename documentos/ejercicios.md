# 📌 Introducción a Python

## 🐍 ¿Qué es Python?

Python es un **lenguaje de programación interpretado, de alto nivel y multiparadigma**, diseñado para ser fácil de leer y escribir. Es ampliamente utilizado en diversas áreas como desarrollo web, análisis de datos, inteligencia artificial y automatización.

### 📜 Características de Python:
✅ **Sintaxis sencilla y clara**: Su código es fácil de leer y escribir.  
✅ **Interpretado**: No requiere compilación, se ejecuta directamente.  
✅ **Multiparadigma**: Soporta programación **imperativa, orientada a objetos y funcional**.  
✅ **Extensible y embebible**: Puede integrarse con otros lenguajes como C y Java.  
✅ **Gran comunidad y librerías**: Existen muchas bibliotecas disponibles para diversas tareas.

---

## 🔧 ¿Cómo funciona Python?

Python es un lenguaje **interpretado**, lo que significa que su código se ejecuta línea por línea en un **intérprete** en lugar de ser compilado a código máquina previamente.

### 🔹 Proceso de ejecución de un programa en Python:
1. **Escribimos el código fuente** en un archivo `.py`.
2. **El intérprete de Python lee el código** y lo traduce a un formato intermedio llamado **bytecode**.
3. **El bytecode es ejecutado por la máquina virtual de Python (PVM)**, que interpreta cada instrucción y la ejecuta en el sistema operativo.

📌 Ejemplo de código básico en Python:
```python
print("¡Hola, mundo!")
```

Al ejecutar este código, el intérprete mostrará:
```
¡Hola, mundo!
```

---

## ⚙️ Generalidades de Python

### 🔹 **Tipado Dinámico**
Python no requiere declarar el tipo de una variable, ya que lo asigna automáticamente en tiempo de ejecución.
```python
x = 10  # Entero
x = "Python"  # Ahora es una cadena
```

### 🔹 **Indentación Obligatoria**
Python usa **indentación** en lugar de llaves `{}` para definir bloques de código, lo que mejora la legibilidad.
```python
if True:
    print("Esto está indentado correctamente")
```
❌ Si la indentación es incorrecta, Python generará un error.

### 🔹 **Multiparadigma**
Python permite programar en distintos estilos:
- **Imperativo** (estructurado con variables y control de flujo).
- **Orientado a objetos** (usando clases y objetos).
- **Funcional** (usando funciones como elementos de primera clase).

### 🔹 **Interpretado e Interactivo**
Puedes ejecutar Python línea por línea en un **entorno interactivo (REPL)** simplemente escribiendo `python` en la terminal.
```python
>>> 2 + 2
4
```

---

## 🚀 Aplicaciones de Python
Python se usa en muchas áreas de la informática, como:

🔹 **Desarrollo Web** → Django, Flask.  
🔹 **Ciencia de Datos** → Pandas, NumPy, Matplotlib.  
🔹 **Inteligencia Artificial y Machine Learning** → TensorFlow, Scikit-Learn.  
🔹 **Automatización y Scripting** → Manipulación de archivos, procesos repetitivos.  
🔹 **Ciberseguridad** → Análisis de seguridad, pruebas de penetración.  
🔹 **Desarrollo de Juegos** → Pygame, Panda3D.  

---

## 🛠 Instalación y Primeros Pasos

### 🔹 **Instalar Python**
1. Descarga la última versión desde [python.org](https://www.python.org/).
2. Asegúrate de marcar la opción **"Add Python to PATH"** al instalar.
3. Verifica la instalación ejecutando:
   ```bash
   python --version
   ```

### 🔹 **Ejecutar un Script en Python**
Guarda un archivo con extensión `.py` y ejecútalo desde la terminal:
```bash
python mi_programa.py
```

### 🔹 **Usar el intérprete interactivo (REPL)**
Para probar código rápidamente, abre la terminal y escribe:
```bash
python
```
Luego, puedes escribir código directamente:
```python
>>> print("Hola, Python")
Hola, Python
```

---

# 📌 Ejercicio de Programación Secuencial

Estos ejercicios están diseñados para evaluar el dominio de la **programación secuencial** y la lógica de pseudocódigo. **No se incluyen estructuras condicionales ni ciclos**, ya que solo se trabaja con secuencias de instrucciones.

---

## **🏋️ Ejercicio 1: Conversión de Unidades**
Escribe un algoritmo que convierta una cantidad ingresada en **metros** a **centímetros y milímetros**.

---

## **🏋️ Ejercicio 2: Cálculo de Nómina**
Diseña un algoritmo que calcule el salario semanal de un empleado, considerando:
- Un pago por hora estándar.
- El número de horas trabajadas en la semana.
- Mostrar el sueldo total.

---

## **🏋️ Ejercicio 3: Facturación con IVA**
Crea un algoritmo que solicite el monto total de una compra y:
- Calcule el IVA (16%).
- Muestre el monto final a pagar.

---

## **🏋️ Ejercicio 4: Cálculo de Raíces Cuadradas**
Elabora un algoritmo que solicite un número al usuario y devuelva su raíz cuadrada.
Si el número es negativo, el programa debe **mostrar un mensaje indicando que no se puede calcular** (sin usar condicionales, solo imprimir el resultado esperado para números negativos).

---

## **🏋️ Ejercicio 5: Conversión de Tiempo**
Pide al usuario una cantidad de **segundos** y conviértela a **horas, minutos y segundos**.
Ejemplo:
```
Entrada: 3665 segundos
Salida: 1 hora, 1 minuto, 5 segundos
```

---

## **🏋️ Ejercicio 6: Promedio de Calificaciones**
Crea un algoritmo que reciba **cinco calificaciones** y calcule el promedio final.

---

## **🏋️ Ejercicio 7: Cálculo de Área y Perímetro de un Círculo**
Elabora un algoritmo que solicite el radio de un círculo y calcule:
- Su área: `π * radio^2`
- Su perímetro: `2 * π * radio`

---

## **🏋️ Ejercicio 8: Conversión de Moneda**
El usuario ingresa una cantidad en **dólares** y el programa debe convertirlo a **euros** y **pesos mexicanos** (usar tasas de cambio fijas).

---

## **🏋️ Ejercicio 9: Precio Total con Propina**
Diseña un algoritmo que solicite el costo de una comida y el porcentaje de propina a dejar. 
Mostrar el total a pagar.

---

## **🏋️ Ejercicio 10: Cálculo del Volumen de una Esfera**
Elabora un algoritmo que solicite el radio de una esfera y calcule su volumen usando la fórmula:
```
Volumen = (4/3) * π * radio^3
```

---

## **🏋️ Ejercicio 11: Cálculo de la Velocidad Promedio**
Elabora un algoritmo que solicite la distancia recorrida y el tiempo empleado, luego calcule la velocidad promedio.

---

## **🏋️ Ejercicio 12: Cálculo de la Energía Cinética**
El usuario debe ingresar la masa y la velocidad de un objeto, y el algoritmo calculará la energía cinética usando la fórmula:
```
Energía Cinética = 0.5 * masa * velocidad^2
```

---

## **🏋️ Ejercicio 13: Conversión de Notación Científica a Decimal**
Elabora un algoritmo que convierta un número expresado en notación científica a su forma decimal.

---

## **🏋️ Ejercicio 14: Cálculo del Costo de un Viaje**
El usuario ingresará la distancia a recorrer, el consumo de combustible del vehículo (litros por kilómetro) y el precio del combustible, y el programa calculará el costo total del viaje.

---

## **🏋️ Ejercicio 15: Conversión de Horas a Formato AM/PM**
Solicita una hora en formato de 24 horas y conviértela a formato AM/PM.

---

## **🏋️ Ejercicio 16: Determinación del Tiempo de Cocción**
Crea un algoritmo que solicite el peso de un alimento y calcule el tiempo de cocción basado en un tiempo fijo por kilogramo.

---

## **🏋️ Ejercicio 17: Cálculo de la Densidad de un Objeto**
El usuario ingresará la masa y el volumen de un objeto, y el programa calculará su densidad usando la fórmula:
```
Densidad = Masa / Volumen
```

---

## **🏋️ Ejercicio 18: Cálculo del Cambio en una Compra**
El usuario ingresará el total de la compra y la cantidad de dinero entregada, y el programa calculará el cambio que debe recibir.

---

## **🏋️ Ejercicio 19: Cálculo del Rendimiento de Combustible**
Elabora un algoritmo que solicite la cantidad de kilómetros recorridos y los litros de combustible usados, y calcule el rendimiento en kilómetros por litro.

---

## **🏋️ Ejercicio 20: Conversión de Unidades de Masa**
Crea un algoritmo que convierta una cantidad ingresada en **gramos** a **kilogramos y toneladas**.

---

🚀 **Estos ejercicios ayudarán a reforzar los conceptos de programación secuencial en un nivel avanzado. ¡Practica y domina la lógica!** 😃

# 📌 Ejemplos y Ejercicios de Programación Secuencial y Pseudocódigo

## 📝 **Ejemplos de Programación Secuencial y Pseudocódigo**

### **Ejemplo 1: Saludo simple**
```
Inicio
    Escribir "¡Hola, bienvenido al mundo de la programación!"
Fin
```

### **Ejemplo 2: Suma de dos números**
```
Inicio
    Leer num1, num2
    resultado ← num1 + num2
    Escribir "La suma es: ", resultado
Fin
```

### **Ejemplo 3: Calcular el área de un rectángulo**
```
Inicio
    Leer base, altura
    area ← base * altura
    Escribir "El área del rectángulo es: ", area
Fin
```

### **Ejemplo 4: Promedio de tres números**
```
Inicio
    Leer num1, num2, num3
    promedio ← (num1 + num2 + num3) / 3
    Escribir "El promedio es: ", promedio
Fin
```

### **Ejemplo 5: Conversión de grados Celsius a Fahrenheit**
```
Inicio
    Leer celsius
    fahrenheit ← (celsius * 9/5) + 32
    Escribir "Temperatura en Fahrenheit: ", fahrenheit
Fin
```

### **Ejemplo 6: Calcular el perímetro de un círculo**
```
Inicio
    Leer radio
    perimetro ← 2 * 3.1416 * radio
    Escribir "El perímetro del círculo es: ", perimetro
Fin
```

### **Ejemplo 7: Calcular descuento en una compra**
```
Inicio
    Leer precio, descuento
    total ← precio - (precio * descuento / 100)
    Escribir "Precio con descuento: ", total
Fin
```

### **Ejemplo 8: Intercambiar valores de dos variables**
```
Inicio
    Leer a, b
    aux ← a
    a ← b
    b ← aux
    Escribir "Nuevo valor de a: ", a
    Escribir "Nuevo valor de b: ", b
Fin
```

### **Ejemplo 9: Calcular salario semanal**
```
Inicio
    Leer horas_trabajadas, pago_por_hora
    salario ← horas_trabajadas * pago_por_hora
    Escribir "Salario semanal: ", salario
Fin
```

### **Ejemplo 10: Conversión de días a semanas y días restantes**
```
Inicio
    Leer dias
    semanas ← dias / 7
    dias_restantes ← dias MOD 7
    Escribir "Semanas: ", semanas, " Días restantes: ", dias_restantes
Fin
```
