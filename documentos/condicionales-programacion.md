---

# **📌 Condicionales en Programación**
Los **condicionales** permiten ejecutar diferentes bloques de código según una condición lógica. Son fundamentales en la programación para tomar decisiones.

## **🔹 Tipos de Condicionales**
1. **Condicional simple** → Ejecuta una acción si la condición es **verdadera**.  
2. **Condicional doble** → Ejecuta una acción si la condición es **verdadera**, y otra diferente si es **falsa**.  
3. **Condicional múltiple** → Evalúa varias condiciones y ejecuta la que corresponda.

---

## **1️⃣ Condicional Simple (`Si... Entonces`)**
Un **condicional simple** ejecuta un bloque de código si la condición es **verdadera**.  
Si es **falsa**, no hace nada.

### **📌 Ejemplo en Pseudocódigo**
```pseudocode
Algoritmo Mayor_de_edad
    Entero edad 
    Escribir "Ingrese su edad:"
    Leer edad
    Si edad >= 18 Entonces
        Escribir "Eres mayor de edad."
    FinSi
FinAlgoritmo
```
🔹 **Explicación:**
- Si el usuario ingresa **18 o más**, se muestra el mensaje.
- Si ingresa un número menor, **no se ejecuta nada**.

### **📌 Ejemplo en Python**
```python
edad = int(input("Ingrese su edad: "))

if edad >= 18:
    print("Eres mayor de edad.")
```
🔹 **Explicación:**
- `if` evalúa si `edad` es **mayor o igual a 18**.
- Si es verdadero, imprime `"Eres mayor de edad."`.
- Si es falso, no hace nada.

---

## **2️⃣ Condicional Doble (`Si... Entonces... SiNo`)**
Un **condicional doble** ejecuta un bloque de código si la condición es **verdadera**.  
Si es **falsa**, ejecuta otra acción alternativa.

### **📌 Ejemplo en Pseudocódigo**
```pseudocode
Algoritmo Par_o_Impar
    Entero numero 
    Escribir "Ingrese un número:"
    Leer numero
    Si numero MOD 2 == 0 Entonces
        Escribir "El número es par."
    SiNo
        Escribir "El número es impar."
    FinSi
FinAlgoritmo
```
🔹 **Explicación:**
- Si el número es **divisible por 2**, se imprime `"El número es par."`
- Si no, se ejecuta el bloque dentro de `SiNo`, mostrando `"El número es impar."`

### **📌 Ejemplo en Python**
```python
numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")
```
🔹 **Explicación:**
- `if` evalúa si `numero % 2 == 0` (**es par**).
- `else` se ejecuta si la condición es falsa (**es impar**).

---

## **3️⃣ Condicional Múltiple (`Segun... Hacer`)**
Cuando tenemos **más de dos condiciones**, usamos **condicionales múltiples**.

### **📌 Ejemplo en Pseudocódigo (`Segun... Hacer`)**
```pseudocode
Algoritmo Calificacion
    Real nota
    Escribir "Ingrese la nota del estudiante:"
    Leer nota
    Segun nota Hacer
        0 hasta 5: Escribir "Reprobado"
        6 hasta 7: Escribir "Regular"
        8 hasta 9: Escribir "Bueno"
        10: Escribir "Excelente"
    FinSegun
FinAlgoritmo
```
🔹 **Explicación:**
- Evalúa `nota` y muestra un mensaje según el **rango de valores**.

### **📌 Ejemplo en Python (`elif`)**
```python
nota = float(input("Ingrese la nota del estudiante: "))

if 0 <= nota <= 5:
    print("Reprobado")
elif 6 <= nota <= 7:
    print("Regular")
elif 8 <= nota <= 9:
    print("Bueno")
elif nota == 10:
    print("Excelente")
else:
    print("Nota inválida")
```
🔹 **Explicación:**
- Se usa `elif` para evaluar **varias condiciones**.
- El `else` maneja el caso de **valores inválidos**.

---

## **4️⃣ Uso de Condiciones Compuestas (`Y`, `O`)**
Podemos combinar condiciones usando **operadores lógicos**:

| Operador | Descripción |
|----------|------------|
| `Y` (AND) | Ambas condiciones deben ser **verdaderas** |
| `O` (OR) | Al menos una condición debe ser **verdadera** |
| `NO` (NOT) | Invierte el valor de la condición |

### **📌 Ejemplo en Pseudocódigo**
```pseudocode
Algoritmo Descuento
    Entero edad
    Escribir "Ingrese su edad:"
    Leer edad
    Si edad >= 18 Y edad <= 25 Entonces
        Escribir "Tienes un descuento del 20%."
    FinSi
FinAlgoritmo
```
🔹 **Explicación:**
- Solo los que tienen entre **18 y 25 años** obtienen descuento.

### **📌 Ejemplo en Python**
```python
edad = int(input("Ingrese su edad: "))

if 18 <= edad <= 25:
    print("Tienes un descuento del 20%.")
```
🔹 **Explicación:**
- Se usa `and` para verificar que **ambas condiciones sean verdaderas**.

---

## **🎯 Resumen**
| Tipo de Condicional | Pseudocódigo | Python |
|---------------------|-------------|--------|
| **Condicional Simple** | `Si... Entonces` | `if` |
| **Condicional Doble** | `Si... Entonces... SiNo` | `if... else` |
| **Condicional Múltiple** | `Segun... Hacer` | `if... elif... else` |
| **Condiciones Compuestas** | `Y, O, NO` | `and, or, not` |
---

# **📌 Uso de Banderas en Condicionales**
Las **banderas** son variables lógicas (`Booleanas`) que se utilizan en programación para **controlar el flujo de ejecución** dentro de una estructura condicional.

## **🔹 ¿Qué es una Bandera?**
Una **bandera** es una variable que almacena un **estado**, generalmente representado por valores booleanos (`Verdadero/Falso` o `True/False` en Python).  
Se usa para indicar si una condición se ha cumplido o no.

✅ **Ejemplo de uso:**  
- **Indicar si un usuario ha ingresado datos válidos.**  
- **Determinar si una condición ha ocurrido en un proceso.**  
- **Evitar ejecutar código repetidamente cuando una condición ya se ha cumplido.**

---

## **1️⃣ Uso de Banderas en Condicionales Simples**
Las banderas pueden inicializarse con un valor (`Verdadero` o `Falso`) y cambiar dentro de un condicional.

### **📌 Ejemplo en Pseudocódigo**
```pseudocode
Algoritmo Verificar_Acceso
    Logico accesoPermitido
    accesoPermitido = Falso
    
    Escribir "Ingrese la clave de acceso:"
    Leer clave

    Si clave = "1234" Entonces
        accesoPermitido =  Verdadero
    FinSi

    Si accesoPermitido Entonces
        Escribir "Acceso concedido."
    SiNo
        Escribir "Acceso denegado."
    FinSi
FinAlgoritmo
```
🔹 **Explicación:**  
- Se inicializa `accesoPermitido` en `Falso`.  
- Si la clave ingresada es `"1234"`, cambia a `Verdadero`.  
- Se usa la bandera para determinar si el usuario puede acceder.

### **📌 Ejemplo en Python**
```python
acceso_permitido = False

clave = input("Ingrese la clave de acceso: ")

if clave == "1234":
    acceso_permitido = True

if acceso_permitido:
    print("Acceso concedido.")
else:
    print("Acceso denegado.")
```
🔹 **Explicación:**  
- Se usa una variable `acceso_permitido` para almacenar el estado de validación.  
- Si la clave es correcta, cambia a `True` y permite el acceso.  

---

## **2️⃣ Uso de Banderas en Condiciones Compuestas**
Las banderas también se pueden combinar con operadores lógicos (`Y`, `O`).

### **📌 Ejemplo en Pseudocódigo**
```pseudocode
Algoritmo Validar_Usuario
    Logico usuarioValido, claveCorrecta
    usuarioValido = Falso
    claveCorrecta =  Falso
    
    Escribir "Ingrese su usuario:"
    Leer usuario
    Escribir "Ingrese su clave:"
    Leer clave

    Si usuario = "admin" Entonces
        usuarioValido = Verdadero
    FinSi

    Si clave = "secreto" Entonces
        claveCorrecta = Verdadero
    FinSi

    Si usuarioValido Y claveCorrecta Entonces
        Escribir "Inicio de sesión exitoso."
    SiNo
        Escribir "Usuario o clave incorrectos."
    FinSi
FinAlgoritmo
```
🔹 **Explicación:**  
- Se usan **dos banderas** (`usuarioValido` y `claveCorrecta`).  
- Ambas deben ser `Verdadero` para permitir el inicio de sesión.

### **📌 Ejemplo en Python**
```python
usuario_valido = False
clave_correcta = False

usuario = input("Ingrese su usuario: ")
clave = input("Ingrese su clave: ")

if usuario == "admin":
    usuario_valido = True

if clave == "secreto":
    clave_correcta = True

if usuario_valido and clave_correcta:
    print("Inicio de sesión exitoso.")
else:
    print("Usuario o clave incorrectos.")
```
🔹 **Explicación:**  
- Se verifican **dos condiciones separadas**.  
- Ambas deben ser `True` para que el usuario pueda iniciar sesión.

---

## **3️⃣ Uso de Banderas para Evitar Ejecución Repetida**
Las banderas también son útiles para evitar que un código se ejecute varias veces cuando ya se ha cumplido una condición.

### **📌 Ejemplo en Pseudocódigo**
```pseudocode
Algoritmo Descuento_Aplicado
    Logico descuentoAplicado
    descuentoAplicado = Falso

    Escribir "Ingrese el total de la compra:"
    Leer totalCompra

    Si totalCompra > 1000 Entonces
        Si No descuentoAplicado Entonces
            Escribir "Descuento del 10% aplicado."
            descuentoAplicado = Verdadero
        FinSi
    SiNo
        Escribir "No aplica descuento."
    FinSi
FinAlgoritmo
```

### **📌 Ejemplo en Python**
```python
descuento_aplicado = False

total_compra = float(input("Ingrese el total de la compra: "))

if total_compra > 1000:
    if not descuento_aplicado:
        print("Descuento del 10% aplicado.")
        descuento_aplicado = True
else:
    print("No aplica descuento.")
```
🔹 **Explicación:**  
- Se usa la bandera `descuento_aplicado` para evitar que el descuento se aplique más de una vez.

---

## **🎯 Resumen**
| Concepto | Uso |
|----------|-----|
| **Banderas en Condicionales** | Se usan para guardar un estado lógico. |
| **Inicialización de Banderas** | Generalmente comienzan en `Falso` y cambian a `Verdadero` cuando se cumple una condición. |
| **Uso con `Y`, `O`, `NO`** | Se pueden combinar para evaluar múltiples condiciones. |
| **Evitar Ejecuciones Repetidas** | Se usan para asegurarse de que un bloque de código se ejecute solo una vez. |

## 	:warning: Aclaración
En python cuando evaluamos la condición:
```python
    booleano = True
    if booleano:
        print("HolaMundo")
```
siempre toma esa condición como verdaera, o sea se pregunta por defecto si es verdadero.

---






