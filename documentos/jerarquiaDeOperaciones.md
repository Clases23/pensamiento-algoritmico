
---

# **📌 Jerarquía de Operaciones**  

## **🔹 ¿Qué es la Jerarquía de Operaciones?**  
La **jerarquía de operaciones** es el conjunto de **reglas matemáticas** que determinan el orden en que deben resolverse las operaciones dentro de una expresión.  

✅ **Propósito:**  
- Evitar ambigüedades en cálculos.  
- Garantizar que los resultados sean correctos y consistentes.  
- Aplicar reglas universales para interpretar expresiones matemáticas.  

📌 **Ejemplo:**  
```pseudocode
resultado = 5 + 3 * 2
```
**¿El resultado es 16 o 11?**  
Depende de la jerarquía de operaciones.  

---

## **🔹 Reglas de la Jerarquía de Operaciones**  
La jerarquía sigue un **orden específico** de evaluación:

| **Orden** | **Operaciones** | **Ejemplo** |
|-----------|----------------|-------------|
| 1️⃣ **Paréntesis** | `( )` Agrupar operaciones | `(2 + 3) * 4 = 20` |
| 2️⃣ **Exponentes y raíces** | `^`, `√` (potencias y raíces) | `2 ^ 3 = 8` |
| 3️⃣ **Multiplicación y división** | `*`, `/`, `MOD` (izq. a der.) | `10 / 2 * 3 = 15` |
| 4️⃣ **Suma y resta** | `+`, `-` (izq. a der.) | `8 - 3 + 2 = 7` |

✅ **Reglas clave:**  
- **Los paréntesis siempre tienen la máxima prioridad.**  
- **Las operaciones del mismo nivel se evalúan de izquierda a derecha.**  
- **Exponentes y raíces se calculan antes que multiplicación o división.**  

---

## **🔹 Jerarquía de Operaciones en Pseudocódigo**  
📌 **Ejemplo 1 - Aplicando la jerarquía**  
```pseudocode
Inicio
    Real resultado1, resultado2
    resultado1 = 5 + 3 * 2
    resultado2 = (5 + 3) * 2
    Escribir "Resultado 1:", resultado1  // Salida: 11
    Escribir "Resultado 2:", resultado2  // Salida: 16
Fin
```
✅ **Explicación:**  
- En `resultado1`, la multiplicación `3 * 2` se evalúa primero, luego la suma.  
- En `resultado2`, los paréntesis `5 + 3` se evalúan primero, luego la multiplicación.  

---

## **🔹 Jerarquía de Operaciones en Python**  
📌 **Ejemplo 2 - Evaluando expresiones en Python**  
```python
resultado1 = 5 + 3 * 2
resultado2 = (5 + 3) * 2

print("Resultado 1:", resultado1)  # Salida: 11
print("Resultado 2:", resultado2)  # Salida: 16
```
✅ **Explicación:**  
- Python sigue la misma jerarquía de operaciones que las matemáticas.  
- **Paréntesis (`()`)** siempre se evalúan primero.  

---

## **🔹 Operaciones de Módulo y División Entera**
📌 **Ejemplo 3 - Uso de `MOD` y División Entera**  
```pseudocode
Inicio
    Entero resultado1, resultado2
    resultado1 = 10 MOD 3
    resultado2 = 10 DIV 3
    Escribir "Módulo:", resultado1  // Salida: 1
    Escribir "División entera:", resultado2  // Salida: 3
Fin
```
📌 **Ejemplo en Python:**
```python
resultado1 = 10 % 3
resultado2 = 10 // 3

print("Módulo:", resultado1)  # Salida: 1
print("División entera:", resultado2)  # Salida: 3
```
✅ **Explicación:**  
- `MOD` devuelve el **residuo** de una división (`10 % 3 = 1`).  
- `DIV` o `//` devuelve el **cociente entero** (`10 // 3 = 3`).  

---

## **🔹 Jerarquía de Operaciones con Operadores Lógicos**
📌 **Reglas de Prioridad en Operadores Lógicos**
| **Orden** | **Operadores** | **Ejemplo** |
|-----------|--------------|-------------|
| 1️⃣ **Negación** (`NO`, `not`) | `NO (A Y B)` |
| 2️⃣ **AND (Y)** | `A Y B` |
| 3️⃣ **OR (O)** | `A O B` |

📌 **Ejemplo 4 - Evaluación de expresiones lógicas**  
```pseudocode
Inicio
    Logico resultado
    resultado = NO (FALSO O VERDADERO) Y VERDADERO
    Escribir "Resultado:", resultado  // Salida: FALSO
Fin
```
📌 **Ejemplo en Python:**
```python
resultado = not (False or True) and True
print("Resultado:", resultado)  # Salida: False
```
✅ **Explicación:**  
- `NO (FALSO O VERDADERO)` → `NO VERDADERO` → `FALSO`  
- `FALSO Y VERDADERO` → `FALSO`  

---

## **🔹 Jerarquía de Operaciones en Expresiones Complejas**
📌 **Ejemplo 5 - Expresión Compleja**  
```pseudocode
Inicio
    Real resultado
    resultado = (10 + 2) * 3 ^ 2 / 6 - 4 MOD 3
    Escribir "Resultado:", resultado
Fin
```
📌 **Ejemplo en Python:**
```python
resultado = (10 + 2) * 3 ** 2 / 6 - 4 % 3
print("Resultado:", resultado)
```
✅ **Explicación Paso a Paso:**  
1. **Paréntesis** → `(10 + 2) = 12`  
2. **Exponente** → `3^2 = 9`  
3. **Multiplicación** → `12 * 9 = 108`  
4. **División** → `108 / 6 = 18`  
5. **Módulo** → `4 MOD 3 = 1`  
6. **Resta** → `18 - 1 = 17`  

**Salida Final:** `17`  

---

## **📌 Resumen Final**
| **Operación** | **Ejemplo** | **Prioridad** |
|--------------|------------|--------------|
| **Paréntesis** | `(5 + 3) * 2` | **Alta** |
| **Exponentes** | `2 ^ 3 = 8` | **Alta** |
| **Multiplicación y División** | `10 / 2 * 3` | **Media** |
| **Suma y Resta** | `8 - 3 + 2` | **Baja** |
| **Módulo y División Entera** | `10 MOD 3`, `10 DIV 3` | **Media** |
| **Operadores Lógicos** | `NO A`, `A Y B`, `A O B` | **Orden de Lógica** |

---
